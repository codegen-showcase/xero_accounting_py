import pydantic
import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment
from xero_accounting_py.types import models


def test_create_200_success_required_only() -> None:
    """Tests a PUT request to the /ManualJournals endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_required_only() -> None:
    """Tests a PUT request to the /ManualJournals endpoint.

    Operation: create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_200_success_all_params() -> None:
    """Tests a PUT request to the /ManualJournals endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params() -> None:
    """Tests a PUT request to the /ManualJournals endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_200_success_all_params() -> None:
    """Tests a POST request to the /ManualJournals/{ManualJournalID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.update(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params() -> None:
    """Tests a POST request to the /ManualJournals/{ManualJournalID} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.update(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
        pagination={
            "item_count": 123,
            "page": 123,
            "page_count": 123,
            "page_size": 123,
        },
        warnings=[{"message": "string"}],
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /ManualJournals endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_required_only() -> None:
    """Tests a POST request to the /ManualJournals endpoint.

    Operation: update_or_create
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /ManualJournals endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_or_create_200_success_all_params() -> None:
    """Tests a POST request to the /ManualJournals endpoint.

    Operation: update_or_create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.update_or_create(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        manual_journals=[
            {
                "attachments": [
                    {
                        "attachment_id": "00000000-0000-0000-0000-000000000000",
                        "content_length": 123,
                        "file_name": "xero-dev.jpg",
                        "include_online": True,
                        "mime_type": "image/jpg",
                        "url": "https://api.xero.com/api.xro/2.0/Accounts/da962997-a8bd-4dff-9616-01cdc199283f/Attachments/sample5.jpg",
                    }
                ],
                "date": "string",
                "has_attachments": True,
                "journal_lines": [
                    {
                        "account_code": "string",
                        "account_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                        "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                        "is_blank": False,
                        "line_amount": -2569.0,
                        "tax_amount": 0.0,
                        "tax_type": "string",
                        "tracking": [
                            {
                                "name": "string",
                                "option": "string",
                                "options": [
                                    {
                                        "name": "string",
                                        "status": "ACTIVE",
                                        "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                        "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                    }
                                ],
                                "status": "ACTIVE",
                                "tracking_category_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                                "tracking_option_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                            }
                        ],
                    }
                ],
                "line_amount_types": "Exclusive",
                "manual_journal_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "narration": "string",
                "show_on_cash_basis_reports": True,
                "status": "ARCHIVED",
                "status_attribute_string": "ERROR",
                "updated_date_utc": "/Date(1573755038314)/",
                "url": "string",
                "validation_errors": [{"message": "string"}],
                "warnings": [{"message": "string"}],
            }
        ],
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
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals/{ManualJournalID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.get(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals/{ManualJournalID} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.get(
        manual_journal_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only() -> None:
    """Tests a GET request to the /ManualJournals endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Date ASC",
        page=1,
        page_size=100,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only() -> None:
    """Tests a GET request to the /ManualJournals endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Date ASC",
        page=1,
        page_size=100,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ManualJournals

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
    response = client.manual_journals.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Date ASC",
        page=1,
        page_size=100,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params() -> None:
    """Tests a GET request to the /ManualJournals endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ManualJournals

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
    response = await client.manual_journals.list(
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        order="Date ASC",
        page=1,
        page_size=100,
        where='Status=="DRAFT"',
    )
    try:
        pydantic.TypeAdapter(models.ManualJournals).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
