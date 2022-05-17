import os
import uvicorn
import pandas as pd

from dotenv import load_dotenv

from elasticsearch import Elasticsearch, helpers

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Post
from models import Post as ModelPost

from schema import IdToDel as SchemaIdToDel
from schema import Req as SchemaReq

from sqlalchemy import desc

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DB_URL'])

es_client = Elasticsearch('http://elsearch:9200')


@app.post('/find-posts/')
def find_by_req(req: SchemaReq):
    if es_client.indices.exists(index='posts'):
        found_items = helpers.scan(es_client, index='posts', query={
            'query': {
                'match': {
                    'text': req.text
                }
            }
        })
    else:
        return None

    cnt = 0
    found_indices = []
    for item in found_items:
        found_indices.append(int(item['_id']))
        cnt += 1
        if cnt == 20:
            break

    items = db.session.query(Post).filter(Post.id.in_(found_indices)).order_by(desc(Post.created_date)).all()
    return items if items else None


@app.post('/delete-doc/')
def delete_doc(id_to_del: SchemaIdToDel):

    es_client.options(ignore_status=[404]).delete(index='posts', id=str(id_to_del.id))

    try:
        db_post = db.session.query(Post).filter(Post.id == id_to_del.id).one()
        db.session.delete(db_post)
        db.session.commit()
    except:
        return None

    return db_post


@app.get('/all-posts/')
def all_posts():
    return db.session.query(Post).order_by(Post.id).all()


@app.post('/upload-data/')
def upload():

    if db.session.query(Post).count() != 0:
        db.session.query(Post).delete()

    df = pd.read_csv('posts.csv')
    df_len = df.shape[0]
    df['index'] = [i for i in range(1, df_len+1)]
    texts = df['text']

    for value in df.values:
        db_post = ModelPost(
            id=value[3],
            text=value[0],
            created_date=value[1],
            rubrics=value[2][1:-1]
        )
        db.session.add(db_post)

    db.session.commit()

    es_client.options(ignore_status=[404]).indices.delete(index='posts')
    es_client.options(ignore_status=[400]).indices.create(index='posts')

    actions = [
        {
            '_index': 'posts',
            '_id': i,
            '_source': {
                'text': texts[i - 1]
            }
        }
        for i in range(1, df_len + 1)
    ]

    helpers.bulk(es_client, actions)

    return 'Data uploaded successfully'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
