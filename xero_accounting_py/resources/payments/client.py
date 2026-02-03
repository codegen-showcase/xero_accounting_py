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
from xero_accounting_py.resources.payments.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class PaymentsClient:
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
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Retrieves payments for invoices and credit notes

        GET /Payments

        Args:
            order: Order by an any element
            page: Up to 100 payments will be returned in a single API call
            page_size: Number of records to retrieve per page
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for all Payments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Amount ASC",
            page=1,
            page_size=100,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/Payments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        payment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Retrieves a specific payment for invoices and credit notes using a unique payment Id

        GET /Payments/{PaymentID}

        Args:
            payment_id: Unique identifier for a Payment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for specified Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payments.get(
            payment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Payments/{payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    def create_1(
        self,
        *,
        xero_tenant_id: str,
        account: typing.Union[
            typing.Optional[params.Account], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        batch_payment: typing.Union[
            typing.Optional[params.BatchPayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        batch_payment_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_note: typing.Union[
            typing.Optional[params.CreditNote], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_note_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency_rate: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        details: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_account: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_validation_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[params.Invoice], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_reconciled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        overpayment: typing.Union[
            typing.Optional[params.Overpayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        particulars: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ACCPAYPAYMENT",
                    "ACCRECPAYMENT",
                    "APCREDITPAYMENT",
                    "APOVERPAYMENTPAYMENT",
                    "APPREPAYMENTPAYMENT",
                    "ARCREDITPAYMENT",
                    "AROVERPAYMENTPAYMENT",
                    "ARPREPAYMENTPAYMENT",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        prepayment: typing.Union[
            typing.Optional[params.Prepayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reference: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status_attribute_string: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Creates a single payment for invoice or credit notes

        POST /Payments

        Args:
            account: Account
            amount: The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00
            bank_account_number: The suppliers bank account number the payment is being made to
            bank_amount: The amount of the payment in the currency of the bank account.
            batch_payment: BatchPayment
            batch_payment_id: Present if the payment was created as part of a batch.
            code: Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)
            credit_note: CreditNote
            credit_note_number: Number of invoice or credit note you are applying payment to e.g. INV-4003
            currency_rate: Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500
            date: Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
            details: The information to appear on the supplier's bank account
            has_account: A boolean to indicate if a contact has an validation errors
            has_validation_errors: A boolean to indicate if a contact has an validation errors
            invoice: Invoice
            invoice_number: Number of invoice or credit note you are applying payment to e.g.INV-4003
            is_reconciled: An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET
            overpayment: Overpayment
            particulars: The suppliers bank account number the payment is being made to
            payment_id: The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            payment_type: See Payment Types.
            prepayment: Prepayment
            reference: An optional description for the payment e.g. Direct Debit
            status: The status of the payment.
            status_attribute_string: A string to indicate if a invoice status
            updated_date_utc: UTC timestamp of last update to the payment
            validation_errors: Displays array of validation error messages from the API
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for newly created Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payments.create_1(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            has_account=True,
            has_validation_errors=True,
            payment_id="00000000-0000-0000-0000-000000000000",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        params._SerializerPayment.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "account": account,
                "amount": amount,
                "bank_account_number": bank_account_number,
                "bank_amount": bank_amount,
                "batch_payment": batch_payment,
                "batch_payment_id": batch_payment_id,
                "code": code,
                "credit_note": credit_note,
                "credit_note_number": credit_note_number,
                "currency_rate": currency_rate,
                "date": date,
                "details": details,
                "has_account": has_account,
                "has_validation_errors": has_validation_errors,
                "invoice": invoice,
                "invoice_number": invoice_number,
                "is_reconciled": is_reconciled,
                "overpayment": overpayment,
                "particulars": particulars,
                "payment_id": payment_id,
                "payment_type": payment_type,
                "prepayment": prepayment,
                "reference": reference,
                "status": status,
                "status_attribute_string": status_attribute_string,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
                "warnings": warnings,
            },
            dump_with=params._SerializerPayment,
        )
        return self._base_client.request(
            method="POST",
            path="/Payments",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Updates a specific payment for invoices and credit notes

        POST /Payments/{PaymentID}

        Args:
            payment_id: Unique identifier for a Payment
            status: The status of the payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for updated Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payments.delete(
            payment_id="00000000-0000-0000-0000-000000000000",
            status="string",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerPaymentDelete
        )
        return self._base_client.request(
            method="POST",
            path=f"/Payments/{payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments: typing.Union[
            typing.Optional[typing.List[params.Payment]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Creates multiple payments for invoices or credit notes

        PUT /Payments

        Args:
            pagination: Pagination
            payments: typing.List[Payment]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for newly created Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payments.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            payments=[
                {"account": {"code": "970"}, "amount": 1.0, "date": "2019-03-12"}
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPayments.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"pagination": pagination, "payments": payments, "warnings": warnings},
            dump_with=params._SerializerPayments,
        )
        return self._base_client.request(
            method="PUT",
            path="/Payments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentsClient:
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
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Retrieves payments for invoices and credit notes

        GET /Payments

        Args:
            order: Order by an any element
            page: Up to 100 payments will be returned in a single API call
            page_size: Number of records to retrieve per page
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for all Payments

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payments.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Amount ASC",
            page=1,
            page_size=100,
            where='Status=="AUTHORISED"',
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/Payments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        payment_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Retrieves a specific payment for invoices and credit notes using a unique payment Id

        GET /Payments/{PaymentID}

        Args:
            payment_id: Unique identifier for a Payment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for specified Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payments.get(
            payment_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Payments/{payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    async def create_1(
        self,
        *,
        xero_tenant_id: str,
        account: typing.Union[
            typing.Optional[params.Account], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_amount: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        batch_payment: typing.Union[
            typing.Optional[params.BatchPayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        batch_payment_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_note: typing.Union[
            typing.Optional[params.CreditNote], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        credit_note_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency_rate: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        details: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_account: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_validation_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice: typing.Union[
            typing.Optional[params.Invoice], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        is_reconciled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        overpayment: typing.Union[
            typing.Optional[params.Overpayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        particulars: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ACCPAYPAYMENT",
                    "ACCRECPAYMENT",
                    "APCREDITPAYMENT",
                    "APOVERPAYMENTPAYMENT",
                    "APPREPAYMENTPAYMENT",
                    "ARCREDITPAYMENT",
                    "AROVERPAYMENTPAYMENT",
                    "ARPREPAYMENTPAYMENT",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        prepayment: typing.Union[
            typing.Optional[params.Prepayment], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reference: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status_attribute_string: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Creates a single payment for invoice or credit notes

        POST /Payments

        Args:
            account: Account
            amount: The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00
            bank_account_number: The suppliers bank account number the payment is being made to
            bank_amount: The amount of the payment in the currency of the bank account.
            batch_payment: BatchPayment
            batch_payment_id: Present if the payment was created as part of a batch.
            code: Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)
            credit_note: CreditNote
            credit_note_number: Number of invoice or credit note you are applying payment to e.g. INV-4003
            currency_rate: Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500
            date: Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
            details: The information to appear on the supplier's bank account
            has_account: A boolean to indicate if a contact has an validation errors
            has_validation_errors: A boolean to indicate if a contact has an validation errors
            invoice: Invoice
            invoice_number: Number of invoice or credit note you are applying payment to e.g.INV-4003
            is_reconciled: An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET
            overpayment: Overpayment
            particulars: The suppliers bank account number the payment is being made to
            payment_id: The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
            payment_type: See Payment Types.
            prepayment: Prepayment
            reference: An optional description for the payment e.g. Direct Debit
            status: The status of the payment.
            status_attribute_string: A string to indicate if a invoice status
            updated_date_utc: UTC timestamp of last update to the payment
            validation_errors: Displays array of validation error messages from the API
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for newly created Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payments.create_1(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            batch_payment_id="00000000-0000-0000-0000-000000000000",
            has_account=True,
            has_validation_errors=True,
            payment_id="00000000-0000-0000-0000-000000000000",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        params._SerializerPayment.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "account": account,
                "amount": amount,
                "bank_account_number": bank_account_number,
                "bank_amount": bank_amount,
                "batch_payment": batch_payment,
                "batch_payment_id": batch_payment_id,
                "code": code,
                "credit_note": credit_note,
                "credit_note_number": credit_note_number,
                "currency_rate": currency_rate,
                "date": date,
                "details": details,
                "has_account": has_account,
                "has_validation_errors": has_validation_errors,
                "invoice": invoice,
                "invoice_number": invoice_number,
                "is_reconciled": is_reconciled,
                "overpayment": overpayment,
                "particulars": particulars,
                "payment_id": payment_id,
                "payment_type": payment_type,
                "prepayment": prepayment,
                "reference": reference,
                "status": status,
                "status_attribute_string": status_attribute_string,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
                "warnings": warnings,
            },
            dump_with=params._SerializerPayment,
        )
        return await self._base_client.request(
            method="POST",
            path="/Payments",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        payment_id: str,
        status: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Updates a specific payment for invoices and credit notes

        POST /Payments/{PaymentID}

        Args:
            payment_id: Unique identifier for a Payment
            status: The status of the payment.
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for updated Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payments.delete(
            payment_id="00000000-0000-0000-0000-000000000000",
            status="string",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"status": status}, dump_with=params._SerializerPaymentDelete
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Payments/{payment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payments: typing.Union[
            typing.Optional[typing.List[params.Payment]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Payments:
        """
        Creates multiple payments for invoices or credit notes

        PUT /Payments

        Args:
            pagination: Pagination
            payments: typing.List[Payment]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Payments array for newly created Payment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payments.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            payments=[
                {"account": {"code": "970"}, "amount": 1.0, "date": "2019-03-12"}
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerPayments.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Payments.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"pagination": pagination, "payments": payments, "warnings": warnings},
            dump_with=params._SerializerPayments,
        )
        return await self._base_client.request(
            method="PUT",
            path="/Payments",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Payments,
            request_options=request_options or default_request_options(),
        )
