from api_service.resources.item import ItemsApi, ItemApi


def initialize_routes(api):
    api.add_resource(ItemsApi, '/items')
    api.add_resource(ItemApi, '/items/<id>')
