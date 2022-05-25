from flask import Flask, jsonify
from celery import Celery

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


@celery.task()
def add(x, y):
    return x + y


@app.route('/')
def add_task():
    for i in range(10000):
        add.delay(i, i)
    return jsonify({'status': 'ok'})
