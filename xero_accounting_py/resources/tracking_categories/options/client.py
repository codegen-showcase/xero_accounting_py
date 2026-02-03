import typing
import typing_extensions

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models, params


class OptionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        tracking_category_id: str,
        tracking_option_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingOptions:
        """
        Deletes a specific option for a specific tracking category

        DELETE /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            tracking_option_id: Unique identifier for a Tracking Option
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of remaining options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.options.delete(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            tracking_option_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="DELETE",
            path=f"/TrackingCategories/{tracking_category_id}/Options/{tracking_option_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        tracking_category_id_path: str,
        tracking_option_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.TrackingOptions:
        """
        Updates a specific option for a specific tracking category

        POST /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}

        Args:
            name: The name of the tracking option e.g. Marketing, East (max length = 100)
            status: The status of a tracking option
            tracking_category_id: Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
            tracking_category_id_path: Unique identifier for a TrackingCategory
            tracking_option_id_path: Unique identifier for a Tracking Option
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.options.update(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            tracking_option_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingOption,
        )
        return self._base_client.request(
            method="POST",
            path=f"/TrackingCategories/{tracking_category_id_path}/Options/{tracking_option_id_path}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        tracking_category_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.TrackingOptions:
        """
        Creates options for a specific tracking category

        PUT /TrackingCategories/{TrackingCategoryID}/Options

        Args:
            name: The name of the tracking option e.g. Marketing, East (max length = 100)
            status: The status of a tracking option
            tracking_category_id: Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
            tracking_category_id_path: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tracking_categories.options.create(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingOption,
        )
        return self._base_client.request(
            method="PUT",
            path=f"/TrackingCategories/{tracking_category_id_path}/Options",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )


class AsyncOptionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        tracking_category_id: str,
        tracking_option_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TrackingOptions:
        """
        Deletes a specific option for a specific tracking category

        DELETE /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}

        Args:
            tracking_category_id: Unique identifier for a TrackingCategory
            tracking_option_id: Unique identifier for a Tracking Option
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of remaining options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.options.delete(
            tracking_category_id="00000000-0000-0000-0000-000000000000",
            tracking_option_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="DELETE",
            path=f"/TrackingCategories/{tracking_category_id}/Options/{tracking_option_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        tracking_category_id_path: str,
        tracking_option_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.TrackingOptions:
        """
        Updates a specific option for a specific tracking category

        POST /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID}

        Args:
            name: The name of the tracking option e.g. Marketing, East (max length = 100)
            status: The status of a tracking option
            tracking_category_id: Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
            tracking_category_id_path: Unique identifier for a TrackingCategory
            tracking_option_id_path: Unique identifier for a Tracking Option
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.options.update(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            tracking_option_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingOption,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/TrackingCategories/{tracking_category_id_path}/Options/{tracking_option_id_path}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        tracking_category_id_path: str,
        xero_tenant_id: str,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.TrackingOptions:
        """
        Creates options for a specific tracking category

        PUT /TrackingCategories/{TrackingCategoryID}/Options

        Args:
            name: The name of the tracking option e.g. Marketing, East (max length = 100)
            status: The status of a tracking option
            tracking_category_id: Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            tracking_option_id: The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
            tracking_category_id_path: Unique identifier for a TrackingCategory
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TrackingOptions array of options for a specified category

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tracking_categories.options.create(
            tracking_category_id_path="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "name": name,
                "status": status,
                "tracking_category_id": tracking_category_id,
                "tracking_option_id": tracking_option_id,
            },
            dump_with=params._SerializerTrackingOption,
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/TrackingCategories/{tracking_category_id_path}/Options",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TrackingOptions,
            request_options=request_options or default_request_options(),
        )
