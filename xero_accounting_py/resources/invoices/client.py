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
from xero_accounting_py.resources.invoices.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.invoices.email import AsyncEmailClient, EmailClient
from xero_accounting_py.resources.invoices.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.resources.invoices.online_invoice import (
    AsyncOnlineInvoiceClient,
    OnlineInvoiceClient,
)
from xero_accounting_py.resources.invoices.pdf import AsyncPdfClient, PdfClient
from xero_accounting_py.types import models, params


class InvoicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)
        self.online_invoice = OnlineInvoiceClient(base_client=self._base_client)
        self.pdf = PdfClient(base_client=self._base_client)
        self.email = EmailClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        contact_i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_by_my_app: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_numbers: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        search_term: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statuses: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summary_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoices:
        """
        Retrieves sales invoices or purchase bills

        GET /Invoices

        Args:
            contact_i_ds: Filter by a comma-separated list of ContactIDs.
            created_by_my_app: When set to true you'll only retrieve Invoices created by your app
            i_ds: Filter by a comma-separated list of InvoicesIDs.
            include_archived: e.g. includeArchived=true - Invoices with a status of ARCHIVED will be included in the response
            invoice_numbers: Filter by a comma-separated list of InvoiceNumbers.
            order: Order by an any element
            page: e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice
            page_size: Number of records to retrieve per page
            search_term: Search parameter that performs a case-insensitive text search across the fields e.g. InvoiceNumber, Reference.
            statuses: Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.
            summary_only: Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient.
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with all Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            created_by_my_app=False,
            include_archived=True,
            order="InvoiceNumber ASC",
            page=1,
            page_size=100,
            search_term="SearchTerm=REF12",
            summary_only=True,
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(contact_i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactIDs",
                to_encodable(item=contact_i_ds, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(created_by_my_app, type_utils.NotGiven):
            encode_query_param(
                _query,
                "createdByMyApp",
                to_encodable(item=created_by_my_app, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IDs",
                to_encodable(item=i_ds, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(include_archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "includeArchived",
                to_encodable(item=include_archived, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(invoice_numbers, type_utils.NotGiven):
            encode_query_param(
                _query,
                "InvoiceNumbers",
                to_encodable(item=invoice_numbers, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
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
        if not isinstance(search_term, type_utils.NotGiven):
            encode_query_param(
                _query,
                "searchTerm",
                to_encodable(item=search_term, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(statuses, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Statuses",
                to_encodable(item=statuses, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(summary_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summaryOnly",
                to_encodable(item=summary_only, dump_with=bool),
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
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoices:
        """
        Retrieves a specific sales invoice or purchase bill using a unique invoice Id

        GET /Invoices/{InvoiceID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.get(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/Invoices/{invoice_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Updates or creates one or more sales invoices or purchase bills

        POST /Invoices

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with newly created Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "date": "2019-03-11",
                    "due_date": "2018-12-10",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Acme Tires",
                            "line_amount": 40.0,
                            "quantity": 2.0,
                            "tax_type": "NONE",
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "Website Design",
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return self._base_client.request(
            method="POST",
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Updates a specific sales invoices or purchase bills

        POST /Invoices/{InvoiceID}

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with updated Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.update(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "invoice_id": "00000000-0000-0000-0000-000000000000",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "reference": "May the force be with you",
                    "type_": "ACCPAY",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return self._base_client.request(
            method="POST",
            path=f"/Invoices/{invoice_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Creates one or more sales invoices or purchase bills

        PUT /Invoices

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with newly created Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "date": "2019-03-11",
                    "due_date": "2018-12-10",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Acme Tires",
                            "line_amount": 40.0,
                            "quantity": 2.0,
                            "tax_type": "NONE",
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "Website Design",
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return self._base_client.request(
            method="PUT",
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )


class AsyncInvoicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)
        self.online_invoice = AsyncOnlineInvoiceClient(base_client=self._base_client)
        self.pdf = AsyncPdfClient(base_client=self._base_client)
        self.email = AsyncEmailClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        contact_i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created_by_my_app: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_numbers: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page_size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        search_term: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statuses: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summary_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoices:
        """
        Retrieves sales invoices or purchase bills

        GET /Invoices

        Args:
            contact_i_ds: Filter by a comma-separated list of ContactIDs.
            created_by_my_app: When set to true you'll only retrieve Invoices created by your app
            i_ds: Filter by a comma-separated list of InvoicesIDs.
            include_archived: e.g. includeArchived=true - Invoices with a status of ARCHIVED will be included in the response
            invoice_numbers: Filter by a comma-separated list of InvoiceNumbers.
            order: Order by an any element
            page: e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice
            page_size: Number of records to retrieve per page
            search_term: Search parameter that performs a case-insensitive text search across the fields e.g. InvoiceNumber, Reference.
            statuses: Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.
            summary_only: Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient.
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with all Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            created_by_my_app=False,
            include_archived=True,
            order="InvoiceNumber ASC",
            page=1,
            page_size=100,
            search_term="SearchTerm=REF12",
            summary_only=True,
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(contact_i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactIDs",
                to_encodable(item=contact_i_ds, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(created_by_my_app, type_utils.NotGiven):
            encode_query_param(
                _query,
                "createdByMyApp",
                to_encodable(item=created_by_my_app, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(i_ds, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IDs",
                to_encodable(item=i_ds, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(include_archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "includeArchived",
                to_encodable(item=include_archived, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(invoice_numbers, type_utils.NotGiven):
            encode_query_param(
                _query,
                "InvoiceNumbers",
                to_encodable(item=invoice_numbers, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
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
        if not isinstance(search_term, type_utils.NotGiven):
            encode_query_param(
                _query,
                "searchTerm",
                to_encodable(item=search_term, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(statuses, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Statuses",
                to_encodable(item=statuses, dump_with=typing.List[str]),
                style="form",
                explode=False,
            )
        if not isinstance(summary_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summaryOnly",
                to_encodable(item=summary_only, dump_with=bool),
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
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invoices:
        """
        Retrieves a specific sales invoice or purchase bill using a unique invoice Id

        GET /Invoices/{InvoiceID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.get(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/Invoices/{invoice_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Updates or creates one or more sales invoices or purchase bills

        POST /Invoices

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with newly created Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "date": "2019-03-11",
                    "due_date": "2018-12-10",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Acme Tires",
                            "line_amount": 40.0,
                            "quantity": 2.0,
                            "tax_type": "NONE",
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "Website Design",
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return await self._base_client.request(
            method="POST",
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        invoice_id: str,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Updates a specific sales invoices or purchase bills

        POST /Invoices/{InvoiceID}

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with updated Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.update(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "invoice_id": "00000000-0000-0000-0000-000000000000",
                    "line_items": [
                        {
                            "account_id": "00000000-0000-0000-0000-000000000000",
                            "line_item_id": "00000000-0000-0000-0000-000000000000",
                            "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                        }
                    ],
                    "reference": "May the force be with you",
                    "type_": "ACCPAY",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Invoices/{invoice_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        invoices: typing.Union[
            typing.Optional[typing.List[params.Invoice]], type_utils.NotGiven
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
    ) -> models.Invoices:
        """
        Creates one or more sales invoices or purchase bills

        PUT /Invoices

        Args:
            invoices: typing.List[Invoice]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Invoices array with newly created Invoice

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            invoices=[
                {
                    "date": "2019-03-11",
                    "due_date": "2018-12-10",
                    "line_items": [
                        {
                            "account_code": "200",
                            "description": "Acme Tires",
                            "line_amount": 40.0,
                            "quantity": 2.0,
                            "tax_type": "NONE",
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "Website Design",
                    "status": "AUTHORISED",
                    "type_": "ACCREC",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerInvoices.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Invoices.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"invoices": invoices, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerInvoices,
        )
        return await self._base_client.request(
            method="PUT",
            path="/Invoices",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Invoices,
            request_options=request_options or default_request_options(),
        )
