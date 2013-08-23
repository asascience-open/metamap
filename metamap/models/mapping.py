from datetime import datetime
from metamap import db
from flask.ext.mongokit import Document
from bson import ObjectId

@db.register
class Mapping(Document):
    __collection__ = 'mappings'
    use_dot_notation = True
    use_schemaless = True

    structure = {
        'ioos_name' : unicode, # ioos concept name
        'queries'   : [{'source_type' :ObjectId,
                        'query'       :unicode}],
        'created'   : datetime,
        'updated'   : datetime,
    }

    default_values = {
        'created': datetime.utcnow
    }


