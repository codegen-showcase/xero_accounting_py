import pytest

from xero_accounting_py import AsyncClient, Client
from xero_accounting_py.environment import Environment


def test_send_204_success_all_params() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID}/Email endpoint.

    Operation: send
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
    response = client.invoices.email.send(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        status="string",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_send_204_success_all_params() -> None:
    """Tests a POST request to the /Invoices/{InvoiceID}/Email endpoint.

    Operation: send
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
    response = await client.invoices.email.send(
        invoice_id="00000000-0000-0000-0000-000000000000",
        xero_tenant_id="YOUR_XERO_TENANT_ID",
        status="string",
    )
    assert response is None
