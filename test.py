import pandas as pd
from elasticsearch import Elasticsearch, helpers

df = pd.read_csv('posts.csv')
df_len = df.shape[0]
df['index'] = [i for i in range(1, df_len+1)]

print(df.created_date)

# client = Elasticsearch('http://localhost:9200')
#
# client.options(ignore_status=[404]).indices.delete(index='posts')
# client.options(ignore_status=[400]).indices.create(index='posts')
#
# actions = [
#   {
#     '_index': 'posts',
#     '_id': i,
#     '_source': {
#         'text': df['text'][i-1]
#     }
#   }
#   for i in range(1, df_len+1)
# ]
#
# helpers.bulk(client, actions)

# reqs = ['привет всем', 'здравствуйте', 'лол', 'хахаха']
#
# for req in reqs:
#     results = helpers.scan(client, index='posts', query={
#         'query': {
#             'match': {
#                 'text': req
#             }
#         }
#     })
#
#     cnt = 0
#     found_indices = []
#     for item in results:
#         print(type(item['_id']))
#         found_indices.append(item['_id'])
#         print(item['_id'], item['_source'])
#         cnt += 1
#         if cnt == 20:
#             break

