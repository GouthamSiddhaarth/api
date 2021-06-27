from flask import request, jsonify
from flask_restful import Resource
from api_service.database.models import Item, db
from sqlalchemy.exc import IntegrityError
from api_service.resources.errors import (
    InternalServerError, InvalidParameterError, SchemaValidationError)


class ItemsApi(Resource):
    def get(self):
        items = Item.query.all()
        # items_json= jsonify({"items": [item.as_dict() for item in items]})
        return jsonify({"items": [item.as_dict() for item in items]})

    def post(self):
        if all(k in request.json for k in ("file_name", "media_type")):
            file_name = request.json['file_name']
            media_type = request.json['media_type']
        else:
            raise InvalidParameterError
        try:
            item = Item(file_name=file_name if file_name else None,
                        media_type=media_type if media_type else None)
            db.session.add(item)
            db.session.commit()
            return {'id': str(item.id)}, 200
        except IntegrityError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


class ItemApi(Resource):
    def get(self, id):
        item = Item.query.get_or_404(id)
        return jsonify(item.as_dict())

    def put(self, id):
        try:
            item = Item.query.get_or_404(id)
            if 'file_name' in request.json:
                file_name = request.json['file_name']
                item.file_name = file_name if file_name else None
            if 'media_type' in request.json:
                media_type = request.json['media_type']
                item.media_type = media_type if media_type else None
            db.session.add(item)
            db.session.commit()
            return {"message": "Updated Successfully",
                    "status": 200}
        except IntegrityError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Deleted Successfully",
                "status": 200}
