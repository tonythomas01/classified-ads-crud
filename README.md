# Classfied Ads CRUD API  

Project structure copied from: https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#project-structure

Shipped with a `docker-compose` that can setup a PostgresSQL server with 
volume on `./posgres-data` for persistance.  

**Setup**: 
```
$ vi env.dev  # Modify the values correctly 
$ docker-compose build
$ docker-compose up -d
```
or to run locally, 
```
pyenv install 3.10.0 
# Make a virtual env out of it.
# TODO: Add docs to setup a virtual env.  
(venv-py-3.10)$ pip install -r requirements.txt 
(venv-py-3.10)$ # Optionally change .env.dev 
(venv-py-3.10)$ gunicorn -c gunicorn.config.py wsgi:app
```
The local version would talk to a temporary sqlite. You can change the 
settings by setting the following OS environment variables: 
```
export SQLALCHEMY_DATABASE_URI=sqlite:////tmp/test.db
```
or, likewise for postgresql. The app uses `pythonv3.10` 
**Tech used**:
- Python-Flask for web services 
- Flask-RESTful for REST services (resources)
- Flask-SQLAlchemy for talking to DBMS 
- marshmallow for serialization/de-serialization

**APIs**: 

@TODO: Document this later in swagger or something. 
* A way to insert a new ad. An ad consists of a subject, a body, an optional 
price, and
an email address.
```
curl --request POST \
  --url http://localhost:5000/api/v1/ads/ \
  --header 'Content-Type: application/json' \
  --data '{
	"subject": "Ad Name", 
	"body": "This is a very short body.", 
	"price": 50000, 
	"currency": "SEK", 
	"email": "teggggter@gmail.com"
}'
```

* A way of fetching existing ads. It should be possible to sort the ads on the time they
were inserted and by their price.
```
curl --request GET \
  --url 'http://localhost:5000/api/v1/ads/?sort=creation&orderBy=asc'
```
or 
```
curl --request GET \
  --url 'http://localhost:5000/api/v1/ads/?sort=price&orderBy=asc'
```
- A way of deleting a previously inserted ad.
```
curl --request DELETE \
  --url http://localhost:5000/api/v1/ads/1/
```



**TODOS**: 
- Tests need models imoprted inline, because of db_session being global in 
  database.py. This has to be fixed properly. 
- Pagination on the listing API
- Better handling of the Sessions (making it easier to test)
- `pytest` do not want to run locally on shell, however runs on pycharm.
- Handle database connect timeout correctly so that the app can wait until 
  postgresql service is up. 
- Figure out if changes in the codebase is reflected correctly in the 
  docker environment. We have a volume mount setup, but I could not test it. 
- Handle migrations. alembic is installed, but not setup. 


**Known issues**: 
- Postgresql can error out on the first boot, due to some hba.conf missing 
  reason. This is fixed by simply restarting `docker-compose` using
```
$ docker-compose restart 
```
- Web service restarts a bit until potsgresql service is up .
- Problems running pytest locally via CLI. 
