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
from xero_accounting_py.resources.repeating_invoices.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.repeating_invoices.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class RepeatingInvoicesClient:
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
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Retrieves repeating invoices

        GET /RepeatingInvoices

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Repeating Invoices array for all Repeating Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.repeating_invoices.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Total ASC",
            where='Status=="DRAFT"',
        )
        ```
        """
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        repeating_invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Retrieves a specific repeating invoice by using a unique repeating invoice Id

        GET /RepeatingInvoices/{RepeatingInvoiceID}

        Args:
            repeating_invoice_id: Unique identifier for a Repeating Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Repeating Invoices array with a specified Repeating Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.repeating_invoices.get(
            repeating_invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/RepeatingInvoices/{repeating_invoice_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Creates or deletes one or more repeating invoice templates

        POST /RepeatingInvoices

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with newly created RepeatingInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.repeating_invoices.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            repeating_invoices=[
                {
                    "approved_for_sending": False,
                    "currency_code": "NZD",
                    "include_pdf": False,
                    "line_amount_types": "Exclusive",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Guitars Fender Strat",
                            "line_amount": 5000.0,
                            "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                            "quantity": 1.0,
                            "tax_amount": 750.0,
                            "tax_type": "OUTPUT2",
                            "tracking": [
                                {
                                    "name": "Region",
                                    "option": "North",
                                    "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                                    "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                                }
                            ],
                            "unit_amount": 5000.0,
                        }
                    ],
                    "mark_as_sent": False,
                    "reference": "[Week]",
                    "schedule": {
                        "due_date": 10,
                        "due_date_type": "OFFOLLOWINGMONTH",
                        "period": 1,
                        "start_date": "/Date(1555286400000+0000)/",
                        "unit": "MONTHLY",
                    },
                    "send_copy": False,
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return self._base_client.request(
            method="POST",
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        repeating_invoice_id: str,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Deletes a specific repeating invoice template

        POST /RepeatingInvoices/{RepeatingInvoiceID}

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            repeating_invoice_id: Unique identifier for a Repeating Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with deleted Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.repeating_invoices.update(
            repeating_invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return self._base_client.request(
            method="POST",
            path=f"/RepeatingInvoices/{repeating_invoice_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Creates one or more repeating invoice templates

        PUT /RepeatingInvoices

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with newly created RepeatingInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.repeating_invoices.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            repeating_invoices=[
                {
                    "approved_for_sending": False,
                    "currency_code": "NZD",
                    "include_pdf": False,
                    "line_amount_types": "Exclusive",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Guitars Fender Strat",
                            "line_amount": 5000.0,
                            "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                            "quantity": 1.0,
                            "tax_amount": 750.0,
                            "tax_type": "OUTPUT2",
                            "tracking": [
                                {
                                    "name": "Region",
                                    "option": "North",
                                    "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                                    "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                                }
                            ],
                            "unit_amount": 5000.0,
                        }
                    ],
                    "mark_as_sent": False,
                    "reference": "[Week]",
                    "schedule": {
                        "due_date": 10,
                        "due_date_type": "OFFOLLOWINGMONTH",
                        "period": 1,
                        "start_date": "/Date(1555286400000+0000)/",
                        "unit": "MONTHLY",
                    },
                    "send_copy": False,
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return self._base_client.request(
            method="PUT",
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )


class AsyncRepeatingInvoicesClient:
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
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Retrieves repeating invoices

        GET /RepeatingInvoices

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Repeating Invoices array for all Repeating Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.repeating_invoices.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Total ASC",
            where='Status=="DRAFT"',
        )
        ```
        """
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        repeating_invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Retrieves a specific repeating invoice by using a unique repeating invoice Id

        GET /RepeatingInvoices/{RepeatingInvoiceID}

        Args:
            repeating_invoice_id: Unique identifier for a Repeating Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Repeating Invoices array with a specified Repeating Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.repeating_invoices.get(
            repeating_invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/RepeatingInvoices/{repeating_invoice_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Creates or deletes one or more repeating invoice templates

        POST /RepeatingInvoices

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with newly created RepeatingInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.repeating_invoices.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            repeating_invoices=[
                {
                    "approved_for_sending": False,
                    "currency_code": "NZD",
                    "include_pdf": False,
                    "line_amount_types": "Exclusive",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Guitars Fender Strat",
                            "line_amount": 5000.0,
                            "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                            "quantity": 1.0,
                            "tax_amount": 750.0,
                            "tax_type": "OUTPUT2",
                            "tracking": [
                                {
                                    "name": "Region",
                                    "option": "North",
                                    "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                                    "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                                }
                            ],
                            "unit_amount": 5000.0,
                        }
                    ],
                    "mark_as_sent": False,
                    "reference": "[Week]",
                    "schedule": {
                        "due_date": 10,
                        "due_date_type": "OFFOLLOWINGMONTH",
                        "period": 1,
                        "start_date": "/Date(1555286400000+0000)/",
                        "unit": "MONTHLY",
                    },
                    "send_copy": False,
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return await self._base_client.request(
            method="POST",
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        repeating_invoice_id: str,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Deletes a specific repeating invoice template

        POST /RepeatingInvoices/{RepeatingInvoiceID}

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            repeating_invoice_id: Unique identifier for a Repeating Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with deleted Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.repeating_invoices.update(
            repeating_invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/RepeatingInvoices/{repeating_invoice_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        repeating_invoices: typing.Union[
            typing.Optional[typing.List[params.RepeatingInvoice]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RepeatingInvoices:
        """
        Creates one or more repeating invoice templates

        PUT /RepeatingInvoices

        Args:
            repeating_invoices: typing.List[RepeatingInvoice]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type RepeatingInvoices array with newly created RepeatingInvoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.repeating_invoices.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            repeating_invoices=[
                {
                    "approved_for_sending": False,
                    "currency_code": "NZD",
                    "include_pdf": False,
                    "line_amount_types": "Exclusive",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Guitars Fender Strat",
                            "line_amount": 5000.0,
                            "line_item_id": "13a8353c-d2af-4d5b-920c-438449f08900",
                            "quantity": 1.0,
                            "tax_amount": 750.0,
                            "tax_type": "OUTPUT2",
                            "tracking": [
                                {
                                    "name": "Region",
                                    "option": "North",
                                    "tracking_category_id": "00000000-0000-0000-0000-000000000000",
                                    "tracking_option_id": "00000000-0000-0000-0000-000000000000",
                                }
                            ],
                            "unit_amount": 5000.0,
                        }
                    ],
                    "mark_as_sent": False,
                    "reference": "[Week]",
                    "schedule": {
                        "due_date": 10,
                        "due_date_type": "OFFOLLOWINGMONTH",
                        "period": 1,
                        "start_date": "/Date(1555286400000+0000)/",
                        "unit": "MONTHLY",
                    },
                    "send_copy": False,
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerRepeatingInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.RepeatingInvoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"repeating_invoices": repeating_invoices},
            dump_with=params._SerializerRepeatingInvoices,
        )
        return await self._base_client.request(
            method="PUT",
            path="/RepeatingInvoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.RepeatingInvoices,
            request_options=request_options or default_request_options(),
        )
