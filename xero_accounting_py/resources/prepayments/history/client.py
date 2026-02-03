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
        prepayment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Retrieves history record for a specific prepayment

        GET /Prepayments/{PrepaymentID}/History

        Args:
            prepayment_id: Unique identifier for a PrePayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of HistoryRecords array of 0 to N HistoryRecord

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.prepayments.history.list(
            prepayment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Prepayments/{prepayment_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )

    def create_record(
        self,
        *,
        prepayment_id: str,
        xero_tenant_id: str,
        history_records: typing.Union[
            typing.Optional[typing.List[params.HistoryRecord]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Creates a history record for a specific prepayment

        PUT /Prepayments/{PrepaymentID}/History

        Args:
            history_records: typing.List[HistoryRecord]
            prepayment_id: Unique identifier for a PrePayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type HistoryRecords array of HistoryRecord objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.prepayments.history.create_record(
            prepayment_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Prepayments/{prepayment_id}/History",
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
        prepayment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Retrieves history record for a specific prepayment

        GET /Prepayments/{PrepaymentID}/History

        Args:
            prepayment_id: Unique identifier for a PrePayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of HistoryRecords array of 0 to N HistoryRecord

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.prepayments.history.list(
            prepayment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Prepayments/{prepayment_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )

    async def create_record(
        self,
        *,
        prepayment_id: str,
        xero_tenant_id: str,
        history_records: typing.Union[
            typing.Optional[typing.List[params.HistoryRecord]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.HistoryRecords:
        """
        Creates a history record for a specific prepayment

        PUT /Prepayments/{PrepaymentID}/History

        Args:
            history_records: typing.List[HistoryRecord]
            prepayment_id: Unique identifier for a PrePayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type HistoryRecords array of HistoryRecord objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.prepayments.history.create_record(
            prepayment_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Prepayments/{prepayment_id}/History",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.HistoryRecords,
            request_options=request_options or default_request_options(),
        )
