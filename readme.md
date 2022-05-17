Инструкция для запуска проекта:

Запустить Docker

git clone https://github.com/IlyasDevelopment/Elasticsearch

Перейти в папку с проектом cd Elasticsearch

docker-compose build

docker-compose run app alembic upgrade head

docker-compose up

Чтобы загрузить данные в базу данных и эластик, необходимо перейти на http://localhost:8000/docs и совершить post-запрос upload-data.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/1.png "Таблица")

После удаления документов из индекса можно снова совершить предыдущий запрос, данные перезальются, запрос идемпотентный.

По адресу http://localhost:5601 откроется Kibana, в ней удобно визуализировать запросы к Elasticsearch, также относится к ELK Stack.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/2.png "Таблица")

Консоль находится в Dev tools.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/3.png "Таблица")

Видим, что все 1500 записей добавились в индекс.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/4.png "Таблица")

Посмотрим теперь на PostgreSQL. По адресу http://localhost:7080 откроется сервис администрирования.

Логин: admin@admin.com

Пароль: adminpass

При первом запуске необходимо зарегистрировать сервер, для этого переходим в Add New Server.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/5.png "Таблица")

Name: db, далее переходим в пункт Connection.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/6.png "Таблица")

Hostname/address: db, Urename: postgres, Password: postgrespass

Нажимаем save.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/7.png "Таблица")

Данные загрузились успешно.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/8.png "Таблица")

Попробуем найти тексты по запросу "Всем привет". Сервис найдет все тексты, где встречается хотя бы одно из слов, но в целом вариантов настройки поиска много.

![alt text](https://github.com/IlyasDevelopment/Elasticsearch/blob/main/screenshots/9.png "Таблица")

Основные библиотеки
# pip install elasticsearch fastapi uvicorn fastapi-sqlalchemy alembic pydantic psycopg2 pandas python-dotenv
