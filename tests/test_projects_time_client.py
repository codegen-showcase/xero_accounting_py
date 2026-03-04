import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import SIDEKO_MOCK_SERVER
from xero_accounting_py.types import models


def test_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

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
    response = client.projects.time.update(
        date_utc="1970-01-01T00:00:00",
        duration=123,
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="00000000-0000-0000-000-000000000000",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        user_id="00000000-0000-0000-000-000000000000",
        xero_tenant_id="string",
        description="string",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_update_204_success_all_params() -> None:
    """Tests a PUT request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

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
    response = await client.projects.time.update(
        date_utc="1970-01-01T00:00:00",
        duration=123,
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="00000000-0000-0000-000-000000000000",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        user_id="00000000-0000-0000-000-000000000000",
        xero_tenant_id="string",
        description="string",
    )
    assert response is None


def test_create_200_success_all_params() -> None:
    """Tests a POST request to the /Projects/{projectId}/Time endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TimeEntry

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.time.create(
        date_utc="1970-01-01T00:00:00",
        duration=123,
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="00000000-0000-0000-000-000000000000",
        user_id="00000000-0000-0000-000-000000000000",
        xero_tenant_id="string",
        description="string",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntry).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a POST request to the /Projects/{projectId}/Time endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TimeEntry

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.time.create(
        date_utc="1970-01-01T00:00:00",
        duration=123,
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        task_id="00000000-0000-0000-000-000000000000",
        user_id="00000000-0000-0000-000-000000000000",
        xero_tenant_id="string",
        description="string",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntry).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TimeEntry

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.time.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntry).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TimeEntry

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.time.get(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntry).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TimeEntries

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.time.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        page=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(models.TimeEntries).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TimeEntries

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.time.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        page=1,
        page_size=10,
    )
    try:
        pydantic.TypeAdapter(models.TimeEntries).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TimeEntries

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.projects.time.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        date_after_utc="1970-01-01T00:00:00",
        date_before_utc="1970-01-01T00:00:00",
        invoice_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        is_chargeable=True,
        page=1,
        page_size=10,
        states=["string"],
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntries).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Projects/{projectId}/Time endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TimeEntries

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.projects.time.list(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
        contact_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        date_after_utc="1970-01-01T00:00:00",
        date_before_utc="1970-01-01T00:00:00",
        invoice_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        is_chargeable=True,
        page=1,
        page_size=10,
        states=["string"],
        task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.TimeEntries).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

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
    response = client.projects.time.delete(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Projects/{projectId}/Time/{timeEntryId} endpoint.

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
    response = await client.projects.time.delete(
        project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        xero_tenant_id="string",
    )
    assert response is None
