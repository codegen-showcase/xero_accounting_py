import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /BankTransfers endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.bank_transfers.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        bank_transfers=[
            {
                "amount": 123.45,
                "bank_transfer_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "created_date_utc": "/Date(1573755038314)/",
                "currency_rate": 123.45,
                "date": "string",
                "from_bank_account": {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "add_to_watchlist": True,
                    "bank_account_number": "string",
                    "bank_account_type": "BANK",
                    "class_": "ASSET",
                    "code": "string",
                    "currency_code": "AED",
                    "description": "string",
                    "enable_payments_to_account": True,
                    "has_attachments": True,
                    "name": "Food Sales",
                    "reporting_code": "string",
                    "reporting_code_name": "string",
                    "show_in_expense_claims": True,
                    "status": "ACTIVE",
                    "system_account": "BANKCURRENCYGAIN",
                    "tax_type": "string",
                    "type_": "BANK",
                    "updated_date_utc": "/Date(1573755038314)/",
                    "validation_errors": [{"message": "string"}],
                },
                "from_bank_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "from_is_reconciled": True,
                "has_attachments": True,
                "reference": "string",
                "to_bank_account": {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "add_to_watchlist": True,
                    "bank_account_number": "string",
                    "bank_account_type": "BANK",
                    "class_": "ASSET",
                    "code": "string",
                    "currency_code": "AED",
                    "description": "string",
                    "enable_payments_to_account": True,
                    "has_attachments": True,
                    "name": "Food Sales",
                    "reporting_code": "string",
                    "reporting_code_name": "string",
                    "show_in_expense_claims": True,
                    "status": "ACTIVE",
                    "system_account": "BANKCURRENCYGAIN",
                    "tax_type": "string",
                    "type_": "BANK",
                    "updated_date_utc": "/Date(1573755038314)/",
                    "validation_errors": [{"message": "string"}],
                },
                "to_bank_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "to_is_reconciled": True,
                "validation_errors": [{"message": "string"}],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /BankTransfers endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.bank_transfers.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        bank_transfers=[
            {
                "amount": 123.45,
                "bank_transfer_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "created_date_utc": "/Date(1573755038314)/",
                "currency_rate": 123.45,
                "date": "string",
                "from_bank_account": {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "add_to_watchlist": True,
                    "bank_account_number": "string",
                    "bank_account_type": "BANK",
                    "class_": "ASSET",
                    "code": "string",
                    "currency_code": "AED",
                    "description": "string",
                    "enable_payments_to_account": True,
                    "has_attachments": True,
                    "name": "Food Sales",
                    "reporting_code": "string",
                    "reporting_code_name": "string",
                    "show_in_expense_claims": True,
                    "status": "ACTIVE",
                    "system_account": "BANKCURRENCYGAIN",
                    "tax_type": "string",
                    "type_": "BANK",
                    "updated_date_utc": "/Date(1573755038314)/",
                    "validation_errors": [{"message": "string"}],
                },
                "from_bank_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "from_is_reconciled": True,
                "has_attachments": True,
                "reference": "string",
                "to_bank_account": {
                    "account_id": "00000000-0000-0000-0000-000000000000",
                    "add_to_watchlist": True,
                    "bank_account_number": "string",
                    "bank_account_type": "BANK",
                    "class_": "ASSET",
                    "code": "string",
                    "currency_code": "AED",
                    "description": "string",
                    "enable_payments_to_account": True,
                    "has_attachments": True,
                    "name": "Food Sales",
                    "reporting_code": "string",
                    "reporting_code_name": "string",
                    "show_in_expense_claims": True,
                    "status": "ACTIVE",
                    "system_account": "BANKCURRENCYGAIN",
                    "tax_type": "string",
                    "type_": "BANK",
                    "updated_date_utc": "/Date(1573755038314)/",
                    "validation_errors": [{"message": "string"}],
                },
                "to_bank_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "to_is_reconciled": True,
                "validation_errors": [{"message": "string"}],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /BankTransfers/{BankTransferID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.bank_transfers.get(
        bank_transfer_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /BankTransfers/{BankTransferID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.bank_transfers.get(
        bank_transfer_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /BankTransfers endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.bank_transfers.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        where="HasAttachments==true",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /BankTransfers endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.bank_transfers.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        where="HasAttachments==true",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /BankTransfers endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.bank_transfers.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        where="HasAttachments==true",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /BankTransfers endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.BankTransfers

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.bank_transfers.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        where="HasAttachments==true",
    )
    try:
        pydantic.TypeAdapter(models.BankTransfers).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
