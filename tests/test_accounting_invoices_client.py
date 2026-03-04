import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import SIDEKO_MOCK_SERVER
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Invoices endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Invoices endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Invoices endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Invoices endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_required_only() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID} endpoint.

    Operation: update
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_required_only() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID} endpoint.

    Operation: update
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Invoices endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Invoices endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Invoices endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Invoices endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={"item_count": 2, "page": 1, "page_count": 1, "page_size": 10},
        summarize_errors=True,
        unitdp=4,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_required_only() -> None:
    """Tests a GET request to the /Invoices/{InvoiceID} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.get(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_required_only() -> None:
    """Tests a GET request to the /Invoices/{InvoiceID} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.get(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Invoices/{InvoiceID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.get(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Invoices/{InvoiceID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.get(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Invoices endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        created_by_my_app=False,
        include_archived=True,
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        summary_only=True,
        unitdp=4,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Invoices endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        created_by_my_app=False,
        include_archived=True,
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        summary_only=True,
        unitdp=4,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Invoices endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.accounting.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        created_by_my_app=False,
        i_ds=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        include_archived=True,
        invoice_numbers=["string"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["string"],
        summary_only=True,
        unitdp=4,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Invoices endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Invoices

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.accounting.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        created_by_my_app=False,
        i_ds=["3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"],
        include_archived=True,
        invoice_numbers=["string"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["string"],
        summary_only=True,
        unitdp=4,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.Invoices).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
