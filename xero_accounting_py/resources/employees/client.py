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


class EmployeesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Retrieves employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        GET /Employees

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with all Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.employees.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="LastName ASC",
            where='Status=="ACTIVE"',
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
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        employee_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Retrieves a specific employee used in Xero payrun using a unique employee Id

        This endpoint is deprecated and will be removed April 28, 2026

        GET /Employees/{EmployeeID}

        Args:
            employee_id: Unique identifier for a Employee
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with specified Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.employees.get(
            employee_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Employees/{employee_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        employees: typing.Union[
            typing.Optional[typing.List[params.Employee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Creates a single new employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        POST /Employees

        Args:
            employees: typing.List[Employee]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with new Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.employees.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            employees=[
                {
                    "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
                    "first_name": "Nick",
                    "last_name": "Fury",
                }
            ],
            summarize_errors=True,
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"employees": employees}, dump_with=params._SerializerEmployees
        )
        return self._base_client.request(
            method="POST",
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        employees: typing.Union[
            typing.Optional[typing.List[params.Employee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Creates new employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        PUT /Employees

        Args:
            employees: typing.List[Employee]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with new Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.employees.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            employees=[
                {
                    "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
                    "first_name": "Nick",
                    "last_name": "Fury",
                }
            ],
            summarize_errors=True,
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"employees": employees}, dump_with=params._SerializerEmployees
        )
        return self._base_client.request(
            method="PUT",
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )


class AsyncEmployeesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Retrieves employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        GET /Employees

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with all Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.employees.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="LastName ASC",
            where='Status=="ACTIVE"',
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
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        employee_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Retrieves a specific employee used in Xero payrun using a unique employee Id

        This endpoint is deprecated and will be removed April 28, 2026

        GET /Employees/{EmployeeID}

        Args:
            employee_id: Unique identifier for a Employee
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with specified Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.employees.get(
            employee_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Employees/{employee_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        employees: typing.Union[
            typing.Optional[typing.List[params.Employee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Creates a single new employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        POST /Employees

        Args:
            employees: typing.List[Employee]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with new Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.employees.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            employees=[
                {
                    "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
                    "first_name": "Nick",
                    "last_name": "Fury",
                }
            ],
            summarize_errors=True,
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"employees": employees}, dump_with=params._SerializerEmployees
        )
        return await self._base_client.request(
            method="POST",
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        employees: typing.Union[
            typing.Optional[typing.List[params.Employee]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Employees:
        """
        Creates new employees used in Xero payrun

        This endpoint is deprecated and will be removed April 28, 2026

        PUT /Employees

        Args:
            employees: typing.List[Employee]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Employees array with new Employee

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.employees.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            employees=[
                {
                    "external_link": {"url": "http://twitter.com/#!/search/Nick+Fury"},
                    "first_name": "Nick",
                    "last_name": "Fury",
                }
            ],
            summarize_errors=True,
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"employees": employees}, dump_with=params._SerializerEmployees
        )
        return await self._base_client.request(
            method="PUT",
            path="/Employees",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Employees,
            request_options=request_options or default_request_options(),
        )
