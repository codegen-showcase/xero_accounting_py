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
from xero_accounting_py.resources.receipts.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.receipts.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class ReceiptsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Retrieves draft expense claim receipts for any user

        GET /Receipts

        Args:
            order: Order by an any element
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for all Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.receipts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="ReceiptNumber ASC",
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
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
            path="/Receipts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        receipt_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Retrieves a specific draft expense claim receipt by using a unique receipt Id

        GET /Receipts/{ReceiptID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            receipt_id: Unique identifier for a Receipt
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for a specified Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.receipts.get(
            receipt_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Receipts/{receipt_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        receipt_id: str,
        xero_tenant_id: str,
        receipts: typing.Union[
            typing.Optional[typing.List[params.Receipt]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Updates a specific draft expense claim receipts

        POST /Receipts/{ReceiptID}

        Args:
            receipts: typing.List[Receipt]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            receipt_id: Unique identifier for a Receipt
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for updated Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.receipts.update(
            receipt_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            receipts=[
                {
                    "reference": "Foobar",
                    "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerReceipts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"receipts": receipts}, dump_with=params._SerializerReceipts
        )
        return self._base_client.request(
            method="POST",
            path=f"/Receipts/{receipt_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        receipts: typing.Union[
            typing.Optional[typing.List[params.Receipt]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Creates draft expense claim receipts for any user

        PUT /Receipts

        Args:
            receipts: typing.List[Receipt]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for newly created Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.receipts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            receipts=[
                {
                    "line_amount_types": "NoTax",
                    "status": "DRAFT",
                    "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerReceipts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"receipts": receipts}, dump_with=params._SerializerReceipts
        )
        return self._base_client.request(
            method="PUT",
            path="/Receipts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )


class AsyncReceiptsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Retrieves draft expense claim receipts for any user

        GET /Receipts

        Args:
            order: Order by an any element
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for all Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.receipts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="ReceiptNumber ASC",
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
                style="form",
                explode=True,
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
            path="/Receipts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        receipt_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Retrieves a specific draft expense claim receipt by using a unique receipt Id

        GET /Receipts/{ReceiptID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            receipt_id: Unique identifier for a Receipt
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for a specified Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.receipts.get(
            receipt_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Receipts/{receipt_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        receipt_id: str,
        xero_tenant_id: str,
        receipts: typing.Union[
            typing.Optional[typing.List[params.Receipt]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Updates a specific draft expense claim receipts

        POST /Receipts/{ReceiptID}

        Args:
            receipts: typing.List[Receipt]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            receipt_id: Unique identifier for a Receipt
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for updated Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.receipts.update(
            receipt_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            receipts=[
                {
                    "reference": "Foobar",
                    "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerReceipts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"receipts": receipts}, dump_with=params._SerializerReceipts
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Receipts/{receipt_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        receipts: typing.Union[
            typing.Optional[typing.List[params.Receipt]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Receipts:
        """
        Creates draft expense claim receipts for any user

        PUT /Receipts

        Args:
            receipts: typing.List[Receipt]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Receipts array for newly created Receipt

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.receipts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            receipts=[
                {
                    "line_amount_types": "NoTax",
                    "status": "DRAFT",
                    "user": {"user_id": "00000000-0000-0000-0000-000000000000"},
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerReceipts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Receipts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(unitdp, type_utils.NotGiven):
            encode_query_param(
                _query,
                "unitdp",
                to_encodable(item=unitdp, dump_with=int),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"receipts": receipts}, dump_with=params._SerializerReceipts
        )
        return await self._base_client.request(
            method="PUT",
            path="/Receipts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Receipts,
            request_options=request_options or default_request_options(),
        )
