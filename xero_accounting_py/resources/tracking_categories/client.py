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
from xero_accounting_py.resources.tracking_categories.options import (
    AsyncOptionsClient,
    OptionsClient,
)
from xero_accounting_py.types import models, params


class TrackingCategoriesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.options = OptionsClient(base_client=self._base_client)

    def delete(
        self,
        *,
        tracking_category_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Deletes a specific tracking category

        DELETE /TrackingCategories/{TrackingCategoryID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of deleted TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.delete(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="DELETE",
            path=f"/TrackingCategories/{tracking_category_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        xero_tenant_id: str,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Retrieves tracking categories and options

        GET /TrackingCategories

        Args:
            include_archived: e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            include_archived=True,
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "includeArchived",
                to_encodable(item=include_archived, dump_with=bool),
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
            path="/TrackingCategories",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        tracking_category_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Retrieves specific tracking categories and options using a unique tracking category Id

        GET /TrackingCategories/{TrackingCategoryID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of specified TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.get(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/TrackingCategories/{tracking_category_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        tracking_category_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        option: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        options: typing.Union[
            typing.Optional[typing.List[params.TrackingOption]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Updates a specific tracking category

        POST /TrackingCategories/{TrackingCategoryID}

        Args:
            name: The name of the tracking category e.g. Department, Region (max length = 100)
            option: The option name of the tracking option e.g. East, West (max length = 100)
            options: See Tracking Options
            status: The status of a tracking category
            tracking_category_id: The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
            tracking_category_id_path: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of updated TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.update(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            name="Avengers",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "option": option,
                "options": options,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingCategory,
        )
        return self._base_client.request(
            method="POST",
            path=f"/TrackingCategories/{tracking_category_id_path}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        option: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        options: typing.Union[
            typing.Optional[typing.List[params.TrackingOption]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Create tracking categories

        PUT /TrackingCategories

        Args:
            name: The name of the tracking category e.g. Department, Region (max length = 100)
            option: The option name of the tracking option e.g. East, West (max length = 100)
            options: See Tracking Options
            status: The status of a tracking category
            tracking_category_id: The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of newly created TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.create(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "option": option,
                "options": options,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingCategory,
        )
        return self._base_client.request(
            method="PUT",
            path="/TrackingCategories",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )


class AsyncTrackingCategoriesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.options = AsyncOptionsClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        tracking_category_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Deletes a specific tracking category

        DELETE /TrackingCategories/{TrackingCategoryID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of deleted TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.delete(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="DELETE",
            path=f"/TrackingCategories/{tracking_category_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        xero_tenant_id: str,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Retrieves tracking categories and options

        GET /TrackingCategories

        Args:
            include_archived: e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            include_archived=True,
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "includeArchived",
                to_encodable(item=include_archived, dump_with=bool),
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
            path="/TrackingCategories",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        tracking_category_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Retrieves specific tracking categories and options using a unique tracking category Id

        GET /TrackingCategories/{TrackingCategoryID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of specified TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.get(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/TrackingCategories/{tracking_category_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        tracking_category_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        option: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        options: typing.Union[
            typing.Optional[typing.List[params.TrackingOption]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Updates a specific tracking category

        POST /TrackingCategories/{TrackingCategoryID}

        Args:
            name: The name of the tracking category e.g. Department, Region (max length = 100)
            option: The option name of the tracking option e.g. East, West (max length = 100)
            options: See Tracking Options
            status: The status of a tracking category
            tracking_category_id: The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
            tracking_category_id_path: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of updated TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.update(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            name="Avengers",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "option": option,
                "options": options,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingCategory,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/TrackingCategories/{tracking_category_id_path}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        option: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        options: typing.Union[
            typing.Optional[typing.List[params.TrackingOption]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tracking_category_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tracking_option_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingCategories:
        """
        Create tracking categories

        PUT /TrackingCategories

        Args:
            name: The name of the tracking category e.g. Department, Region (max length = 100)
            option: The option name of the tracking option e.g. East, West (max length = 100)
            options: See Tracking Options
            status: The status of a tracking category
            tracking_category_id: The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingCategories array of newly created TrackingCategory

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.create(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "option": option,
                "options": options,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingCategory,
        )
        return await self._base_client.request(
            method="PUT",
            path="/TrackingCategories",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingCategories,
            request_options=request_options or default_request_options(),
        )
