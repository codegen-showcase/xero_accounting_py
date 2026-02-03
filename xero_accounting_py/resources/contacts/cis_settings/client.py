import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from xero_accounting_py.types import models


class CisSettingsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CisSettings:
        """
        Retrieves CIS settings for a specific contact in a Xero organisation

        GET /Contacts/{ContactID}/CISSettings

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type CISSettings for a specific Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.cis_settings.list(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}/CISSettings",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.CisSettings,
            request_options=request_options or default_request_options(),
        )


class AsyncCisSettingsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CisSettings:
        """
        Retrieves CIS settings for a specific contact in a Xero organisation

        GET /Contacts/{ContactID}/CISSettings

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type CISSettings for a specific Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.cis_settings.list(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}/CISSettings",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.CisSettings,
            request_options=request_options or default_request_options(),
        )
