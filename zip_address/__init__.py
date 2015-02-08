from .apis import blueprint
from main import app_factory
from flask import (Flask, request_finished)
from database import Session
import config

app = Flask(__name__)
app = app_factory(config.Config, config.project_name)
app.register_blueprint(blueprint)
def remove_session(sender, response, **extra):
    Session.remove()

request_finished.connect(remove_session, app)
