import pydantic
import pytest

from make_api_request import BinaryResponse
from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_by_filename_200_success_all_params() -> None:
    """Tests a PUT request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: create_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Attachments

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
    response = client.contacts.attachments.create_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        data="string",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_by_filename_200_success_all_params() -> None:
    """Tests a PUT request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: create_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Attachments

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
    response = await client.contacts.attachments.create_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        data="string",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_by_filename_200_success_all_params() -> None:
    """Tests a POST request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: update_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Attachments

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
    response = client.contacts.attachments.update_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        data="string",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_by_filename_200_success_all_params() -> None:
    """Tests a POST request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: update_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Attachments

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
    response = await client.contacts.attachments.update_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        data="string",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_by_filename_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: get_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

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
    response = client.contacts.attachments.get_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        content_type="image/jpg",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_by_filename_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments/{FileName} endpoint.

    Operation: get_by_filename
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

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
    response = await client.contacts.attachments.get_by_filename(
        contact_id="00000000-0000-0000-0000-000000000000",
        content_type="image/jpg",
        file_name="xero-dev.jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_get_by_id_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments/{AttachmentID} endpoint.

    Operation: get_by_id
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

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
    response = client.contacts.attachments.get_by_id(
        attachment_id="00000000-0000-0000-0000-000000000000",
        contact_id="00000000-0000-0000-0000-000000000000",
        content_type="image/jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_by_id_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments/{AttachmentID} endpoint.

    Operation: get_by_id
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

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
    response = await client.contacts.attachments.get_by_id(
        attachment_id="00000000-0000-0000-0000-000000000000",
        contact_id="00000000-0000-0000-0000-000000000000",
        content_type="image/jpg",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Attachments

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
    response = client.contacts.attachments.list(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Contacts/{ContactID}/Attachments endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Attachments

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
    response = await client.contacts.attachments.list(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Attachments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
