import typing
import typing_extensions

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
from xero_accounting_py.resources.purchase_orders.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.purchase_orders.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class PurchaseOrdersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves purchase orders

        GET /PurchaseOrders

        Args:
            date_from: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
            date_to: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
            order: Order by an any element
            page: To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned.
            page_size: Number of records to retrieve per page
            status: Filter by purchase order status
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array of all PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-12-01",
            date_to="2019-12-31",
            order="PurchaseOrderNumber ASC",
            page=1,
            page_size=100,
            status="SUBMITTED",
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "DateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "DateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
                    ],
                ),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves a specific purchase order using a unique purchase order Id

        GET /PurchaseOrders/{PurchaseOrderID}

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.get(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    def get_by_number(
        self,
        *,
        purchase_order_number: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves a specific purchase order using purchase order number

        GET /PurchaseOrders/{PurchaseOrderNumber}

        Args:
            purchase_order_number: Unique identifier for a PurchaseOrder
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.get_by_number(
            purchase_order_number="PO1234", xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_number}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Updates or creates one or more purchase orders

        POST /PurchaseOrders

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "date": "2019-03-13",
                    "line_items": [
                        {
                            "account_code": "710",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return self._base_client.request(
            method="POST",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Updates a specific purchase order

        POST /PurchaseOrders/{PurchaseOrderID}

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            warnings: Displays array of warning messages from the API
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for updated PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.update(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "attention_to": "Peter Parker",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                }
            ],
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return self._base_client.request(
            method="POST",
            path=f"/PurchaseOrders/{purchase_order_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Creates one or more purchase orders

        PUT /PurchaseOrders

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "date": "2019-03-13",
                    "line_items": [
                        {
                            "account_code": "710",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return self._base_client.request(
            method="PUT",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )


class AsyncPurchaseOrdersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves purchase orders

        GET /PurchaseOrders

        Args:
            date_from: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
            date_to: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
            order: Order by an any element
            page: To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned.
            page_size: Number of records to retrieve per page
            status: Filter by purchase order status
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array of all PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-12-01",
            date_to="2019-12-31",
            order="PurchaseOrderNumber ASC",
            page=1,
            page_size=100,
            status="SUBMITTED",
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "DateFrom",
                to_encodable(item=date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "DateTo",
                to_encodable(item=date_to, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
                    ],
                ),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves a specific purchase order using a unique purchase order Id

        GET /PurchaseOrders/{PurchaseOrderID}

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.get(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    async def get_by_number(
        self,
        *,
        purchase_order_number: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Retrieves a specific purchase order using purchase order number

        GET /PurchaseOrders/{PurchaseOrderNumber}

        Args:
            purchase_order_number: Unique identifier for a PurchaseOrder
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.get_by_number(
            purchase_order_number="PO1234", xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_number}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Updates or creates one or more purchase orders

        POST /PurchaseOrders

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "date": "2019-03-13",
                    "line_items": [
                        {
                            "account_code": "710",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return await self._base_client.request(
            method="POST",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Updates a specific purchase order

        POST /PurchaseOrders/{PurchaseOrderID}

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            warnings: Displays array of warning messages from the API
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for updated PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.update(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "attention_to": "Peter Parker",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                }
            ],
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/PurchaseOrders/{purchase_order_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_orders: typing.Union[
            typing.Optional[typing.List[params.PurchaseOrder]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PurchaseOrders:
        """
        Creates one or more purchase orders

        PUT /PurchaseOrders

        Args:
            pagination: Pagination
            purchase_orders: typing.List[PurchaseOrder]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PurchaseOrder array for specified PurchaseOrder

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            purchase_orders=[
                {
                    "date": "2019-03-13",
                    "line_items": [
                        {
                            "account_code": "710",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPurchaseOrders.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.PurchaseOrders.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "pagination": pagination,
                "purchase_orders": purchase_orders,
                "warnings": warnings,
            },
            dump_with=params._SerializerPurchaseOrders,
        )
        return await self._base_client.request(
            method="PUT",
            path="/PurchaseOrders",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.PurchaseOrders,
            request_options=request_options or default_request_options(),
        )
