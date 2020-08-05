import os
import sys
import flask
import pypi_org.data.db_session as db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.db')
    db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    app.register_blueprint(home_views.blueprint)
    from pypi_org.views import package_views
    app.register_blueprint(package_views.blueprint)


# account stuff will go here

if __name__ == '__main__':
    main()
else:
    register_blueprints()
    setup_db()
