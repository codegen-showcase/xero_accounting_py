import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /LinkedTransactions endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LinkedTransactions

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
    response = client.linked_transactions.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        linked_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_line_item_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_transaction_type_code="ACCPAY",
        status="APPROVED",
        target_line_item_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        target_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        type_="BILLABLEEXPENSE",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /LinkedTransactions endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LinkedTransactions

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
    response = await client.linked_transactions.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        linked_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_line_item_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        source_transaction_type_code="ACCPAY",
        status="APPROVED",
        target_line_item_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        target_transaction_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        type_="BILLABLEEXPENSE",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LinkedTransactions

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
    response = client.linked_transactions.update(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        linked_transactions=[
            {
                "contact_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "linked_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_line_item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_transaction_type_code": "ACCPAY",
                "status": "APPROVED",
                "target_line_item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "target_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "type_": "BILLABLEEXPENSE",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LinkedTransactions

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
    response = await client.linked_transactions.update(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        linked_transactions=[
            {
                "contact_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "linked_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_line_item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "source_transaction_type_code": "ACCPAY",
                "status": "APPROVED",
                "target_line_item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "target_transaction_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "type_": "BILLABLEEXPENSE",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LinkedTransactions

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
    response = client.linked_transactions.get(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LinkedTransactions

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
    response = await client.linked_transactions.get(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /LinkedTransactions endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LinkedTransactions

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
    response = client.linked_transactions.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="00000000-0000-0000-0000-000000000000",
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        page=1,
        source_transaction_id="00000000-0000-0000-0000-000000000000",
        status="APPROVED",
        target_transaction_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /LinkedTransactions endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LinkedTransactions

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
    response = await client.linked_transactions.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="00000000-0000-0000-0000-000000000000",
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        page=1,
        source_transaction_id="00000000-0000-0000-0000-000000000000",
        status="APPROVED",
        target_transaction_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /LinkedTransactions endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.LinkedTransactions

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
    response = client.linked_transactions.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="00000000-0000-0000-0000-000000000000",
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        page=1,
        source_transaction_id="00000000-0000-0000-0000-000000000000",
        status="APPROVED",
        target_transaction_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /LinkedTransactions endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.LinkedTransactions

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
    response = await client.linked_transactions.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_id="00000000-0000-0000-0000-000000000000",
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        page=1,
        source_transaction_id="00000000-0000-0000-0000-000000000000",
        status="APPROVED",
        target_transaction_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.LinkedTransactions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

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
    response = client.linked_transactions.delete(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /LinkedTransactions/{LinkedTransactionID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.linked_transactions.delete(
        linked_transaction_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None
