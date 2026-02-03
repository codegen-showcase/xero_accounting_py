import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /ContactGroups/{ContactGroupID}/Contacts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Contacts

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
    response = client.contact_groups.contacts.create(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Contacts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /ContactGroups/{ContactGroupID}/Contacts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Contacts

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
    response = await client.contact_groups.contacts.create(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Contacts).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /ContactGroups/{ContactGroupID}/Contacts/{ContactID} endpoint.

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
    response = client.contact_groups.contacts.delete(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /ContactGroups/{ContactGroupID}/Contacts/{ContactID} endpoint.

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
    response = await client.contact_groups.contacts.delete(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None


def test_delete_all_204_success_all_params() -> None:
    """Tests a DELETE request to the /ContactGroups/{ContactGroupID}/Contacts endpoint.

    Operation: delete_all
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
    response = client.contact_groups.contacts.delete_all(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_all_204_success_all_params() -> None:
    """Tests a DELETE request to the /ContactGroups/{ContactGroupID}/Contacts endpoint.

    Operation: delete_all
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
    response = await client.contact_groups.contacts.delete_all(
        contact_group_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None
