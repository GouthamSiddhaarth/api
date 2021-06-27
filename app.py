from api_service.database import app
from flask_restful import Api
from api_service.resources.routes import initialize_routes
from api_service.resources.errors import errors
from api_service.database.setup import setup_db

api = Api(app, errors=errors)
initialize_routes(api)

setup_db()

if __name__ == '__main__':
    app.run()
