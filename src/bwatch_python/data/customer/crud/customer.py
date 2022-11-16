from base64 import b64encode
import os
from typing import Any, Dict, Optional
# from src.schema.base import EnvironmentEnum
from schema.cusotmer_data import Customer
from src.bwatch_python.data.utils import constants

from firebase_admin import auth
from .base import CRUDBase

from src.bwatch_python.data.database.db import root_db


class CRUDCustomer(CRUDBase):
    def __init__(self, path: str):
        """CRUD object with default methods to Create, Read, Update, Delete (CRUD)."""
        self.db_ref = super().__init__(path)

    def create(self, *, obj_in: Customer) -> Dict:
        """
        Creates data in the database.

        Args:
            obj_in (Dict): the data to be inserted to the database.

        Returns:

            Optional[Dict]: The data dictionary from the database or None on an Exception.

        """
        customer_dict = obj_in.dict()
        try:            
            self.db_ref.child(obj_in.customer_data.id).set(customer_dict)
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

    # def filter_db(self, field: str, value: str):
    #     ordered_dict_data = self.db_ref.order_by_child(
    #         field).equal_to(value).get()

    #     dict_data = dict(ordered_dict_data)

    #     if ordered_dict_data is None:
    #         return None

    #     elif dict_data == {}:
    #         return None

    #     dict_key = list(dict_data.keys())[0]
    #     return dict_data[dict_key]

    # def push_to_child_node(self, id: str, field: str, value: dict):
    #     """
    #     Adds data to a child node.

    #     Args:
    #         id (str): the primarykey/indentifier.

    #         field (str): the name of the child field

    #         value (dict): the data to be added onto the child node.
    #     Returns:

    #         boolean: A boolean value indicating whether the operation was successful or not.

    #     """
    #     try:
    #         self.db_ref.child(id).child(f"{field}").push(value)
    #         return True
    #     except:
    #         return False

    # def set_child_node(self, id: str, field: str, value: dict):
    #     """
    #     Adds data to a child node.

    #     Args:
    #         id (str): the primarykey/indentifier.

    #         field (str): the name of the child field

    #         value (dict): the data to be added onto the child node.
    #     Returns:

    #         boolean: A boolean value indicating whether the operation was successful or not.

    #     """
    #     try:
    #         self.db_ref.child(id).child(f"{field}").set(value)
    #         return True
    #     except:
    #         return False

    # def update(self, *, id: str, obj: dict) -> bool:

    #     try:
    #         self.db_ref.child(id).update(obj)
    #         if obj.get("work_email") is not None:
    #             auth.update_user(id, email=obj["work_email"])
    #         return obj
    #     except:
    #         return False

    # def update_team_members_details(self, *, id: str, obj: dict) -> bool:

    #     try:

    #         work_email = obj["work_email"]

    #         email = b64encode(work_email.encode('ascii')).decode("ascii")

    #         self.db_ref.child(id).child(
    #             constants.TEAM_MEMBERS_CHILD_NODE_PATH_NAME).child(email).update(obj)

    #         return obj

    #     except:
    #         return False

    # def delete_team_members_details(self, *, id: str, work_email: str) -> bool:
    #     try:

    #         email = b64encode(work_email.encode('ascii')).decode("ascii")

    #         self.db_ref.child(id).child(
    #             constants.TEAM_MEMBERS_CHILD_NODE_PATH_NAME).child(email).delete()

    #         return True
    #     except:
    #         return False

    # def update_accounts_token_claim(self, *, id: str, obj: dict) -> bool:

    #     try:
    #         auth.set_custom_user_claims(id, obj)
    #         return True
    #     except:
    #         return False

    # def check_if_accountsistrator_exists(
    #     self,
    #     email: str,
    # ):
    #     try:

    #         auth.get_user_by_email(email).uid

    #         return True

    #     except:
    #         return False

    # def check_if_team_member_exists(
    #     self,
    #     id: str,
    #     email: str,
    # ):
    #     email = b64encode(email.encode('ascii')).decode("ascii")

    #     team_member_data = self.db_ref.child(id).child(
    #         constants.TEAM_MEMBERS_CHILD_NODE_PATH_NAME).child(email).get()

    #     if team_member_data == None:

    #         return False

    #     return True

    # def verify_accounts_issuing_transactions(
    #     self,
    #     id: str,
    #     currency: str,
    #     environment: str,
    #     trasanction_id: str,
    # ):

    #     all_transactions = self.db_ref.child(id).child(
    #         constants.ISSUING_TRANSACTIONS_CHILD_NODE_PATH_NAME + f"/{currency}/{environment}").child(trasanction_id).get()

    #     if all_transactions == None:

    #         return False

    #     return True

    # def fetch_accounts_issuing_transactions(
    #     self,
    #     id: str,
    #     currency: str,
    #     environment: str,
    #     page: int
    # ):

    #     all_transactions = self.db_ref.child(id).child(
    #         constants.ISSUING_TRANSACTIONS_CHILD_NODE_PATH_NAME + f"/{currency}/{environment}").get()

    #     if all_transactions == None:

    #         pagination = Pagination(
    #             total=0, pages=pages, previous=None, next=None)
    #         result = IssuingTransactionsOutSchema(
    #             status="success", message="Issuing Transactions Fetched successfully", data=[], meta=pagination)
    #         return result.dict()

    #     all_transactions = list(all_transactions.values())

    #     tuple_keys = ('amount', 'created_at',
    #                   'currency', 'description', 'type')

    #     all_transactions = [dict((k, d.get(k, None))
    #                              for k in tuple_keys) for d in all_transactions]

    #     all_transactions = sorted(
    #         all_transactions, key=lambda i: i['created_at'], reverse=True)

    #     if len(all_transactions) % 20 == 0:
    #         pages = len(all_transactions)/20
    #     else:
    #         pages = int(len(all_transactions)/20)
    #         pages += 1

    #     if environment == EnvironmentEnum.production.value:
    #         url = constants.BASE_URL + \
    #             f"/v1/accounts/{id}/issuing-transactions/{currency}/{environment}"
    #     else:
    #         url = constants.BASE_URL + \
    #             f"/v1/accounts/{id}/issuing-transactions/{currency}/{environment}"

    #     if len(all_transactions) > (page+1) * 20 or len(all_transactions) > (page * 20):
    #         next_page = page+1
    #         next_page = f"{url}?page={next_page}"
    #     else:
    #         next_page = None

    #     if page == 1:
    #         pagination = Pagination(
    #             total=len(all_transactions), pages=pages, previous=None, next=next_page)
    #         result = IssuingTransactionsOutSchema(
    #             status="success", message="Issuing Transactions Fetched successfully", data=all_transactions[:20], meta=pagination)
    #         return result.dict()

    #     elif len(all_transactions) > page * 20:
    #         previous_page = f"{url}?page={(page-1)}"

    #         pagination = Pagination(total=len(
    #             all_transactions), pages=pages, previous=previous_page, next=next_page)
    #         result = IssuingTransactionsOutSchema(
    #             status="success", message="Issuing Transactions Fetched successfully", data=all_transactions[(page-1) * 20:page * 20], meta=pagination)
    #         return result.dict()

    #     elif len(all_transactions) > (page-1) * 20:
    #         previous_page = f"{url}?page={(page-1)}"

    #         pagination = Pagination(
    #             total=len(all_transactions), pages=pages, previous=previous_page, next=None)
    #         result = IssuingTransactionsOutSchema(
    #             status="success", message="Issuing Transactions Fetched successfully", data=all_transactions[(page-1) * 20:page * 20], meta=pagination)
    #         return result.dict()

    #     else:
    #         pagination = Pagination(
    #             total=len(all_transactions), pages=pages, previous=None, next=None)
    #         result = IssuingTransactionsOutSchema(
    #             status="success", message="Issuing Transactions Fetched successfully", data=[], meta=pagination)
    #         return result.dict()


crud_customer = CRUDCustomer("customers")
