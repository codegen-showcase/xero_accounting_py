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


class BudgetsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
        i_ds: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Budgets:
        """
        Retrieve a list of budgets

        GET /Budgets

        Args:
            date_from: Filter by end date
            date_to: Filter by start date
            i_ds: Filter by BudgetID. Allows you to retrieve a specific individual budget.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Budgets array with 0 to N Budgets

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.budgets.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-10-31",
            date_to="2019-10-31",
            i_ds="&quot;00000000-0000-0000-0000-000000000000&quot;",
        )
        ```
        """
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
        if not isinstance(i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IDs",
                to_encodable(item=i_ds, dump_with=str),
                style="form",
                explode=False,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Budgets",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Budgets,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        budget_id: str,
        xero_tenant_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Budgets:
        """
        Retrieves a specific budget, which includes budget lines

        GET /Budgets/{BudgetID}

        Args:
            date_from: Filter by end date
            date_to: Filter by start date
            budget_id: Unique identifier for Budgets
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.budgets.get(
            budget_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-10-31",
            date_to="2019-10-31",
        )
        ```
        """
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Budgets/{budget_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Budgets,
            request_options=request_options or default_request_options(),
        )


class AsyncBudgetsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
        i_ds: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Budgets:
        """
        Retrieve a list of budgets

        GET /Budgets

        Args:
            date_from: Filter by end date
            date_to: Filter by start date
            i_ds: Filter by BudgetID. Allows you to retrieve a specific individual budget.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Budgets array with 0 to N Budgets

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.budgets.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-10-31",
            date_to="2019-10-31",
            i_ds="&quot;00000000-0000-0000-0000-000000000000&quot;",
        )
        ```
        """
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
        if not isinstance(i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IDs",
                to_encodable(item=i_ds, dump_with=str),
                style="form",
                explode=False,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Budgets",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Budgets,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        budget_id: str,
        xero_tenant_id: str,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Budgets:
        """
        Retrieves a specific budget, which includes budget lines

        GET /Budgets/{BudgetID}

        Args:
            date_from: Filter by end date
            date_to: Filter by start date
            budget_id: Unique identifier for Budgets
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.budgets.get(
            budget_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            date_from="2019-10-31",
            date_to="2019-10-31",
        )
        ```
        """
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
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Budgets/{budget_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Budgets,
            request_options=request_options or default_request_options(),
        )
