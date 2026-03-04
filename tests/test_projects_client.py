import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import SIDEKO_MOCK_SERVER
from xero_accounting_py.types import models


def test_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId} endpoint.

    Operation: update
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
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.update(
        name="New Kitchen",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        contact_id="01234567-89ab-cdef-0123-456789abcdef",
        deadline_utc="2019-12-10T12:59:59Z",
        estimate_amount=1.0,
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId} endpoint.

    Operation: update
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
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.update(
        name="New Kitchen",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        contact_id="01234567-89ab-cdef-0123-456789abcdef",
        deadline_utc="2019-12-10T12:59:59Z",
        estimate_amount=1.0,
    )
    assert response is None


def test_create_201_success_all_params() -> None:
    """Tests a POST request to the /Projects endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Project

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.create(
        name="New Kitchen",
        xero_tenant_id="string",
        contact_id="01234567-89ab-cdef-0123-456789abcdef",
        deadline_utc="2019-12-10T12:59:59Z",
        estimate_amount=1.0,
    )
    try:
        pydantic.TypeAdapter(models.Project).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params() -> None:
    """Tests a POST request to the /Projects endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Project

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.create(
        name="New Kitchen",
        xero_tenant_id="string",
        contact_id="01234567-89ab-cdef-0123-456789abcdef",
        deadline_utc="2019-12-10T12:59:59Z",
        estimate_amount=1.0,
    )
    try:
        pydantic.TypeAdapter(models.Project).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_patch_204_success_all_params() -> None:
    """Tests a PATCH request to the /Projects/{projectId} endpoint.

    Operation: patch
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
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.patch(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="INPROGRESS",
        xero_tenant_id="string",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_patch_204_success_all_params() -> None:
    """Tests a PATCH request to the /Projects/{projectId} endpoint.

    Operation: patch
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
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.patch(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        status="INPROGRESS",
        xero_tenant_id="string",
    )
    assert response is None


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Project

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
    )
    try:
        pydantic.TypeAdapter(models.Project).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Project

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
    )
    try:
        pydantic.TypeAdapter(models.Project).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Projects

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.list(xero_tenant_id="string", page=1, page_size=100)
    try:
        pydantic.TypeAdapter(models.Projects).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Projects

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.list(
        xero_tenant_id="string", page=1, page_size=100
    )
    try:
        pydantic.TypeAdapter(models.Projects).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Projects

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.list(
        xero_tenant_id="string",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        page=1,
        page_size=100,
        project_ids=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        states="string",
    )
    try:
        pydantic.TypeAdapter(models.Projects).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Projects

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.list(
        xero_tenant_id="string",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        page=1,
        page_size=100,
        project_ids=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        states="string",
    )
    try:
        pydantic.TypeAdapter(models.Projects).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
