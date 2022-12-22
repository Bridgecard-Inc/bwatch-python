# Bwatch - A library that lets you quickly add simple to complex rules to your API's to combat fraud.

## How to Integrate:

### 1. Installation

pip install git+https://github.com/Bridgecard-Inc/bwatch-python.git#egg=bwatch-python

### 2. Initialization

```python
from bwatch_python import bwatch_python

bwatch_python.init(
        auth_data={
            "app_id": settings.BWATCH_APP_ID,
            "auth_token": settings.BWATCH_AUTH_TOKEN,
            "secret_key": settings.BWATCH_SECRET_KEY,
        },
        middleware_data={
            "url_to_track_on_middleware": settings.BWATCH_MIDDLEWARE_URL  ,
            "id_to_track_on_middleware": "personId",
        },
        data_mappers={
            "transactions": BwatchUtil.get_bwatch_transaction_mapping_json(),
            "customers": BwatchUtil.get_bwatch_customer_mapping_json(),
        },
    )
```

### 3. Create customer sample

```python

 BwatchUtil.create_customer_from_cardholder(
        input_data=input_data, cardholder_id=person_id, issuing_app_id=""
    )
```

### 4. Process customer transaction via middleware


```python
from bwatch_python.middleware.bwatch_middleware import BWatchAsgiMiddleware

app.add_middleware(BWatchAsgiMiddleware)
```

### 5. Process customer transaction via process_as_middleware function


```python
from bwatch_python.middleware.bwatch_middleware import process_as_middleware

response = process_as_middleware(
        url=settings.BWATCH_MIDDLEWARE_URL,
        body={
            "id": "d742f62b-2939-4e65-a1eb-550a5181cecb-5",
            "amount": "2000.00",
            "transferType": "intrabank",
            "subType": "accountCreationCredit",
            "description": "Account Opened",
            "balance": "1000.00",
        },
    )

    if response is not None:

        return response

    response = BaseResponseSchema(
        status="success",
        message="transaction successful",
        data={},
    )

    return response.dict()
```

