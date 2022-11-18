from base64 import b64encode
import os
from typing import Any, Dict, Optional
# from src.schema.base import EnvironmentEnum

from firebase_admin import auth
from ...core.crud_base import CRUDBase

from bwatch_python.data.database.db import bwatch_data_customers_db

from ....utils import bwatch_python_data_context


class CRUDCustomer(CRUDBase):
    def __init__(self, path: str):
        """CRUD object with default methods to Create, Read, Update, Delete (CRUD)."""
        self.db_ref = bwatch_data_customers_db.child(bwatch_python_data_context.app_id)

    def create(self, *, obj_in: Dict) -> Dict:
        """
        Creates data in the database.

        Args:
            obj_in (Dict): the data to be inserted to the database.

        Returns:

            Optional[Dict]: The data dictionary from the database or None on an Exception.

        """
        customer_dict = obj_in
        try:            
            self.db_ref.child(obj_in["id"]).set(customer_dict)
            return customer_dict
        except:
            return {}
    
    def fetch_db(self,id:str):
        try:
            data=self.db_ref.child(id).get()
            if data:
                return data
        except:
            return None


crud_customer = CRUDCustomer("customers")
