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


class ProjectsUsersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProjectUsers:
        """
        Retrieves a list of all project users

        Allows you to retrieve the users on a projects.

        GET /ProjectsUsers

        Args:
            page: set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of project users

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects_users.list(
            xero_tenant_id="string", page=1, page_size=100
        )
        ```
        """
        _query: QueryParams = {}
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
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/ProjectsUsers",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ProjectUsers,
            request_options=request_options or default_request_options(),
        )


class AsyncProjectsUsersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProjectUsers:
        """
        Retrieves a list of all project users

        Allows you to retrieve the users on a projects.

        GET /ProjectsUsers

        Args:
            page: set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of project users

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects_users.list(
            xero_tenant_id="string", page=1, page_size=100
        )
        ```
        """
        _query: QueryParams = {}
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
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/ProjectsUsers",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ProjectUsers,
            request_options=request_options or default_request_options(),
        )
