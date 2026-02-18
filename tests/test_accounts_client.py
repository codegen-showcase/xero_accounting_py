import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Accounts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        account_id="00000000-0000-0000-0000-000000000000",
        add_to_watchlist=True,
        bank_account_number="string",
        bank_account_type="BANK",
        class_="ASSET",
        code="4400",
        currency_code="AED",
        description="string",
        enable_payments_to_account=True,
        has_attachments=False,
        name="Food Sales",
        reporting_code="string",
        reporting_code_name="string",
        show_in_expense_claims=True,
        status="ACTIVE",
        system_account="BANKCURRENCYGAIN",
        tax_type="string",
        type_="BANK",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Accounts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        account_id="00000000-0000-0000-0000-000000000000",
        add_to_watchlist=True,
        bank_account_number="string",
        bank_account_type="BANK",
        class_="ASSET",
        code="4400",
        currency_code="AED",
        description="string",
        enable_payments_to_account=True,
        has_attachments=False,
        name="Food Sales",
        reporting_code="string",
        reporting_code_name="string",
        show_in_expense_claims=True,
        status="ACTIVE",
        system_account="BANKCURRENCYGAIN",
        tax_type="string",
        type_="BANK",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /Accounts/{AccountID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.update(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        accounts=[
            {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "add_to_watchlist": True,
                "bank_account_number": "string",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "4400",
                "currency_code": "AED",
                "description": "string",
                "enable_payments_to_account": True,
                "has_attachments": False,
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
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /Accounts/{AccountID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.update(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        accounts=[
            {
                "account_id": "00000000-0000-0000-0000-000000000000",
                "add_to_watchlist": True,
                "bank_account_number": "string",
                "bank_account_type": "BANK",
                "class_": "ASSET",
                "code": "4400",
                "currency_code": "AED",
                "description": "string",
                "enable_payments_to_account": True,
                "has_attachments": False,
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
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Accounts/{AccountID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.get(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Accounts/{AccountID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.get(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Accounts endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Name ASC",
        where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Accounts endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Name ASC",
        where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Accounts endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Name ASC",
        where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Accounts endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Name ASC",
        where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_200_success_all_params() -> None:
    """Tests a DELETE request to the /Accounts/{AccountID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.accounts.delete(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params() -> None:
    """Tests a DELETE request to the /Accounts/{AccountID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Accounts

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.accounts.delete(
        account_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Accounts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
