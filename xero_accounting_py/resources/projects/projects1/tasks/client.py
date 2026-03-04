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
from xero_accounting_py.types import models, params


class TasksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        project_id: str,
        task_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Allows you to delete a task

        Allows you to delete a specific task

        DELETE /Projects/{projectId}/Tasks/{taskId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.tasks.delete(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        project_id: str,
        xero_tenant_id: str,
        charge_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        task_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Tasks:
        """
        Retrieves all project tasks

        Allows you to retrieve a specific project

        GET /Projects/{projectId}/Tasks

        Args:
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            page: Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            task_ids: Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID}
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of task objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.tasks.list(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            page=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(charge_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "chargeType",
                to_encodable(
                    item=charge_type,
                    dump_with=typing_extensions.Literal[
                        "FIXED", "NON_CHARGEABLE", "TIME"
                    ],
                ),
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
        if not isinstance(task_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "taskIds",
                to_encodable(item=task_ids, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Tasks",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Tasks,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        project_id: str,
        task_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Task:
        """
        Retrieves a single project task

        Allows you to retrieve a specific project

        GET /Projects/{projectId}/Tasks/{taskId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID}
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified task object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.tasks.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Task,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        charge_type: typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"],
        name: str,
        project_id: str,
        rate: params.Amount,
        xero_tenant_id: str,
        estimate_minutes: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Task:
        """
        Allows you to create a task

        Allows you to create a specific task

        POST /Projects/{projectId}/Tasks

        Args:
            estimate_minutes: An estimated time to perform the task
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            name: Name of the task. Max length 100 characters.
            project_id: You can create a task on a specified projectId
            rate: Amount
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the new task object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.tasks.create(
            charge_type="TIME",
            name="Demolition",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            rate={"currency": "AUD", "value": 20.0},
            xero_tenant_id="string",
            estimate_minutes=12000,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "estimate_minutes": estimate_minutes,
                "charge_type": charge_type,
                "name": name,
                "rate": rate,
            },
            dump_with=params._SerializerTaskCreateOrUpdate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/Projects/{project_id}/Tasks",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Task,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        charge_type: typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"],
        name: str,
        project_id: str,
        rate: params.Amount,
        task_id: str,
        xero_tenant_id: str,
        estimate_minutes: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Allows you to update a task

        Allows you to update a specific task

        PUT /Projects/{projectId}/Tasks/{taskId}

        Args:
            estimate_minutes: An estimated time to perform the task
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            name: Name of the task. Max length 100 characters.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            rate: Amount
            task_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.projects1.tasks.update(
            charge_type="TIME",
            name="Demolition",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            rate={"currency": "AUD", "value": 20.0},
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            estimate_minutes=12000,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "estimate_minutes": estimate_minutes,
                "charge_type": charge_type,
                "name": name,
                "rate": rate,
            },
            dump_with=params._SerializerTaskCreateOrUpdate,
        )
        self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncTasksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        project_id: str,
        task_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Allows you to delete a task

        Allows you to delete a specific task

        DELETE /Projects/{projectId}/Tasks/{taskId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.tasks.delete(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        project_id: str,
        xero_tenant_id: str,
        charge_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        task_ids: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Tasks:
        """
        Retrieves all project tasks

        Allows you to retrieve a specific project

        GET /Projects/{projectId}/Tasks

        Args:
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            page: Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            task_ids: Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID}
            project_id: You can specify an individual project by appending the projectId to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of task objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.tasks.list(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            page=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(charge_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "chargeType",
                to_encodable(
                    item=charge_type,
                    dump_with=typing_extensions.Literal[
                        "FIXED", "NON_CHARGEABLE", "TIME"
                    ],
                ),
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
        if not isinstance(task_ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "taskIds",
                to_encodable(item=task_ids, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Tasks",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Tasks,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        project_id: str,
        task_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Task:
        """
        Retrieves a single project task

        Allows you to retrieve a specific project

        GET /Projects/{projectId}/Tasks/{taskId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID}
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified task object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.tasks.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Task,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        charge_type: typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"],
        name: str,
        project_id: str,
        rate: params.Amount,
        xero_tenant_id: str,
        estimate_minutes: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Task:
        """
        Allows you to create a task

        Allows you to create a specific task

        POST /Projects/{projectId}/Tasks

        Args:
            estimate_minutes: An estimated time to perform the task
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            name: Name of the task. Max length 100 characters.
            project_id: You can create a task on a specified projectId
            rate: Amount
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the new task object

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.tasks.create(
            charge_type="TIME",
            name="Demolition",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            rate={"currency": "AUD", "value": 20.0},
            xero_tenant_id="string",
            estimate_minutes=12000,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "estimate_minutes": estimate_minutes,
                "charge_type": charge_type,
                "name": name,
                "rate": rate,
            },
            dump_with=params._SerializerTaskCreateOrUpdate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Projects/{project_id}/Tasks",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Task,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        charge_type: typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"],
        name: str,
        project_id: str,
        rate: params.Amount,
        task_id: str,
        xero_tenant_id: str,
        estimate_minutes: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Allows you to update a task

        Allows you to update a specific task

        PUT /Projects/{projectId}/Tasks/{taskId}

        Args:
            estimate_minutes: An estimated time to perform the task
            charge_type: Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
            name: Name of the task. Max length 100 characters.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            rate: Amount
            task_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.projects1.tasks.update(
            charge_type="TIME",
            name="Demolition",
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            rate={"currency": "AUD", "value": 20.0},
            task_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            estimate_minutes=12000,
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "estimate_minutes": estimate_minutes,
                "charge_type": charge_type,
                "name": name,
                "rate": rate,
            },
            dump_with=params._SerializerTaskCreateOrUpdate,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}/Tasks/{task_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
