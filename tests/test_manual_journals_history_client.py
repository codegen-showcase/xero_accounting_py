import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_record_200_success_all_params() -> None:
    """Tests a PUT request to the /ManualJournals/{ManualJournalID}/History endpoint.

    Operation: create_record
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.HistoryRecords

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
    response = client.manual_journals.history.create_record(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        history_records=[
            {
                "changes": "string",
                "date_utc": "/Date(1573755038314)/",
                "details": "string",
                "user": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.HistoryRecords).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_record_200_success_all_params() -> None:
    """Tests a PUT request to the /ManualJournals/{ManualJournalID}/History endpoint.

    Operation: create_record
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.HistoryRecords

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
    response = await client.manual_journals.history.create_record(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        history_records=[
            {
                "changes": "string",
                "date_utc": "/Date(1573755038314)/",
                "details": "string",
                "user": "string",
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.HistoryRecords).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals/{ManualJournalID}/History endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.HistoryRecords

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
    response = client.manual_journals.history.list(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.HistoryRecords).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals/{ManualJournalID}/History endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.HistoryRecords

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
    response = await client.manual_journals.history.list(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.HistoryRecords).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
