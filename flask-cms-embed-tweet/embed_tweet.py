from flask import Flask
from app import blog

app = Flask(__name__)
app.register_blueprint(blog, url_prefix='/blog')


@app.route('/')
def hello_world():
    return 'Homepage of our sample app. Go to /blog'
