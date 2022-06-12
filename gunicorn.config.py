# Copied from https://github.com/ytimocin/flask-postgres-server/blob/master/gunicorn.config.py
import multiprocessing

bind = "0.0.0.0:5000"

workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 1000
