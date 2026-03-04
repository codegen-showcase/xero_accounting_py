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
from xero_accounting_py.types import models, params


class TimeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        project_id: str,
        time_entry_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a time entry for a specific project

        Allows you to delete a specific time entry

        DELETE /Projects/{projectId}/Time/{timeEntryId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            time_entry_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.time.delete(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
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
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_after_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_before_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_chargeable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        states: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        task_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntries:
        """
        Retrieves all time entries associated with a specific project

        Allows you to retrieve the time entries associated with a specific project

        GET /Projects/{projectId}/Time

        Args:
            contact_id: Finds all time entries for this contact identifier.
            date_after_utc: ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field.
            date_before_utc: ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field.
            invoice_id: Finds all time entries for this invoice.
            is_chargeable: Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`.
            page: Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            states: Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified.
            task_id: Identifier of the task that time entry is logged against.
            user_id: The xero user identifier of the person who logged time.
            project_id: Identifier of the project, that the task (which the time entry is logged against) belongs to.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of time entry objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.time.list(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            page=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contactId",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_after_utc, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateAfterUtc",
                to_encodable(item=date_after_utc, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_before_utc, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateBeforeUtc",
                to_encodable(item=date_before_utc, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(invoice_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invoiceId",
                to_encodable(item=invoice_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(is_chargeable, type_utils.NotGiven):
            encode_query_param(
                _query,
                "isChargeable",
                to_encodable(item=is_chargeable, dump_with=bool),
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
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(task_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "taskId",
                to_encodable(item=task_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(user_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "userId",
                to_encodable(item=user_id, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Time",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TimeEntries,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        project_id: str,
        time_entry_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntry:
        """
        Retrieves a single time entry for a specific project

        Allows you to get a single time entry in a project

        GET /Projects/{projectId}/Time/{timeEntryId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            time_entry_id: You can specify an individual time entry by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified time entry

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.time.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TimeEntry,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        date_utc: str,
        duration: int,
        project_id: str,
        task_id: str,
        user_id: str,
        xero_tenant_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntry:
        """
        Creates a time entry for a specific project

        Allows you to create a specific task

        POST /Projects/{projectId}/Time

        Args:
            description: An optional description of the time entry, will be set to null if not provided during update.
            date_utc: Date time entry is logged on. UTC Date Time in ISO-8601 format.
            duration: Number of minutes to be logged. Duration is between 1 and 59940 inclusively.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: Identifier of the task that time entry is logged against.
            user_id: The xero user identifier of the person logging the time.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the newly created time entry

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.time.create(
            date_utc="2020-02-26T15:00:00Z",
            duration=30,
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="00000000-0000-0000-0000-000000000000",
            user_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="string",
            description="My description",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "description": description,
                "date_utc": date_utc,
                "duration": duration,
                "task_id": task_id,
                "user_id": user_id,
            },
            dump_with=params._SerializerTimeEntryCreateOrUpdate,
        )
        return self._base_client.request(
            method="POST",
            path=f"/Projects/{project_id}/Time",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TimeEntry,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        date_utc: str,
        duration: int,
        project_id: str,
        task_id: str,
        time_entry_id: str,
        user_id: str,
        xero_tenant_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a time entry for a specific project

        Allows you to update time entry in a project

        PUT /Projects/{projectId}/Time/{timeEntryId}

        Args:
            description: An optional description of the time entry, will be set to null if not provided during update.
            date_utc: Date time entry is logged on. UTC Date Time in ISO-8601 format.
            duration: Number of minutes to be logged. Duration is between 1 and 59940 inclusively.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: Identifier of the task that time entry is logged against.
            time_entry_id: You can specify an individual time entry by appending the id to the endpoint
            user_id: The xero user identifier of the person logging the time.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.projects.time.update(
            date_utc="2020-02-27T15:00:00Z",
            duration=45,
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="00000000-0000-0000-0000-000000000000",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            user_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="string",
            description="My UPDATED description",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "description": description,
                "date_utc": date_utc,
                "duration": duration,
                "task_id": task_id,
                "user_id": user_id,
            },
            dump_with=params._SerializerTimeEntryCreateOrUpdate,
        )
        self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )


class AsyncTimeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        project_id: str,
        time_entry_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a time entry for a specific project

        Allows you to delete a specific time entry

        DELETE /Projects/{projectId}/Time/{timeEntryId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            time_entry_id: You can specify an individual task by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.time.delete(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
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
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_after_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_before_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_chargeable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        states: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        task_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        user_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntries:
        """
        Retrieves all time entries associated with a specific project

        Allows you to retrieve the time entries associated with a specific project

        GET /Projects/{projectId}/Time

        Args:
            contact_id: Finds all time entries for this contact identifier.
            date_after_utc: ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field.
            date_before_utc: ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field.
            invoice_id: Finds all time entries for this invoice.
            is_chargeable: Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`.
            page: Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
            page_size: Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
            states: Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified.
            task_id: Identifier of the task that time entry is logged against.
            user_id: The xero user identifier of the person who logged time.
            project_id: Identifier of the project, that the task (which the time entry is logged against) belongs to.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns a list of time entry objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.time.list(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
            page=1,
            page_size=10,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contactId",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_after_utc, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateAfterUtc",
                to_encodable(item=date_after_utc, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(date_before_utc, type_utils.NotGiven):
            encode_query_param(
                _query,
                "dateBeforeUtc",
                to_encodable(item=date_before_utc, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(invoice_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "invoiceId",
                to_encodable(item=invoice_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(is_chargeable, type_utils.NotGiven):
            encode_query_param(
                _query,
                "isChargeable",
                to_encodable(item=is_chargeable, dump_with=bool),
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
        if not isinstance(states, type_utils.NotGiven):
            encode_query_param(
                _query,
                "states",
                to_encodable(item=states, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        if not isinstance(task_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "taskId",
                to_encodable(item=task_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(user_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "userId",
                to_encodable(item=user_id, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Time",
            service_name="projects",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TimeEntries,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        project_id: str,
        time_entry_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntry:
        """
        Retrieves a single time entry for a specific project

        Allows you to get a single time entry in a project

        GET /Projects/{projectId}/Time/{timeEntryId}

        Args:
            project_id: You can specify an individual project by appending the projectId to the endpoint
            time_entry_id: You can specify an individual time entry by appending the id to the endpoint
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the specified time entry

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.time.get(
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            xero_tenant_id="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TimeEntry,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        date_utc: str,
        duration: int,
        project_id: str,
        task_id: str,
        user_id: str,
        xero_tenant_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TimeEntry:
        """
        Creates a time entry for a specific project

        Allows you to create a specific task

        POST /Projects/{projectId}/Time

        Args:
            description: An optional description of the time entry, will be set to null if not provided during update.
            date_utc: Date time entry is logged on. UTC Date Time in ISO-8601 format.
            duration: Number of minutes to be logged. Duration is between 1 and 59940 inclusively.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: Identifier of the task that time entry is logged against.
            user_id: The xero user identifier of the person logging the time.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            OK/success, returns the newly created time entry

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.time.create(
            date_utc="2020-02-26T15:00:00Z",
            duration=30,
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="00000000-0000-0000-0000-000000000000",
            user_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="string",
            description="My description",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "description": description,
                "date_utc": date_utc,
                "duration": duration,
                "task_id": task_id,
                "user_id": user_id,
            },
            dump_with=params._SerializerTimeEntryCreateOrUpdate,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Projects/{project_id}/Time",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TimeEntry,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        date_utc: str,
        duration: int,
        project_id: str,
        task_id: str,
        time_entry_id: str,
        user_id: str,
        xero_tenant_id: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a time entry for a specific project

        Allows you to update time entry in a project

        PUT /Projects/{projectId}/Time/{timeEntryId}

        Args:
            description: An optional description of the time entry, will be set to null if not provided during update.
            date_utc: Date time entry is logged on. UTC Date Time in ISO-8601 format.
            duration: Number of minutes to be logged. Duration is between 1 and 59940 inclusively.
            project_id: You can specify an individual project by appending the projectId to the endpoint
            task_id: Identifier of the task that time entry is logged against.
            time_entry_id: You can specify an individual time entry by appending the id to the endpoint
            user_id: The xero user identifier of the person logging the time.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.projects.time.update(
            date_utc="2020-02-27T15:00:00Z",
            duration=45,
            project_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            task_id="00000000-0000-0000-0000-000000000000",
            time_entry_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            user_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="string",
            description="My UPDATED description",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Xero-Tenant-Id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "description": description,
                "date_utc": date_utc,
                "duration": duration,
                "task_id": task_id,
                "user_id": user_id,
            },
            dump_with=params._SerializerTimeEntryCreateOrUpdate,
        )
        await self._base_client.request(
            method="PUT",
            path=f"/Projects/{project_id}/Time/{time_entry_id}",
            service_name="projects",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
