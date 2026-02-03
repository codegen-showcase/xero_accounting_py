import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from xero_accounting_py.types import models


class OnlineInvoiceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OnlineInvoices:
        """
        Retrieves a URL to an online invoice

        GET /Invoices/{InvoiceID}/OnlineInvoice

        Args:
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type OnlineInvoice array with one OnlineInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.online_invoice.get(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/OnlineInvoice",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.OnlineInvoices,
            request_options=request_options or default_request_options(),
        )


class AsyncOnlineInvoiceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.OnlineInvoices:
        """
        Retrieves a URL to an online invoice

        GET /Invoices/{InvoiceID}/OnlineInvoice

        Args:
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type OnlineInvoice array with one OnlineInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.online_invoice.get(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/OnlineInvoice",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.OnlineInvoices,
            request_options=request_options or default_request_options(),
        )
