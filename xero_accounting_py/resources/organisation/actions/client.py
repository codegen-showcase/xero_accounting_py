import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from xero_accounting_py.types import models


class ActionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Actions:
        """
        Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

        GET /Organisation/Actions

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Actions array with all key actions

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.organisation.actions.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Organisation/Actions",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Actions,
            request_options=request_options or default_request_options(),
        )


class AsyncActionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Actions:
        """
        Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

        GET /Organisation/Actions

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Actions array with all key actions

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.organisation.actions.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Organisation/Actions",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Actions,
            request_options=request_options or default_request_options(),
        )
