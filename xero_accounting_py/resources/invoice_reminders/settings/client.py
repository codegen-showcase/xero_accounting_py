import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from xero_accounting_py.types import models


class SettingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceReminders:
        """
        Retrieves invoice reminder settings

        GET /InvoiceReminders/Settings

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Invoice Reminders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoice_reminders.settings.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/InvoiceReminders/Settings",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.InvoiceReminders,
            request_options=request_options or default_request_options(),
        )


class AsyncSettingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvoiceReminders:
        """
        Retrieves invoice reminder settings

        GET /InvoiceReminders/Settings

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Invoice Reminders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoice_reminders.settings.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/InvoiceReminders/Settings",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.InvoiceReminders,
            request_options=request_options or default_request_options(),
        )
