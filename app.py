import connexion


def create_app():

    app = connexion.FlaskApp(__name__.split('.')[0], options={"swagger_ui": False, "serve_spec": False})
    app.add_api('openapi.yml')

    # flask app
    app = app.app
    # flask-specific code
    return app