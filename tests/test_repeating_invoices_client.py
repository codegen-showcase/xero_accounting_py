import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /RepeatingInvoices endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /RepeatingInvoices endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /RepeatingInvoices endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /RepeatingInvoices endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /RepeatingInvoices/{RepeatingInvoiceID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.update(
        repeating_invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /RepeatingInvoices/{RepeatingInvoiceID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.update(
        repeating_invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /RepeatingInvoices endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /RepeatingInvoices endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /RepeatingInvoices endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /RepeatingInvoices endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /RepeatingInvoices/{RepeatingInvoiceID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.get(
        repeating_invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /RepeatingInvoices/{RepeatingInvoiceID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.get(
        repeating_invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /RepeatingInvoices endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /RepeatingInvoices endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /RepeatingInvoices endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.repeating_invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /RepeatingInvoices endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RepeatingInvoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.repeating_invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Total ASC", where='Status=="DRAFT"'
    )
    try:
        pydantic.TypeAdapter(models.RepeatingInvoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
