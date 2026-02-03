import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import params


class EmailClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def send(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends a copy of a specific invoice to related contact via email

        POST /Invoices/{InvoiceID}/Email

        Args:
            status: Need at least one field to create an empty JSON payload
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.email.send(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerRequestEmpty
        )
        self._base_client.request(
            method="POST",
            path=f"/Invoices/{invoice_id}/Email",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncEmailClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def send(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends a copy of a specific invoice to related contact via email

        POST /Invoices/{InvoiceID}/Email

        Args:
            status: Need at least one field to create an empty JSON payload
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.email.send(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerRequestEmpty
        )
        await self._base_client.request(
            method="POST",
            path=f"/Invoices/{invoice_id}/Email",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
