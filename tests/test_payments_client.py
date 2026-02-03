import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Payments endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        summarize_errors=True,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Payments endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        summarize_errors=True,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Payments endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        summarize_errors=True,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Payments endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        summarize_errors=True,
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_200_success_all_params() -> None:
    """Tests a POST request to the /Payments/{PaymentID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.delete(
        payment_id="00000000-0000-0000-0000-000000000000",
        status="string",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params() -> None:
    """Tests a POST request to the /Payments/{PaymentID} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.delete(
        payment_id="00000000-0000-0000-0000-000000000000",
        status="string",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_1_200_success_all_params() -> None:
    """Tests a POST request to the /Payments endpoint.

    Operation: create_1
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.create_1(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        account={
            "account_id": "00000000-0000-0000-0000-000000000000",
            "add_to_watchlist": True,
            "bank_account_number": "string",
            "bank_account_type": "BANK",
            "class_": "ASSET",
            "code": "string",
            "currency_code": "AED",
            "description": "string",
            "enable_payments_to_account": True,
            "has_attachments": True,
            "name": "Food Sales",
            "reporting_code": "string",
            "reporting_code_name": "string",
            "show_in_expense_claims": True,
            "status": "ACTIVE",
            "system_account": "BANKCURRENCYGAIN",
            "tax_type": "string",
            "type_": "BANK",
            "updated_date_utc": "/Date(1573755038314)/",
            "validation_errors": [{"message": "string"}],
        },
        amount=123.45,
        bank_account_number="string",
        bank_amount=123.45,
        batch_payment_id="00000000-0000-0000-0000-000000000000",
        code="string",
        credit_note_number="string",
        currency_rate=123.45,
        date="string",
        details="string",
        has_account=True,
        has_validation_errors=True,
        invoice_number="string",
        is_reconciled=True,
        particulars="string",
        payment_id="00000000-0000-0000-0000-000000000000",
        payment_type="ACCPAYPAYMENT",
        reference="string",
        status="AUTHORISED",
        status_attribute_string="string",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_1_200_success_all_params() -> None:
    """Tests a POST request to the /Payments endpoint.

    Operation: create_1
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.create_1(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        account={
            "account_id": "00000000-0000-0000-0000-000000000000",
            "add_to_watchlist": True,
            "bank_account_number": "string",
            "bank_account_type": "BANK",
            "class_": "ASSET",
            "code": "string",
            "currency_code": "AED",
            "description": "string",
            "enable_payments_to_account": True,
            "has_attachments": True,
            "name": "Food Sales",
            "reporting_code": "string",
            "reporting_code_name": "string",
            "show_in_expense_claims": True,
            "status": "ACTIVE",
            "system_account": "BANKCURRENCYGAIN",
            "tax_type": "string",
            "type_": "BANK",
            "updated_date_utc": "/Date(1573755038314)/",
            "validation_errors": [{"message": "string"}],
        },
        amount=123.45,
        bank_account_number="string",
        bank_amount=123.45,
        batch_payment_id="00000000-0000-0000-0000-000000000000",
        code="string",
        credit_note_number="string",
        currency_rate=123.45,
        date="string",
        details="string",
        has_account=True,
        has_validation_errors=True,
        invoice_number="string",
        is_reconciled=True,
        particulars="string",
        payment_id="00000000-0000-0000-0000-000000000000",
        payment_type="ACCPAYPAYMENT",
        reference="string",
        status="AUTHORISED",
        status_attribute_string="string",
        updated_date_utc="/Date(1573755038314)/",
        validation_errors=[{"message": "string"}],
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Payments/{PaymentID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.get(
        payment_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Payments/{PaymentID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.get(
        payment_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Payments endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        page=1,
        page_size=100,
        where='Status=="AUTHORISED"',
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Payments endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        page=1,
        page_size=100,
        where='Status=="AUTHORISED"',
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Payments endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Payments

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
    response = client.payments.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        page=1,
        page_size=100,
        where='Status=="AUTHORISED"',
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Payments endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Payments

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
    response = await client.payments.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Amount ASC",
        page=1,
        page_size=100,
        where='Status=="AUTHORISED"',
    )
    try:
        pydantic.TypeAdapter(models.Payments).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
