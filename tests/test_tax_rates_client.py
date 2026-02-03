import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /TaxRates endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxRates

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
    response = client.tax_rates.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        tax_rates=[
            {
                "can_apply_to_assets": True,
                "can_apply_to_equity": True,
                "can_apply_to_expenses": True,
                "can_apply_to_liabilities": True,
                "can_apply_to_revenue": True,
                "display_tax_rate": 123.45,
                "effective_rate": 123.45,
                "name": "string",
                "report_tax_type": "ACC28PLUS",
                "status": "ACTIVE",
                "tax_components": [
                    {
                        "is_compound": True,
                        "is_non_recoverable": True,
                        "name": "string",
                        "rate": 123.45,
                    }
                ],
                "tax_type": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /TaxRates endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxRates

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
    response = await client.tax_rates.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        tax_rates=[
            {
                "can_apply_to_assets": True,
                "can_apply_to_equity": True,
                "can_apply_to_expenses": True,
                "can_apply_to_liabilities": True,
                "can_apply_to_revenue": True,
                "display_tax_rate": 123.45,
                "effective_rate": 123.45,
                "name": "string",
                "report_tax_type": "ACC28PLUS",
                "status": "ACTIVE",
                "tax_components": [
                    {
                        "is_compound": True,
                        "is_non_recoverable": True,
                        "name": "string",
                        "rate": 123.45,
                    }
                ],
                "tax_type": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /TaxRates endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxRates

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
    response = client.tax_rates.update(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        tax_rates=[
            {
                "can_apply_to_assets": True,
                "can_apply_to_equity": True,
                "can_apply_to_expenses": True,
                "can_apply_to_liabilities": True,
                "can_apply_to_revenue": True,
                "display_tax_rate": 123.45,
                "effective_rate": 123.45,
                "name": "string",
                "report_tax_type": "ACC28PLUS",
                "status": "ACTIVE",
                "tax_components": [
                    {
                        "is_compound": True,
                        "is_non_recoverable": True,
                        "name": "string",
                        "rate": 123.45,
                    }
                ],
                "tax_type": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /TaxRates endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxRates

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
    response = await client.tax_rates.update(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        tax_rates=[
            {
                "can_apply_to_assets": True,
                "can_apply_to_equity": True,
                "can_apply_to_expenses": True,
                "can_apply_to_liabilities": True,
                "can_apply_to_revenue": True,
                "display_tax_rate": 123.45,
                "effective_rate": 123.45,
                "name": "string",
                "report_tax_type": "ACC28PLUS",
                "status": "ACTIVE",
                "tax_components": [
                    {
                        "is_compound": True,
                        "is_non_recoverable": True,
                        "name": "string",
                        "rate": 123.45,
                    }
                ],
                "tax_type": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /TaxRates/{TaxType} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxRates

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
    response = client.tax_rates.get(
        tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID"
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /TaxRates/{TaxType} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxRates

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
    response = await client.tax_rates.get(
        tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID"
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /TaxRates endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxRates

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
    response = client.tax_rates.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /TaxRates endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxRates

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
    response = await client.tax_rates.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /TaxRates endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.TaxRates

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
    response = client.tax_rates.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /TaxRates endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.TaxRates

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
    response = await client.tax_rates.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID", order="Name ASC", where='Status=="ACTIVE"'
    )
    try:
        pydantic.TypeAdapter(models.TaxRates).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
