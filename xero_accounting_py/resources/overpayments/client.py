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
from xero_accounting_py.resources.overpayments.allocations import (
    AllocationsClient,
    AsyncAllocationsClient,
)
from xero_accounting_py.resources.overpayments.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models


class OverpaymentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.allocations = AllocationsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        references: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Overpayments:
        """
        Retrieves overpayments

        GET /Overpayments

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment
            page_size: Number of records to retrieve per page
            references: Filter by a comma-separated list of References
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Overpayments array with all Overpayments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.overpayments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Status ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.Overpayments.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page_size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "pageSize",
                to_encodable(item=page_size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(references, type_utils.NotGiven):
            encode_query_param(
                _query,
                "References",
                to_encodable(item=references, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(where, type_utils.NotGiven):
            encode_query_param(
                _query,
                "where",
                to_encodable(item=where, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Overpayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Overpayments,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        overpayment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Overpayments:
        """
        Retrieves a specific overpayment using a unique overpayment Id

        GET /Overpayments/{OverpaymentID}

        Args:
            overpayment_id: Unique identifier for a Overpayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Overpayments array with specified Overpayments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.overpayments.get(
            overpayment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Overpayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Overpayments/{overpayment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Overpayments,
            request_options=request_options or default_request_options(),
        )


class AsyncOverpaymentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.allocations = AsyncAllocationsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        references: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Overpayments:
        """
        Retrieves overpayments

        GET /Overpayments

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment
            page_size: Number of records to retrieve per page
            references: Filter by a comma-separated list of References
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Overpayments array with all Overpayments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.overpayments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Status ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.Overpayments.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(page_size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "pageSize",
                to_encodable(item=page_size, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(references, type_utils.NotGiven):
            encode_query_param(
                _query,
                "References",
                to_encodable(item=references, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(where, type_utils.NotGiven):
            encode_query_param(
                _query,
                "where",
                to_encodable(item=where, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Overpayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Overpayments,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        overpayment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Overpayments:
        """
        Retrieves a specific overpayment using a unique overpayment Id

        GET /Overpayments/{OverpaymentID}

        Args:
            overpayment_id: Unique identifier for a Overpayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Overpayments array with specified Overpayments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.overpayments.get(
            overpayment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Overpayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Overpayments/{overpayment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Overpayments,
            request_options=request_options or default_request_options(),
        )
