import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Items endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /Items endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Items endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /Items endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_required_only() -> None:
    """Tests a POST request to the /Items/{ItemID} endpoint.

    Operation: update
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.update(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_required_only() -> None:
    """Tests a POST request to the /Items/{ItemID} endpoint.

    Operation: update
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.update(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /Items/{ItemID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.update(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /Items/{ItemID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.update(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Items endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /Items endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Items endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /Items endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        items=[
            {
                "code": "string",
                "description": "string",
                "inventory_asset_account_code": "string",
                "is_purchased": True,
                "is_sold": True,
                "is_tracked_as_inventory": True,
                "item_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "name": "string",
                "purchase_description": "string",
                "purchase_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "quantity_on_hand": 123.45,
                "sales_details": {
                    "account_code": "string",
                    "cogs_account_code": "string",
                    "tax_type": "string",
                    "unit_price": 123.45,
                },
                "status_attribute_string": "string",
                "total_cost_pool": 123.45,
                "updated_date_utc": "/Date(1573755038314)/",
                "validation_errors": [{"message": "string"}],
            }
        ],
        summarize_errors=True,
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_required_only() -> None:
    """Tests a GET request to the /Items/{ItemID} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.get(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_required_only() -> None:
    """Tests a GET request to the /Items/{ItemID} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.get(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Items/{ItemID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.get(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Items/{ItemID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.get(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        unitdp=4,
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /Items endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Code ASC",
        unitdp=4,
        where="IsSold==true",
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /Items endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Code ASC",
        unitdp=4,
        where="IsSold==true",
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Items endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Code ASC",
        unitdp=4,
        where="IsSold==true",
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Items endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Items

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Code ASC",
        unitdp=4,
        where="IsSold==true",
    )
    try:
        pydantic.TypeAdapter(models.Items).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Items/{ItemID} endpoint.

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
    client = Client(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.items.delete(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params() -> None:
    """Tests a DELETE request to the /Items/{ItemID} endpoint.

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
    client = AsyncClient(oauth_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.items.delete(
        item_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    assert response is None
