import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /TrackingCategories/{TrackingCategoryID}/Options endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TrackingOptions

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
    response = client.tracking_categories.options.create(
        tracking_category_id_path="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        name="string",
        status="ACTIVE",
        tracking_category_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        tracking_option_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /TrackingCategories/{TrackingCategoryID}/Options endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TrackingOptions

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
    response = await client.tracking_categories.options.create(
        tracking_category_id_path="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        name="string",
        status="ACTIVE",
        tracking_category_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        tracking_option_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TrackingOptions

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
    response = client.tracking_categories.options.update(
        tracking_category_id_path="00000000-0000-0000-0000-000000000000",
        tracking_option_id_path="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        name="string",
        status="ACTIVE",
        tracking_category_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        tracking_option_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TrackingOptions

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
    response = await client.tracking_categories.options.update(
        tracking_category_id_path="00000000-0000-0000-0000-000000000000",
        tracking_option_id_path="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        name="string",
        status="ACTIVE",
        tracking_category_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        tracking_option_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_200_success_all_params() -> None:
    """Tests a DELETE request to the /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TrackingOptions

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
    response = client.tracking_categories.options.delete(
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params() -> None:
    """Tests a DELETE request to the /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TrackingOptions

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
    response = await client.tracking_categories.options.delete(
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.TrackingOptions).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
