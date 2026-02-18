import typing

from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models


class JournalsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        offset: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Journals:
        """
        Retrieves journals

        GET /Journals

        Args:
            offset: Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned
            payments_only: Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Journals array with all Journals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.journals.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID", offset=10, payments_only=True
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Journals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Journals,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        journal_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Journals:
        """
        Retrieves a specific journal using a unique journal Id.

        GET /Journals/{JournalID}

        Args:
            journal_id: Unique identifier for a Journal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Journals array with specified Journal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.journals.get(
            journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Journals/{journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Journals,
            request_options=request_options or default_request_options(),
        )


class AsyncJournalsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        offset: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Journals:
        """
        Retrieves journals

        GET /Journals

        Args:
            offset: Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned
            payments_only: Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Journals array with all Journals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.journals.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID", offset=10, payments_only=True
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(payments_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "paymentsOnly",
                to_encodable(item=payments_only, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Journals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Journals,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        journal_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Journals:
        """
        Retrieves a specific journal using a unique journal Id.

        GET /Journals/{JournalID}

        Args:
            journal_id: Unique identifier for a Journal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Journals array with specified Journal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.journals.get(
            journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Journals/{journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Journals,
            request_options=request_options or default_request_options(),
        )
