import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models, params


class HistoryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Retrieves history records for a specific contact

        GET /Contacts/{ContactID}/History

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of HistoryRecords array of 0 to N HistoryRecord

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.history.list(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        history_records: typing.Union[
            typing.Optional[typing.List[params.HistoryRecord]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Creates a new history record for a specific contact

        PUT /Contacts/{ContactID}/History

        Args:
            history_records: typing.List[HistoryRecord]
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type HistoryRecords array of HistoryRecord objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.history.create(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            history_records=[{"details": "Hello World"}],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"history_records": history_records},
            dump_with=params._SerializerHistoryRecords,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/Contacts/{contact_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )


class AsyncHistoryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Retrieves history records for a specific contact

        GET /Contacts/{ContactID}/History

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of HistoryRecords array of 0 to N HistoryRecord

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.history.list(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        history_records: typing.Union[
            typing.Optional[typing.List[params.HistoryRecord]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Creates a new history record for a specific contact

        PUT /Contacts/{ContactID}/History

        Args:
            history_records: typing.List[HistoryRecord]
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type HistoryRecords array of HistoryRecord objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.history.create(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            history_records=[{"details": "Hello World"}],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"history_records": history_records},
            dump_with=params._SerializerHistoryRecords,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/Contacts/{contact_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )
