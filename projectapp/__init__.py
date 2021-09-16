from flask import Flask
from projectapp.api import apiobj
from projectapp.site import siteobj

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    from projectapp import config
    app.config.from_object(config.LiveConfig)
    app.config.from_pyfile('config.py') 
    from projectapp.mymodel import db #instantiated as db=SQLAlchemy()
    db.init_app(app)
    app.register_blueprint(apiobj)
    app.register_blueprint(siteobj)
    return app

from projectapp import forms
from projectapp import mymodel



