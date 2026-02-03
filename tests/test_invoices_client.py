import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.update(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.get(
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.get(
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.get(
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.get(
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        created_by_my_app=False,
        i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        include_archived=True,
        invoice_numbers=["&quot;INV-001&quot;, &quot;INV-002&quot;"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["&quot;DRAFT&quot;, &quot;SUBMITTED&quot;"],
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        created_by_my_app=False,
        i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        include_archived=True,
        invoice_numbers=["&quot;INV-001&quot;, &quot;INV-002&quot;"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["&quot;DRAFT&quot;, &quot;SUBMITTED&quot;"],
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
    client = Client(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = client.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        created_by_my_app=False,
        i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        include_archived=True,
        invoice_numbers=["&quot;INV-001&quot;, &quot;INV-002&quot;"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["&quot;DRAFT&quot;, &quot;SUBMITTED&quot;"],
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
    client = AsyncClient(
        oauth={
            "client_id": "OAUTH_CLIENT_ID",
            "client_secret": "OAUTH_CLIENT_SECRET",
            "token_url": "https://api.sideko.dev/v1/mock_oauth_token/public/xero-accounting/0.1.0/OAuth2",
        },
        environment=Environment.MOCK_SERVER,
    )
    response = await client.invoices.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        contact_i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        created_by_my_app=False,
        i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
        include_archived=True,
        invoice_numbers=["&quot;INV-001&quot;, &quot;INV-002&quot;"],
        order="InvoiceNumber ASC",
        page=1,
        page_size=100,
        search_term="SearchTerm=REF12",
        statuses=["&quot;DRAFT&quot;, &quot;SUBMITTED&quot;"],
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
