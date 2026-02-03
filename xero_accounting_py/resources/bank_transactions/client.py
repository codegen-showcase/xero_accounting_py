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
from xero_accounting_py.resources.bank_transactions.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.bank_transactions.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class BankTransactionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Retrieves any spent or received money transactions

        GET /BankTransactions

        Args:
            order: Order by an any element
            page: Up to 100 bank transactions will be returned in a single API call with line items details
            page_size: Number of records to retrieve per page
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with 0 to n BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Type ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
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
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        bank_transaction_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Retrieves a single spent or received money transaction by using a unique bank transaction Id

        GET /BankTransactions/{BankTransactionID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with a specific BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.get(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/BankTransactions/{bank_transaction_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Updates or creates one or more spent or received money transaction

        POST /BankTransactions

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with new BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transactions=[
                {
                    "bank_account": {"code": "088"},
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "type_": "SPEND",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return self._base_client.request(
            method="POST",
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        bank_transaction_id: str,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Updates a single spent or received money transaction

        POST /BankTransactions/{BankTransactionID}

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with updated BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.update(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transactions=[
                {
                    "bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "code": "088",
                        "name": "Business Wells Fargo",
                    },
                    "bank_transaction_id": "00000000-0000-0000-0000-000000000000",
                    "currency_code": "USD",
                    "currency_rate": 1.0,
                    "date": "2019-02-25",
                    "is_reconciled": False,
                    "line_amount_types": "Inclusive",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "reference": "You just updated",
                    "status": "AUTHORISED",
                    "total_tax": 1.74,
                    "type_": "SPEND",
                    "updated_date_utc": "2019-02-26T12:39:27.813-08:00",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return self._base_client.request(
            method="POST",
            path=f"/BankTransactions/{bank_transaction_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Creates one or more spent or received money transaction

        PUT /BankTransactions

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with new BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True, unitdp=4
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return self._base_client.request(
            method="PUT",
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )


class AsyncBankTransactionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Retrieves any spent or received money transactions

        GET /BankTransactions

        Args:
            order: Order by an any element
            page: Up to 100 bank transactions will be returned in a single API call with line items details
            page_size: Number of records to retrieve per page
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with 0 to n BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Type ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(item=order, dump_with=str),
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
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        bank_transaction_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Retrieves a single spent or received money transaction by using a unique bank transaction Id

        GET /BankTransactions/{BankTransactionID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with a specific BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.get(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/BankTransactions/{bank_transaction_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Updates or creates one or more spent or received money transaction

        POST /BankTransactions

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with new BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transactions=[
                {
                    "bank_account": {"code": "088"},
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "type_": "SPEND",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return await self._base_client.request(
            method="POST",
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        bank_transaction_id: str,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Updates a single spent or received money transaction

        POST /BankTransactions/{BankTransactionID}

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with updated BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.update(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            bank_transactions=[
                {
                    "bank_account": {
                        "account_id": "00000000-0000-0000-0000-000000000000",
                        "code": "088",
                        "name": "Business Wells Fargo",
                    },
                    "bank_transaction_id": "00000000-0000-0000-0000-000000000000",
                    "currency_code": "USD",
                    "currency_rate": 1.0,
                    "date": "2019-02-25",
                    "is_reconciled": False,
                    "line_amount_types": "Inclusive",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "reference": "You just updated",
                    "status": "AUTHORISED",
                    "total_tax": 1.74,
                    "type_": "SPEND",
                    "updated_date_utc": "2019-02-26T12:39:27.813-08:00",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/BankTransactions/{bank_transaction_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        bank_transactions: typing.Union[
            typing.Optional[typing.List[params.BankTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BankTransactions:
        """
        Creates one or more spent or received money transaction

        PUT /BankTransactions

        Args:
            bank_transactions: typing.List[BankTransaction]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BankTransactions array with new BankTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID", summarize_errors=True, unitdp=4
        )
        ```
        """
        params._SerializerBankTransactions.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BankTransactions.model_rebuild(_types_namespace=models._types_namespace)
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
        _json = to_encodable(
            item={
                "bank_transactions": bank_transactions,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerBankTransactions,
        )
        return await self._base_client.request(
            method="PUT",
            path="/BankTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BankTransactions,
            request_options=request_options or default_request_options(),
        )
