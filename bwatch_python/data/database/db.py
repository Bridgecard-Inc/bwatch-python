import firebase_admin
from firebase_admin import db, credentials
from ..core.config import settings
from ...utils.decode_base_64_to_json_helper import decode_base_64_to_json


try:

    cred = credentials.Certificate(decode_base_64_to_json(settings.GOOGLE_CONFIG_BASE64))

    firebase_admin.initialize_app(cred, {"databaseURL": settings.DATABASE_URL})

    bwatch_data_db_app = firebase_admin.initialize_app(cred, {
            'databaseURL': settings.BWATCH_DATABASE_URL
        }, name='bwatch_data_db_app')

    bwatch_data_customers_db = db.reference("customers", bwatch_data_db_app)

    bwatch_data_transactions_db = db.reference("transactions", bwatch_data_db_app)

    root_db = db.reference()

except:

    ...

else:

    bwatch_data_db_app = firebase_admin.initialize_app(cred, {
            'databaseURL': settings.BWATCH_DATABASE_URL
        }, name='bwatch_data_db_app')

    bwatch_data_customers_db = db.reference("customers", bwatch_data_db_app)

    bwatch_data_transactions_db = db.reference("transactions", bwatch_data_db_app)

    root_db = db.reference()
