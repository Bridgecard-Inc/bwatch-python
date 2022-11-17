import firebase_admin
from firebase_admin import db, credentials
from src.bwatch_python.data.core.config import settings
from src.bwatch_python.data.utils.decode_base_64_to_json_helper import decode_base_64_to_json


cred = credentials.Certificate(decode_base_64_to_json(settings.GOOGLE_CONFIG_BASE64))

firebase_admin.initialize_app(cred, {"databaseURL": settings.DATABASE_URL})
bwatch_data_db_app = firebase_admin.initialize_app(cred, {
        'databaseURL': settings.BWATCH_DATABASE_URL
    }, name='bwatch_data_db_app')
bwatch_data_db = db.reference("company_users", bwatch_data_db_app)
bwatch_data_company_to_user_mapping = db.reference("company_to_user_mapping", bwatch_data_db_app)

root_db = db.reference()
