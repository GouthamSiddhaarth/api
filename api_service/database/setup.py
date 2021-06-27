from api_service.database.models import db, Item


def setup_db():
    db.create_all()
    item = Item.query.all()
    if not item:
        item = Item(file_name='Sample File', media_type='mp4')
        db.session.add(item)
        db.session.commit()
