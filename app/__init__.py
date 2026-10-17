from flask import Flask
from .models import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+app.instance_path+'/app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists
        try:
            app.config.from_pyfile('config.py', silent=True)
        except Exception:
            pass
    else:
        app.config.update(test_config)

    # ensure the instance folder exists
    import os
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    return app
