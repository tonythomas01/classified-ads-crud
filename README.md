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


**Known issues**: 
- Postgresql can error out on the first boot, due to some hba.conf missing 
  reason. This is fixed by simply restarting `docker-compose` using
```
$ docker-compose restart 
```
- Web service restarts a bit until potsgresql service is up .
