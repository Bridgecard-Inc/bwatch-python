from typing import Any, Dict, List, Optional, TypeVar, Union

from bwatch_python.data.database.db import bwatch_data_db
from firebase_admin import auth



class CRUDBase:
    def __init__(self, path: str):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        """
        self.db_ref = bwatch_data_db

        return self.db_ref

    def get(self, id: str) -> Optional[Dict]:
        """
        Gets data from the database using the id.

        Args:
            id (str): the primarykey/indentifier.
        Returns:

            Optional[Dict]: The data dictionary from the database.

        """

        try:
            data = self.db_ref.child(id).get()
            return data
        except:
            return None

    def create(self, *, obj_in: Dict[str, Any]) -> Dict:
        """
        Creates data in the database.

        Args:
            obj_in (Dict): the data to be inserted to the database.

        Returns:

            Optional[Dict]: The data dictionary from the database or None on an Exception.

        """
        try:
            self.db_ref.child(obj_in["id"]).set(obj_in)
            return obj_in
        except:
            return None

    def remove(self, *, id: str) -> bool:
        """
        Removes data from the database using the id.

        Args:
            id (str): the primarykey/indentifier.

        Returns:

            boolean: A boolean value indicating whether the operation was successful or not.

        """
        try:
            auth.delete_user(id)
            self.db_ref.child(id).set({})
        except:
            return False

        return True

    def update(self, *, id: str, field: str, value: str) -> bool:
        """
        Updates data in the database using the id.

        Args:
            id (str): the primarykey/indentifier.

        Returns:

            boolean: A boolean value indicating whether the operation was successful or not.

        """
        try:
            self.db_ref.child(id).update({f"{field}": value})
        except:
            return False
        return True

    def get_child_node_value_as_list(self, id: str, field: str):

        """
        Gets a node's child values as a list.

        Args:
            id (str): the primarykey/indentifier.
            field (str): the name of the child field

        Returns:

            List[Dict]: A list of the node's child values or None on an Exception

        """
        try:
            data_dict = self.db_ref.child(id).child(f"{field}").get()
            data_dict_list = list(data_dict.values())
            return data_dict_list
        except:
            return None

    def get_child_node_value(self, id: str, field: str):

        """
        Gets a node's child value.

        Args:
            id (str): the primarykey/indentifier.
            field (str): the name of the child field

        Returns:

            Any: The node's child value or None on an Exception

        """
        try:
            data = self.db_ref.child(id).child(f"{field}").get()

            
            return data
        except:
            return None

    
    def get_api_stats(self, company_issuing_app_id: str):

        try:
            data = root_db.child("administrators_api_stats").child(company_issuing_app_id).get()

            final_dict = {
                "total_active_cards": {},
                "total_api_calls": {},
                "total_issued_cards": {},
                "total_transaction_volume": {},
                "total_transaction_volume_credits": {},
                "total_transaction_volume_debits": {},
            }
            stats_list = ['total_active_cards', 'total_api_calls', 'total_issued_cards', 'total_transaction_volume',
                         'total_transaction_volume_credits', 'total_transaction_volume_debits',
                         ]

            for stat in stats_list:
                final_dict[stat]["production"] = sortMonthList(data[stat]["production"])

                final_dict[stat]["sandbox"] = sortMonthList(data[stat]["sandbox"])
            return final_dict
        except:
            return None
