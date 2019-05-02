import os
import config
from flask import Flask
from models.base_model import db
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'quando_api')


app = Flask('QUANDO', root_path=web_dir)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc

