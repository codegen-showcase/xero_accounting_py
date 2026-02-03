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
from xero_accounting_py.resources.items.history import AsyncHistoryClient, HistoryClient
from xero_accounting_py.types import models, params


class ItemsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.history = HistoryClient(base_client=self._base_client)

    def delete(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific item

        DELETE /Items/{ItemID}

        Args:
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.delete(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.Items:
        """
        Retrieves items

        GET /Items

        Args:
            order: Order by an any element
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with all Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Code ASC",
            unitdp=4,
            where="IsSold==true",
        )
        ```
        """
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
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Retrieves a specific item using a unique item Id

        GET /Items/{ItemID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with specified Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.get(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
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
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Updates or creates one or more items

        POST /Items

        Args:
            items: typing.List[Item]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with newly created Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[
                {
                    "code": "ItemCode123",
                    "description": "Item Description ABC",
                    "name": "ItemName XYZ",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return self._base_client.request(
            method="POST",
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Updates a specific item

        POST /Items/{ItemID}

        Args:
            items: typing.List[Item]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with updated Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.update(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[{"code": "ItemCode123", "description": "Description 123"}],
            unitdp=4,
        )
        ```
        """
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
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return self._base_client.request(
            method="POST",
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Creates one or more items

        PUT /Items

        Args:
            items: typing.List[Item]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with newly created Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.items.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[
                {
                    "code": "code123",
                    "description": "Foobar",
                    "inventory_asset_account_code": "140",
                    "name": "Item Name XYZ",
                    "purchase_details": {"cogs_account_code": "500"},
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return self._base_client.request(
            method="PUT",
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )


class AsyncItemsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific item

        DELETE /Items/{ItemID}

        Args:
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.delete(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.Items:
        """
        Retrieves items

        GET /Items

        Args:
            order: Order by an any element
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with all Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Code ASC",
            unitdp=4,
            where="IsSold==true",
        )
        ```
        """
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
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Retrieves a specific item using a unique item Id

        GET /Items/{ItemID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with specified Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.get(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
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
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Updates or creates one or more items

        POST /Items

        Args:
            items: typing.List[Item]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with newly created Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[
                {
                    "code": "ItemCode123",
                    "description": "Item Description ABC",
                    "name": "ItemName XYZ",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return await self._base_client.request(
            method="POST",
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        item_id: str,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Updates a specific item

        POST /Items/{ItemID}

        Args:
            items: typing.List[Item]
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            item_id: Unique identifier for an Item
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with updated Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.update(
            item_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[{"code": "ItemCode123", "description": "Description 123"}],
            unitdp=4,
        )
        ```
        """
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
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return await self._base_client.request(
            method="POST",
            path=f"/Items/{item_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        items: typing.Union[
            typing.Optional[typing.List[params.Item]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Items:
        """
        Creates one or more items

        PUT /Items

        Args:
            items: typing.List[Item]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Items array with newly created Item

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.items.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            items=[
                {
                    "code": "code123",
                    "description": "Foobar",
                    "inventory_asset_account_code": "140",
                    "name": "Item Name XYZ",
                    "purchase_details": {"cogs_account_code": "500"},
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(item={"items": items}, dump_with=params._SerializerItems)
        return await self._base_client.request(
            method="PUT",
            path="/Items",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Items,
            request_options=request_options or default_request_options(),
        )
