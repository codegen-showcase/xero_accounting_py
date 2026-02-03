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
from xero_accounting_py.resources.batch_payments.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class BatchPaymentsClient:
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
    ) -> models.BatchPayments:
        """
        Retrieves either one or many batch payments for invoices

        GET /BatchPayments

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array of BatchPayment objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.batch_payments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Date ASC",
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/BatchPayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        batch_payment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Retrieves a specific batch payment using a unique batch payment Id

        GET /BatchPayments/{BatchPaymentID}

        Args:
            batch_payment_id: Unique identifier for BatchPayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array with matching batch payment Id

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.batch_payments.get(
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/BatchPayments/{batch_payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        batch_payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Updates a specific batch payment for invoices and credit notes

        POST /BatchPayments

        Args:
            batch_payment_id: The Xero generated unique identifier for the bank transaction (read-only)
            status: The status of the batch payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array for updated BatchPayment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.batch_payments.delete(
            batch_payment_id="9bf296e9-0748-4d29-a3dc-24dde1098030",
            status="DELETED",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"batch_payment_id": batch_payment_id, "status": status},
            dump_with=params._SerializerBatchPaymentDelete,
        )
        return self._base_client.request(
            method="POST",
            path="/BatchPayments",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        batch_payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Updates a specific batch payment for invoices and credit notes

        POST /BatchPayments/{BatchPaymentID}

        Args:
            batch_payment_id: Unique identifier for BatchPayment
            status: The status of the batch payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array for updated BatchPayment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.batch_payments.update(
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            status="DELETED",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status},
            dump_with=params._SerializerBatchPaymentDeleteByUrlParam,
        )
        return self._base_client.request(
            method="POST",
            path=f"/BatchPayments/{batch_payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        batch_payments: typing.Union[
            typing.Optional[typing.List[params.BatchPayment]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Creates one or many batch payments for invoices

        PUT /BatchPayments

        Args:
            batch_payments: typing.List[BatchPayment]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array of BatchPayment objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.batch_payments.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            batch_payments=[
                {
                    "account": {"account_id": "00000000-0000-0000-0000-000000000000"},
                    "date": "2018-08-01",
                    "reference": "ref",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerBatchPayments.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"batch_payments": batch_payments},
            dump_with=params._SerializerBatchPayments,
        )
        return self._base_client.request(
            method="PUT",
            path="/BatchPayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )


class AsyncBatchPaymentsClient:
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
    ) -> models.BatchPayments:
        """
        Retrieves either one or many batch payments for invoices

        GET /BatchPayments

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array of BatchPayment objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.batch_payments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Date ASC",
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/BatchPayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        batch_payment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Retrieves a specific batch payment using a unique batch payment Id

        GET /BatchPayments/{BatchPaymentID}

        Args:
            batch_payment_id: Unique identifier for BatchPayment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array with matching batch payment Id

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.batch_payments.get(
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/BatchPayments/{batch_payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        batch_payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Updates a specific batch payment for invoices and credit notes

        POST /BatchPayments

        Args:
            batch_payment_id: The Xero generated unique identifier for the bank transaction (read-only)
            status: The status of the batch payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array for updated BatchPayment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.batch_payments.delete(
            batch_payment_id="9bf296e9-0748-4d29-a3dc-24dde1098030",
            status="DELETED",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"batch_payment_id": batch_payment_id, "status": status},
            dump_with=params._SerializerBatchPaymentDelete,
        )
        return await self._base_client.request(
            method="POST",
            path="/BatchPayments",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        batch_payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Updates a specific batch payment for invoices and credit notes

        POST /BatchPayments/{BatchPaymentID}

        Args:
            batch_payment_id: Unique identifier for BatchPayment
            status: The status of the batch payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array for updated BatchPayment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.batch_payments.update(
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            status="DELETED",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status},
            dump_with=params._SerializerBatchPaymentDeleteByUrlParam,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/BatchPayments/{batch_payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        batch_payments: typing.Union[
            typing.Optional[typing.List[params.BatchPayment]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BatchPayments:
        """
        Creates one or many batch payments for invoices

        PUT /BatchPayments

        Args:
            batch_payments: typing.List[BatchPayment]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BatchPayments array of BatchPayment objects

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.batch_payments.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            batch_payments=[
                {
                    "account": {"account_id": "00000000-0000-0000-0000-000000000000"},
                    "date": "2018-08-01",
                    "reference": "ref",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerBatchPayments.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.BatchPayments.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"batch_payments": batch_payments},
            dump_with=params._SerializerBatchPayments,
        )
        return await self._base_client.request(
            method="PUT",
            path="/BatchPayments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.BatchPayments,
            request_options=request_options or default_request_options(),
        )
