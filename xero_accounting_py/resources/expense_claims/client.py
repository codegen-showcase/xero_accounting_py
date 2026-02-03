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
from xero_accounting_py.resources.expense_claims.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class ExpenseClaimsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.history = HistoryClient(base_client=self._base_client)

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
    ) -> models.ExpenseClaims:
        """
        Retrieves expense claims

        GET /ExpenseClaims

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with all ExpenseClaims

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.expense_claims.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Status ASC",
            where='Status=="SUBMITTED"',
        )
        ```
        """
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/ExpenseClaims",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        expense_claim_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Retrieves a specific expense claim using a unique expense claim Id

        GET /ExpenseClaims/{ExpenseClaimID}

        Args:
            expense_claim_id: Unique identifier for a ExpenseClaim
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with specified ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.expense_claims.get(
            expense_claim_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/ExpenseClaims/{expense_claim_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        expense_claim_id: str,
        xero_tenant_id: str,
        expense_claims: typing.Union[
            typing.Optional[typing.List[params.ExpenseClaim]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Updates a specific expense claims

        POST /ExpenseClaims/{ExpenseClaimID}

        Args:
            expense_claims: typing.List[ExpenseClaim]
            expense_claim_id: Unique identifier for a ExpenseClaim
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with updated ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.expense_claims.update(
            expense_claim_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            expense_claims=[
                {
                    "status": "SUBMITTED",
                    "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
                }
            ],
        )
        ```
        """
        params._SerializerExpenseClaims.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"expense_claims": expense_claims},
            dump_with=params._SerializerExpenseClaims,
        )
        return self._base_client.request(
            method="POST",
            path=f"/ExpenseClaims/{expense_claim_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        expense_claims: typing.Union[
            typing.Optional[typing.List[params.ExpenseClaim]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Creates expense claims

        PUT /ExpenseClaims

        Args:
            expense_claims: typing.List[ExpenseClaim]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with newly created ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.expense_claims.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            expense_claims=[
                {
                    "status": "SUBMITTED",
                    "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
                }
            ],
        )
        ```
        """
        params._SerializerExpenseClaims.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"expense_claims": expense_claims},
            dump_with=params._SerializerExpenseClaims,
        )
        return self._base_client.request(
            method="PUT",
            path="/ExpenseClaims",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )


class AsyncExpenseClaimsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.history = AsyncHistoryClient(base_client=self._base_client)

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
    ) -> models.ExpenseClaims:
        """
        Retrieves expense claims

        GET /ExpenseClaims

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with all ExpenseClaims

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.expense_claims.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Status ASC",
            where='Status=="SUBMITTED"',
        )
        ```
        """
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/ExpenseClaims",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        expense_claim_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Retrieves a specific expense claim using a unique expense claim Id

        GET /ExpenseClaims/{ExpenseClaimID}

        Args:
            expense_claim_id: Unique identifier for a ExpenseClaim
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with specified ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.expense_claims.get(
            expense_claim_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/ExpenseClaims/{expense_claim_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        expense_claim_id: str,
        xero_tenant_id: str,
        expense_claims: typing.Union[
            typing.Optional[typing.List[params.ExpenseClaim]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Updates a specific expense claims

        POST /ExpenseClaims/{ExpenseClaimID}

        Args:
            expense_claims: typing.List[ExpenseClaim]
            expense_claim_id: Unique identifier for a ExpenseClaim
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with updated ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.expense_claims.update(
            expense_claim_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            expense_claims=[
                {
                    "status": "SUBMITTED",
                    "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
                }
            ],
        )
        ```
        """
        params._SerializerExpenseClaims.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"expense_claims": expense_claims},
            dump_with=params._SerializerExpenseClaims,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/ExpenseClaims/{expense_claim_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        expense_claims: typing.Union[
            typing.Optional[typing.List[params.ExpenseClaim]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ExpenseClaims:
        """
        Creates expense claims

        PUT /ExpenseClaims

        Args:
            expense_claims: typing.List[ExpenseClaim]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ExpenseClaims array with newly created ExpenseClaim

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.expense_claims.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            expense_claims=[
                {
                    "status": "SUBMITTED",
                    "user": {"user_id": "d1164823-0ac1-41ad-987b-b4e30fe0b273"},
                }
            ],
        )
        ```
        """
        params._SerializerExpenseClaims.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ExpenseClaims.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"expense_claims": expense_claims},
            dump_with=params._SerializerExpenseClaims,
        )
        return await self._base_client.request(
            method="PUT",
            path="/ExpenseClaims",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ExpenseClaims,
            request_options=request_options or default_request_options(),
        )
