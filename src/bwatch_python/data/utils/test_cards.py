import json
from src.main import app
from fastapi.testclient import TestClient
from src.core.config import settings
import src.core.error as errors
import src.tests.data as test_data 
import pytest
import logging

logger = logging.getLogger(__name__)


client = TestClient(app)


from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_402_PAYMENT_REQUIRED,
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
)
########CADRHOLDER TEST#######
# @pytest.mark.asyncio
# async def test_get_all_states():
  
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/get_all_states",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()
#     assert res.status_code == HTTP_200_OK
#     assert result["message"] ==  "States fetched successfully"



# @pytest.mark.asyncio
# async def test_get_all_lga():
  
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/get_all_lga?state=adamawa",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()
#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Local Governments fetched successfully"


# @pytest.mark.asyncio
# async def test_register_cardholder_bvn_is_blacklisted_error():
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_blacklisted_cardholder_bvn_data
#     )

#     result = res.json()

#     assert res.status_code == HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
#     message = await errors.parse_error(exception_class= errors.CustomerHasBeenBlacklisted)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_register_cardholder_id_is_blacklisted_error():
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_blacklisted_cardholder_id_data
#     )

#     result = res.json()

#     assert res.status_code == HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
#     message = await errors.parse_error(exception_class= errors.CustomerHasBeenBlacklisted)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_register_cardholder_nigeria():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_new_nigerian_cardholderdata,
#     )

#     result = res.json()
#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully, you\'ll recieve a webhook event when this user\'s identity has been verified.'



# @pytest.mark.asyncio
# async def test_register_cardholder_ghana():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_new_ghana_cardholderdata,
#     )

#     result = res.json()

#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully, you\'ll recieve a webhook event when this user\'s identity has been verified.'


# @pytest.mark.asyncio
# async def test_register_cardholder_kenya():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_new_kenya_cardholderdata,
#     )

#     result = res.json()

#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully, you\'ll recieve a webhook event when this user\'s identity has been verified.'



# @pytest.mark.asyncio
# async def test_register_cardholder_uganda():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.register_new_uganda_cardholderdata,
#     )

#     result = res.json()

#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully, you\'ll recieve a webhook event when this user\'s identity has been verified.'




# ########CARD TEST#############
# @pytest.mark.asyncio
# async def test_create_card_successfully():
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.create_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == "The virtual USD card was created successfully"


# #TODO: Test case for inactive cardholder and unverified card.

# @pytest.mark.asyncio
# async def test_creating_unavailable_card():
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.create_unavailable_card
#     )

#     result = res.json()
#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.CardTypeCurrentlyUnavailable)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_creating_card_for_invalid_cardholderid():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.create_card_for_invalid_cardholser
#     )

#     result = res.json()
#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardHolderID)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_creating_card_for_insufficient_fund():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {test_data.admin_with_no_balance}"},
#         json=test_data.create_card_successfully
#     )

#     result = res.json()
#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message = await errors.parse_error(exception_class= errors.InsufficientUSDBalance)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_fetch_card_details_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_details?card_id={test_data.valid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card details was fetched successfully"



# @pytest.mark.asyncio
# async def test_fetch_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_details?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_get_card_balance_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_balance?card_id={test_data.valid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card balance was fetched successfully"



# @pytest.mark.asyncio
# async def test_get_invalid_card_id_balance():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_balance?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_fund_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was funded successfully"



# @pytest.mark.asyncio
# async def test_fund_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_fund_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]

# @pytest.mark.asyncio
# async def test_fund_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was funded successfully"



# @pytest.mark.asyncio
# async def test_fund_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_fund_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_fund_card_with_insufficient_issuing_wallet_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message =  await errors.parse_error(exception_class= errors.InsufficientUSDBalance)
#     assert result["message"] == message["message"]["message"]

# @pytest.mark.asyncio
# async def test_unload_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.unload_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was unloaded successfully"



# @pytest.mark.asyncio
# async def test_unload_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_unload_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_unload_card_with_amount_greater_than_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message = await errors.parse_error(exception_class= errors.InsufficientCardBalance)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mock_card_debit_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.mock_card_successfully
#     )

#     result = res.json()
    
#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was charged successfully"



# @pytest.mark.asyncio
# async def test_mock_card_debit_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mock_card_debit_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mock_card_debit_with_amount_greater_than_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json=test_data.fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message = await errors.parse_error(exception_class= errors.InsufficientCardBalance)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_get_card_transactions_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_transactions?card_id={test_data.valid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"



# @pytest.mark.asyncio
# async def test_get_card_transactions_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_transactions?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_get_card_transactions_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_transactions?card_id={test_data.valid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"


# @pytest.mark.asyncio
# async def test_get_card_transactions_with_empty_transactions():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_transactions?card_id={test_data.frozen_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"


# @pytest.mark.asyncio
# async def test_get_card_transactions_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_card_transactions?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_freeze_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/freeze_card?card_id={test_data.frozen_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card has been frozen successfully"



# @pytest.mark.asyncio
# async def test_freeze_card_successfully_with_invalid_card_id_details():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/freeze_card?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_unfreeze_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unfreeze_card?card_id={test_data.frozen_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card has been unfrozen successfully"



# @pytest.mark.asyncio
# async def test_unfreeze_card_successfully_with_invalid_card_id_details():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/unfreeze_card?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_fund_issuing_wallet():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/fund_issuing_wallet",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#         json= test_data.fund_issuing_wallet_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Your issuing wallet was funded successfully"



# @pytest.mark.asyncio
# async def test_get_all_cards_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cards?page=1",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All your issued cards have been fetched successfully"



# @pytest.mark.asyncio
# async def test_get_all_cards_with_client_without_cards():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cards?page=1",
#         headers={"token": f"Bearer {test_data.admin_with_no_balance}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All your issued cards have been fetched successfully"



# @pytest.mark.asyncio
# async def test_get_all_cardholder_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cardholder?page=1",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All your cardholders have been fetched successfully"



# @pytest.mark.asyncio
# async def test_get_all_cardholder_with_client_without_cardholders():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cardholder?page=1",
#         headers={"token": f"Bearer {test_data.admin_with_no_balance}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All your cardholders have been fetched successfully"
    



# @pytest.mark.asyncio
# async def test_get_all_cardholder_cards_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cardholder_cards?cardholder_id={test_data.cardholder_with_cards}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All the cards for this cardholder have been fetched successfully"



# @pytest.mark.asyncio
# async def test_get_all_cardholder_cards_for_cardholder_without_card():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/sandbox/cards/get_all_cardholder_cards?cardholder_id={test_data.cardholder_without_cards}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "All the cards for this cardholder have been fetched successfully"



# @pytest.mark.asyncio
# async def test_process_all_webhook():
#     res = client.get(
#         f"{settings.API_V1_0STR}/issuing/cards/process_debit_transaction_webhook",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Webhook was processed successfully"


# @pytest.mark.asyncio
# async def test_maintenance_fee_collection_on_fresh_card():
    

#     res1 = client.get(
#         f"{settings.API_V1_0STR}/sandbox/cards/get_card_balance?card_id={test_data.test_maintenance_fee_collection_on_fresh_card_test_card_id}",
#         headers={"token": f"Bearer {settings.TEST_TOKEN}"},
#     )

    # assert res1.status_code == HTTP_200_OK
    # previous_card_balance = res1.json().get("balance")

    # assert previous_card_balance != None

    # res = client.patch(
    #     f"{settings.API_V1_0STR}/sandbox/cards/fund_card",
    #     headers={"token": f"Bearer {settings.TEST_TOKEN}"},
    #     json=test_data.test_maintenance_fee_collection_on_fresh_card_test_data
    # )

    # result = res.json()

    # assert res.status_code == HTTP_200_OK
    # assert result["message"] == "This card was funded successfully"

#TODO: test processing an already processed transaction ref
#TODO: test delete cardholder





################## MONO TESTS ##########################

# @pytest.mark.asyncio
# async def test_mono_register_cardholder_nigeria():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_create_mono_nigerian_cardholder,
#     )

#     result = res.json()
#     logger.info(f"this is the result {result}")
#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully.'



# @pytest.mark.asyncio
# async def test_mono_register_cardholder_kenya():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_create_mono_kenya_cardholder,
#     )

#     result = res.json()
#     logger.info(f"this is the result {result}")
#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully.'



# @pytest.mark.asyncio
# async def test_mono_register_cardholder_uganda():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_create_mono_uganda_cardholder,
#     )

#     result = res.json()
#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully.'



# @pytest.mark.asyncio
# async def test_mono_register_cardholder_ghana():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cardholder/register_cardholder",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_create_mono_ghana_cardholder,
#     )

#     result = res.json()
#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == 'cardholder created successfully.'


# @pytest.mark.asyncio
# async def test_mono_create_card_successfully():
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_mono_create_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_201_CREATED
#     assert result["message"] == "The virtual USD card was created successfully"


# @pytest.mark.asyncio
# async def test_mono_creating_unavailable_card():
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.test_create_unavailable_cards_mono
#     )

#     result = res.json()
#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.CardTypeCurrentlyUnavailable)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_creating_card_for_invalid_cardholderid():
  
#     res = client.post(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/create_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.create_card_for_invalid_cardholser
#     )

#     result = res.json()
#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardHolderID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_fetch_card_details_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_details?card_id={test_data.mono_valid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card details was fetched successfully"



# @pytest.mark.asyncio
# async def test_mono_fetch_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_details?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_get_card_balance_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_balance?card_id={test_data.mono_valid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card balance was fetched successfully"



# @pytest.mark.asyncio
# async def test_mono_get_invalid_card_id_balance():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_balance?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_mono_fund_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was funded successfully"



# @pytest.mark.asyncio
# async def test_mono_fund_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_fund_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]

# @pytest.mark.asyncio
# async def test_mono_fund_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was funded successfully"



# @pytest.mark.asyncio
# async def test_mono_fund_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_fund_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_fund_card_with_insufficient_issuing_wallet_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/fund_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message =  await errors.parse_error(exception_class= errors.InsufficientUSDBalance)
#     assert result["message"] == message["message"]["message"]

# @pytest.mark.asyncio
# async def test_mono_unload_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_unload_card_successfully
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was unloaded successfully"



# @pytest.mark.asyncio
# async def test_mono_unload_card_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_invalid_card_id
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_unload_card_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_unload_card_with_amount_greater_than_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unload_card",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message = await errors.parse_error(exception_class= errors.InsufficientCardBalance)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_mock_card_debit_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_mock_card_successfully
#     )

#     result = res.json()
    
#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card was charged successfully"



# @pytest.mark.asyncio
# async def test_mono_mock_card_debit_with_invalid_card_id():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_invalid_card_id 
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_mock_card_debit_with_used_transaction_ref():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_used_transaction_ref
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.TransactionReferenceAlreadyExists)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_mock_card_debit_with_amount_greater_than_balance():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/mock_debit_transaction",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"},
#         json=test_data.mono_fund_card_with_insufficient_balance
#     )

#     result = res.json()

#     assert res.status_code == HTTP_402_PAYMENT_REQUIRED
#     message = await errors.parse_error(exception_class= errors.InsufficientCardBalance)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_get_card_transactions_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_transactions?card_id={test_data.mono_valid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"



# @pytest.mark.asyncio
# async def test_mono_get_card_transactions_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_transactions?card_id={test_data.mono_invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_get_card_transactions_successfully():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_transactions?card_id={test_data.mono_valid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"


# @pytest.mark.asyncio
# async def test_mono_get_card_transactions_with_empty_transactions():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_transactions?card_id={test_data.mono_frozen_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "Card transaction history was fetched successfully"


# @pytest.mark.asyncio
# async def test_mono_get_card_transactions_invalid_card_id_details():
#     res = client.get(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/get_card_transactions?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]



# @pytest.mark.asyncio
# async def test_mono_freeze_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/freeze_card?card_id={test_data.mono_frozen_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card has been frozen successfully"



# @pytest.mark.asyncio
# async def test_mono_freeze_card_successfully_with_invalid_card_id_details():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/freeze_card?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]


# @pytest.mark.asyncio
# async def test_mono_unfreeze_card_successfully():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unfreeze_card?card_id={test_data.mono_frozen_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_200_OK
#     assert result["message"] == "This card has been unfrozen successfully"



# @pytest.mark.asyncio
# async def test_mono_unfreeze_card_successfully_with_invalid_card_id_details():
#     res = client.patch(
#         f"{settings.API_V1_0STR}/mono_issuing/sandbox/cards/unfreeze_card?card_id={test_data.invalid_card_id}",
#         headers={"token": f"Bearer {settings.MONO_ISSUING_TEST_KEY}"}
#     )

#     result = res.json()

#     assert res.status_code == HTTP_400_BAD_REQUEST
#     message = await errors.parse_error(exception_class= errors.InvalidCardID)
#     assert result["message"] == message["message"]["message"]




# 2022-10-01 15:58:56,050 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED
# 2022-10-01 15:58:56,051 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED
# 2022-10-01 15:58:56,051 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED = 28200
# 2022-10-01 15:58:56,591 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for 1stcapital
# 2022-10-01 15:58:56,591 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for 1stcapital
# 2022-10-01 15:58:56,591 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for 1stcapital = 0
# 2022-10-01 15:58:56,866 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Sproutly Inc
# 2022-10-01 15:58:56,866 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Sproutly Inc
# 2022-10-01 15:58:56,866 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Sproutly Inc = 300
# 2022-10-01 15:58:57,151 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payourse
# 2022-10-01 15:58:57,151 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payourse
# 2022-10-01 15:58:57,151 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payourse = 0
# 2022-10-01 15:58:57,415 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Borderless Money
# 2022-10-01 15:58:57,415 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Borderless Money
# 2022-10-01 15:58:57,415 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Borderless Money = 300
# 2022-10-01 15:58:57,832 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for BRIDGECARD
# 2022-10-01 15:58:57,832 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for BRIDGECARD
# 2022-10-01 15:58:57,833 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for BRIDGECARD = 300
# 2022-10-01 15:58:58,102 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payourse
# 2022-10-01 15:58:58,103 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payourse
# 2022-10-01 15:58:58,103 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payourse = 2700
# 2022-10-01 15:58:58,374 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Chace Inc
# 2022-10-01 15:58:58,374 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Chace Inc
# 2022-10-01 15:58:58,375 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Chace Inc = 0
# 2022-10-01 15:58:58,631 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Springstack Technologies Limited
# 2022-10-01 15:58:58,631 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Springstack Technologies Limited
# 2022-10-01 15:58:58,631 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Springstack Technologies Limited = 0
# 2022-10-01 15:58:59,197 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payday
# 2022-10-01 15:58:59,217 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payday
# 2022-10-01 15:58:59,217 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payday = 149400
# 2022-10-01 15:58:59,521 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Maplerad Limited 
# 2022-10-01 15:58:59,538 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Maplerad Limited 
# 2022-10-01 15:58:59,538 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Maplerad Limited  = 133500
# 2022-10-01 15:59:00,003 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Mono
# 2022-10-01 15:59:00,111 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Mono
# 2022-10-01 15:59:00,111 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Mono = 1274400
# 2022-10-01 15:59:00,382 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Pay Up Limited Company
# 2022-10-01 15:59:00,383 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Pay Up Limited Company
# 2022-10-01 15:59:00,383 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Pay Up Limited Company = 3900
# 2022-10-01 15:59:00,650 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Errand P LTD
# 2022-10-01 15:59:00,650 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Errand P LTD
# 2022-10-01 15:59:00,650 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Errand P LTD = 0
# 2022-10-01 15:59:00,970 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Bridgecard
# 2022-10-01 15:59:00,972 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Bridgecard
# 2022-10-01 15:59:00,972 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Bridgecard = 6600







# 2022-10-01 15:56:31,759 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED
# 2022-10-01 15:56:31,763 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED
# 2022-10-01 15:56:31,763 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for STANBUZZ TECHNOLOGY LIMITED = 28800
# 2022-10-01 15:56:32,569 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for 1stcapital
# 2022-10-01 15:56:32,570 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for 1stcapital
# 2022-10-01 15:56:32,570 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for 1stcapital = 0
# 2022-10-01 15:56:32,825 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Sproutly Inc
# 2022-10-01 15:56:32,826 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Sproutly Inc
# 2022-10-01 15:56:32,826 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Sproutly Inc = 300
# 2022-10-01 15:56:33,093 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payourse
# 2022-10-01 15:56:33,093 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payourse
# 2022-10-01 15:56:33,093 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payourse = 0
# 2022-10-01 15:56:33,352 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Borderless Money
# 2022-10-01 15:56:33,352 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Borderless Money
# 2022-10-01 15:56:33,353 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Borderless Money = 300
# 2022-10-01 15:56:33,750 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for BRIDGECARD
# 2022-10-01 15:56:33,750 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for BRIDGECARD
# 2022-10-01 15:56:33,750 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for BRIDGECARD = 600
# 2022-10-01 15:56:34,018 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payourse
# 2022-10-01 15:56:34,018 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payourse
# 2022-10-01 15:56:34,018 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payourse = 3000
# 2022-10-01 15:56:34,374 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Chace Inc
# 2022-10-01 15:56:34,374 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Chace Inc
# 2022-10-01 15:56:34,375 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Chace Inc = 0
# 2022-10-01 15:56:34,628 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Springstack Technologies Limited
# 2022-10-01 15:56:34,629 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Springstack Technologies Limited
# 2022-10-01 15:56:34,629 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Springstack Technologies Limited = 0
# 2022-10-01 15:56:34,908 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Payday
# 2022-10-01 15:56:34,923 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Payday
# 2022-10-01 15:56:34,924 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Payday = 174000
# 2022-10-01 15:56:35,183 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Maplerad Limited 
# 2022-10-01 15:56:35,190 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Maplerad Limited 
# 2022-10-01 15:56:35,190 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Maplerad Limited  = 149100
# 2022-10-01 15:56:35,600 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Mono
# 2022-10-01 15:56:35,674 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Mono
# 2022-10-01 15:56:35,674 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Mono = 1385100
# 2022-10-01 15:56:35,932 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Pay Up Limited Company
# 2022-10-01 15:56:35,933 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Pay Up Limited Company
# 2022-10-01 15:56:35,933 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Pay Up Limited Company = 8100
# 2022-10-01 15:56:36,190 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Errand P LTD
# 2022-10-01 15:56:36,190 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Errand P LTD
# 2022-10-01 15:56:36,190 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Errand P LTD = 0
# 2022-10-01 15:56:36,488 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L128  started collect_maintenance_fee for Bridgecard
# 2022-10-01 15:56:36,489 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L161  ended collect_maintenance_fee for Bridgecard
# 2022-10-01 15:56:36,489 loglevel=INFO   logger=src.crud.super_admin collect_card_maintenance_fee_from_companies() L163  total collect_maintenance_fee for Bridgecard = 10200