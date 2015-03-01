from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "s3cr3t jhbijo kkii"

from app import views
