import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/{ReportID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get(
        report_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/{ReportID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get(
        report_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_trial_balance_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/TrialBalance endpoint.

    Operation: get_trial_balance
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_trial_balance(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_trial_balance_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/TrialBalance endpoint.

    Operation: get_trial_balance
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_trial_balance(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_trial_balance_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/TrialBalance endpoint.

    Operation: get_trial_balance
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_trial_balance(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_trial_balance_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/TrialBalance endpoint.

    Operation: get_trial_balance
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_trial_balance(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-10-31", payments_only=True
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_ten_ninety_nine_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/TenNinetyNine endpoint.

    Operation: get_ten_ninety_nine
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Reports

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
    response = client.reports.get_ten_ninety_nine(
        xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
    )
    try:
        pydantic.TypeAdapter(models.Reports).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_ten_ninety_nine_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/TenNinetyNine endpoint.

    Operation: get_ten_ninety_nine
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Reports

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
    response = await client.reports.get_ten_ninety_nine(
        xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
    )
    try:
        pydantic.TypeAdapter(models.Reports).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_ten_ninety_nine_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/TenNinetyNine endpoint.

    Operation: get_ten_ninety_nine
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Reports

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
    response = client.reports.get_ten_ninety_nine(
        xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
    )
    try:
        pydantic.TypeAdapter(models.Reports).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_ten_ninety_nine_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/TenNinetyNine endpoint.

    Operation: get_ten_ninety_nine
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Reports

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
    response = await client.reports.get_ten_ninety_nine(
        xero_tenant_id="YOUR_XERO_TENANT_ID", report_year="2019"
    )
    try:
        pydantic.TypeAdapter(models.Reports).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_profit_and_loss_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/ProfitAndLoss endpoint.

    Operation: get_profit_and_loss
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_profit_and_loss(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        payments_only=True,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        to_date="2019-10-31",
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_category_id2="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_profit_and_loss_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/ProfitAndLoss endpoint.

    Operation: get_profit_and_loss
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_profit_and_loss(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        payments_only=True,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        to_date="2019-10-31",
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_category_id2="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_profit_and_loss_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/ProfitAndLoss endpoint.

    Operation: get_profit_and_loss
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_profit_and_loss(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        payments_only=True,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        to_date="2019-10-31",
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_category_id2="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_profit_and_loss_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/ProfitAndLoss endpoint.

    Operation: get_profit_and_loss
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_profit_and_loss(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        payments_only=True,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        to_date="2019-10-31",
        tracking_category_id="00000000-0000-0000-0000-000000000000",
        tracking_category_id2="00000000-0000-0000-0000-000000000000",
        tracking_option_id="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_executive_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/ExecutiveSummary endpoint.

    Operation: get_executive_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_executive_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_executive_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/ExecutiveSummary endpoint.

    Operation: get_executive_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_executive_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_executive_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/ExecutiveSummary endpoint.

    Operation: get_executive_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_executive_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_executive_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/ExecutiveSummary endpoint.

    Operation: get_executive_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_executive_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31"
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_budget_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BudgetSummary endpoint.

    Operation: get_budget_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_budget_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_budget_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BudgetSummary endpoint.

    Operation: get_budget_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_budget_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_budget_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BudgetSummary endpoint.

    Operation: get_budget_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_budget_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_budget_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BudgetSummary endpoint.

    Operation: get_budget_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_budget_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID", date="2019-03-31", periods=2, timeframe=3
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_bank_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BankSummary endpoint.

    Operation: get_bank_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_bank_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_bank_summary_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BankSummary endpoint.

    Operation: get_bank_summary
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_bank_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_bank_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BankSummary endpoint.

    Operation: get_bank_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_bank_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_bank_summary_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BankSummary endpoint.

    Operation: get_bank_summary
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_bank_summary(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_balance_sheet_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BalanceSheet endpoint.

    Operation: get_balance_sheet
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_balance_sheet(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-11-01",
        payments_only=False,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        tracking_option_id1="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_balance_sheet_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/BalanceSheet endpoint.

    Operation: get_balance_sheet
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_balance_sheet(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-11-01",
        payments_only=False,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        tracking_option_id1="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_balance_sheet_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BalanceSheet endpoint.

    Operation: get_balance_sheet
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_balance_sheet(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-11-01",
        payments_only=False,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        tracking_option_id1="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_balance_sheet_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/BalanceSheet endpoint.

    Operation: get_balance_sheet
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_balance_sheet(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-11-01",
        payments_only=False,
        periods=3,
        standard_layout=True,
        timeframe="MONTH",
        tracking_option_id1="00000000-0000-0000-0000-000000000000",
        tracking_option_id2="00000000-0000-0000-0000-000000000000",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_aged_receivables_by_contact_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/AgedReceivablesByContact endpoint.

    Operation: get_aged_receivables_by_contact
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_aged_receivables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_aged_receivables_by_contact_200_success_required_only() -> (
    None
):
    """Tests a GET request to the /Reports/AgedReceivablesByContact endpoint.

    Operation: get_aged_receivables_by_contact
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_aged_receivables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_aged_receivables_by_contact_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/AgedReceivablesByContact endpoint.

    Operation: get_aged_receivables_by_contact
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_aged_receivables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_aged_receivables_by_contact_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/AgedReceivablesByContact endpoint.

    Operation: get_aged_receivables_by_contact
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_aged_receivables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_aged_payables_by_contact_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/AgedPayablesByContact endpoint.

    Operation: get_aged_payables_by_contact
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_aged_payables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_aged_payables_by_contact_200_success_required_only() -> None:
    """Tests a GET request to the /Reports/AgedPayablesByContact endpoint.

    Operation: get_aged_payables_by_contact
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_aged_payables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_aged_payables_by_contact_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/AgedPayablesByContact endpoint.

    Operation: get_aged_payables_by_contact
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.get_aged_payables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_aged_payables_by_contact_200_success_all_params() -> None:
    """Tests a GET request to the /Reports/AgedPayablesByContact endpoint.

    Operation: get_aged_payables_by_contact
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.get_aged_payables_by_contact(
        contact_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        date="2019-10-31",
        from_date="2019-10-31",
        to_date="2019-10-31",
    )
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /Reports endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ReportWithRows

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
    response = client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /Reports endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ReportWithRows

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
    response = await client.reports.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
    try:
        pydantic.TypeAdapter(models.ReportWithRows).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
