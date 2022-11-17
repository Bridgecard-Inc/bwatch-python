# from typing import Optional
# from fastapi import Header
# from firebase_admin import auth
# from src.crud.super_admin import crud_super_admin
# from src.core.error import InvalidToken, MissingPermission
# from src.schema.auth import ValidatedUserDetails
# import logging
# from src.utils import constants


# logger = logging.getLogger(__name__)

# PREFIX = "Bearer"


# def parse_auth_token_from_header(header: str):
#     if header is None:
#         raise InvalidToken
#     if not header.startswith(PREFIX):
#         logger.error("Invalid Authentication Token")
#         raise InvalidToken

#     return header[len(PREFIX) :].lstrip()



# def verifyToken( token: Optional[str] = Header(None)):

#     # logger.info("This is token f{token}")
    
#     try:
#         parsed_token = parse_auth_token_from_header(token)
#         decoded_token = auth.verify_id_token(parsed_token)
#         uid = decoded_token["uid"]
#         team_member_id = uid
#         user = auth.get_user(uid=uid)

#         # print(user.custom_claims)
#         if user.custom_claims != None:
#             if "team_id" in user.custom_claims:
#                 uid = user.custom_claims.get("team_id") or ""

#         return ValidatedUserDetails(id=uid, token=parsed_token, team_member_id=team_member_id)
        
#     except:
#         raise InvalidToken



# def verifyAdminToken( token: Optional[str] = Header(None)):
    
#     try:
#         parsed_token = parse_auth_token_from_header(token)
#         decoded_token = auth.verify_id_token(parsed_token)
#         uid = decoded_token["uid"]

#         user_detail = crud_super_admin.get(id=uid)
#     except:
#         raise InvalidToken

#     else:
#           if not user_detail.get(constants.IS_DEDICATED_SUPER_ADMIN_NODE_NAME):
#             raise MissingPermission
        
    
#     return ValidatedUserDetails(id=uid, token=parsed_token)
        