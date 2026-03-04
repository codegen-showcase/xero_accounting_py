import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import SIDEKO_MOCK_SERVER
from xero_accounting_py.types import models


def test_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

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
    response = client.projects.projects1.tasks.update(
        charge_type="FIXED",
        name="string",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        rate={"currency": "AUD", "value": 1.0},
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        estimate_minutes=123,
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

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
    response = await client.projects.projects1.tasks.update(
        charge_type="FIXED",
        name="string",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        rate={"currency": "AUD", "value": 1.0},
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        estimate_minutes=123,
    )
    assert response is None


def test_create_201_success_all_params() -> None:
    """Tests a POST request to the /Projects/{projectId}/Tasks endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Task

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.projects1.tasks.create(
        charge_type="FIXED",
        name="string",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        rate={"currency": "AUD", "value": 1.0},
        xero_tenant_id="string",
        estimate_minutes=123,
    )
    try:
        pydantic.TypeAdapter(models.Task).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params() -> None:
    """Tests a POST request to the /Projects/{projectId}/Tasks endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Task

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.projects1.tasks.create(
        charge_type="FIXED",
        name="string",
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        rate={"currency": "AUD", "value": 1.0},
        xero_tenant_id="string",
        estimate_minutes=123,
    )
    try:
        pydantic.TypeAdapter(models.Task).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Task

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.projects1.tasks.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    try:
        pydantic.TypeAdapter(models.Task).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Task

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.projects1.tasks.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    try:
        pydantic.TypeAdapter(models.Task).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Tasks

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.projects1.tasks.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        page=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(models.Tasks).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Tasks

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.projects1.tasks.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        page=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(models.Tasks).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Tasks

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.projects1.tasks.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        charge_type="FIXED",
        page=1,
        page_size=10,
        task_ids="string",
    )
    try:
        pydantic.TypeAdapter(models.Tasks).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Tasks endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Tasks

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.projects1.tasks.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        charge_type="FIXED",
        page=1,
        page_size=10,
        task_ids="string",
    )
    try:
        pydantic.TypeAdapter(models.Tasks).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

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
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.projects1.tasks.delete(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Projects/{projectId}/Tasks/{taskId} endpoint.

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
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.projects1.tasks.delete(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    assert response is None
