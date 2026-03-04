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
from xero_accounting_py.resources.projects.projects1.tasks import (
    AsyncTasksClient,
    TasksClient,
)
from xero_accounting_py.resources.projects.projects1.time import (
    AsyncTimeClient,
    TimeClient,
)
from xero_accounting_py.types import models, params


class Projects1Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.tasks = TasksClient(base_client=self._base_client)
        self.time = TimeClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        project_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        states: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Projects:
        """
        Retrieves all projects

        Allows you to retrieve, create and update projects.

        GET /Projects

        Args:
            contact_id: Filter for projects for a specific contact
            page: set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            project_ids: Search for all projects that match a comma separated list of projectIds
            states: Filter for projects in a particular state (INPROGRESS or CLOSED)
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of project objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.list(xero_tenant_id="string", page=1, page_size=100)
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contactID",
                to_encodable(item=contact_id, dump_with=str),
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
        if not isinstance(project_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "projectIds",
                to_encodable(item=project_ids, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Projects",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Projects,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        project_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Project:
        """
        Retrieves a single project

        Allows you to retrieve a specific project using the projectId

        GET /Projects/{projectId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified project object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Project,
            request_options=request_options or default_request_options(),
        )

    def patch(
        self,
        *,
        project_id: str,
        status: typing_extensions.Literal["CLOSED", "INPROGRESS"],
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        creates a project for the specified contact

        Allows you to update a specific projects.

        PATCH /Projects/{projectId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            status: Status for project
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.patch(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="INPROGRESS",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerProjectPatch
        )
        self._base_client.request(
            method="PATCH",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deadline_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimate_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Project:
        """
        Create one or more new projects

        POST /Projects

        Args:
            contact_id: Identifier of the contact this project was created for.
            deadline_utc: Deadline for the project. UTC Date Time in ISO-8601 format.
            estimate_amount: float
            name: Name of the project.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the new project object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.create(
            name="New Kitchen",
            xero_tenant_id="string",
            contact_id="00000000-0000-0000-000-000000000000",
            deadline_utc="2019-12-10T12:59:59Z",
            estimate_amount=99.99,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "deadline_utc": deadline_utc,
                "estimate_amount": estimate_amount,
                "name": name,
            },
            dump_with=params._SerializerProjectCreateOrUpdate,
        )
        return self._base_client.request(
            method="POST",
            path="/Projects",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Project,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        name: str,
        project_id: str,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deadline_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimate_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a specific project

        Allows you to update a specific projects.

        PUT /Projects/{projectId}

        Args:
            contact_id: Identifier of the contact this project was created for.
            deadline_utc: Deadline for the project. UTC Date Time in ISO-8601 format.
            estimate_amount: float
            name: Name of the project.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.update(
            name="New Kitchen",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            contact_id="01234567-89ab-cdef-0123-456789abcdef",
            deadline_utc="2017-04-23T18:25:43.511Z",
            estimate_amount=99.99,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "deadline_utc": deadline_utc,
                "estimate_amount": estimate_amount,
                "name": name,
            },
            dump_with=params._SerializerProjectCreateOrUpdate,
        )
        self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncProjects1Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.tasks = AsyncTasksClient(base_client=self._base_client)
        self.time = AsyncTimeClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        project_ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        states: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Projects:
        """
        Retrieves all projects

        Allows you to retrieve, create and update projects.

        GET /Projects

        Args:
            contact_id: Filter for projects for a specific contact
            page: set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            project_ids: Search for all projects that match a comma separated list of projectIds
            states: Filter for projects in a particular state (INPROGRESS or CLOSED)
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of project objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.list(
            xero_tenant_id="string", page=1, page_size=100
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contactID",
                to_encodable(item=contact_id, dump_with=str),
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
        if not isinstance(project_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "projectIds",
                to_encodable(item=project_ids, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Projects",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Projects,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        project_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Project:
        """
        Retrieves a single project

        Allows you to retrieve a specific project using the projectId

        GET /Projects/{projectId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified project object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", xero_tenant_id="string"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Project,
            request_options=request_options or default_request_options(),
        )

    async def patch(
        self,
        *,
        project_id: str,
        status: typing_extensions.Literal["CLOSED", "INPROGRESS"],
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        creates a project for the specified contact

        Allows you to update a specific projects.

        PATCH /Projects/{projectId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            status: Status for project
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.patch(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            status="INPROGRESS",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerProjectPatch
        )
        await self._base_client.request(
            method="PATCH",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deadline_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimate_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Project:
        """
        Create one or more new projects

        POST /Projects

        Args:
            contact_id: Identifier of the contact this project was created for.
            deadline_utc: Deadline for the project. UTC Date Time in ISO-8601 format.
            estimate_amount: float
            name: Name of the project.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the new project object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.create(
            name="New Kitchen",
            xero_tenant_id="string",
            contact_id="00000000-0000-0000-000-000000000000",
            deadline_utc="2019-12-10T12:59:59Z",
            estimate_amount=99.99,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "deadline_utc": deadline_utc,
                "estimate_amount": estimate_amount,
                "name": name,
            },
            dump_with=params._SerializerProjectCreateOrUpdate,
        )
        return await self._base_client.request(
            method="POST",
            path="/Projects",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Project,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        name: str,
        project_id: str,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deadline_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimate_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a specific project

        Allows you to update a specific projects.

        PUT /Projects/{projectId}

        Args:
            contact_id: Identifier of the contact this project was created for.
            deadline_utc: Deadline for the project. UTC Date Time in ISO-8601 format.
            estimate_amount: float
            name: Name of the project.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.update(
            name="New Kitchen",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            contact_id="01234567-89ab-cdef-0123-456789abcdef",
            deadline_utc="2017-04-23T18:25:43.511Z",
            estimate_amount=99.99,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "deadline_utc": deadline_utc,
                "estimate_amount": estimate_amount,
                "name": name,
            },
            dump_with=params._SerializerProjectCreateOrUpdate,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
