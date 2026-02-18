import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Employees endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Employees endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Employees endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Employees endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Employees endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Employees endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Employees endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Employees endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        employees=[
            {
                "employee_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "external_link": {
                    "description": "string",
                    "link_type": "Facebook",
                    "url": "string",
                },
                "first_name": "string",
                "last_name": "string",
                "status": "ACTIVE",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Employees/{EmployeeID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.get(
        employee_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Employees/{EmployeeID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.get(
        employee_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Employees endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="LastName ASC",
        where='Status=="ACTIVE"',
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Employees endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="LastName ASC",
        where='Status=="ACTIVE"',
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Employees endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.employees.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="LastName ASC",
        where='Status=="ACTIVE"',
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Employees endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Employees

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.employees.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="LastName ASC",
        where='Status=="ACTIVE"',
    )
    try:
        pydantic.TypeAdapter(models.Employees).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
