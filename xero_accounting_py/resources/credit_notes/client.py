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
from xero_accounting_py.resources.credit_notes.allocations import (
    AllocationsClient,
    AsyncAllocationsClient,
)
from xero_accounting_py.resources.credit_notes.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.credit_notes.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.resources.credit_notes.pdf import AsyncPdfClient, PdfClient
from xero_accounting_py.types import models, params


class CreditNotesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.allocations = AllocationsClient(base_client=self._base_client)
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)
        self.pdf = PdfClient(base_client=self._base_client)

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
    ) -> models.CreditNotes:
        """
        Retrieves any credit notes

        GET /CreditNotes

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note
            page_size: Number of records to retrieve per page
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="CreditNoteNumber ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNotes:
        """
        Retrieves a specific credit note using a unique credit note Id

        GET /CreditNotes/{CreditNoteID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array with a unique CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.get(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/CreditNotes/{credit_note_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Updates or creates one or more credit notes

        POST /CreditNotes

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of newly created CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "HelloWorld",
                    "status": "AUTHORISED",
                    "type_": "ACCPAYCREDIT",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return self._base_client.request(
            method="POST",
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Updates a specific credit note

        POST /CreditNotes/{CreditNoteID}

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array with updated CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.update(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "HelloWorld",
                    "sent_to_contact": True,
                    "status": "AUTHORISED",
                    "type_": "ACCPAYCREDIT",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return self._base_client.request(
            method="POST",
            path=f"/CreditNotes/{credit_note_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Creates a new credit note

        PUT /CreditNotes

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of newly created CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "type_": "ACCPAYCREDIT",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return self._base_client.request(
            method="PUT",
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )


class AsyncCreditNotesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.allocations = AsyncAllocationsClient(base_client=self._base_client)
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)
        self.pdf = AsyncPdfClient(base_client=self._base_client)

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
    ) -> models.CreditNotes:
        """
        Retrieves any credit notes

        GET /CreditNotes

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note
            page_size: Number of records to retrieve per page
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="CreditNoteNumber ASC",
            page=1,
            page_size=100,
            unitdp=4,
            where='Status=="DRAFT"',
        )
        ```
        """
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        unitdp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreditNotes:
        """
        Retrieves a specific credit note using a unique credit note Id

        GET /CreditNotes/{CreditNoteID}

        Args:
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array with a unique CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.get(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            unitdp=4,
        )
        ```
        """
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/CreditNotes/{credit_note_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Updates or creates one or more credit notes

        POST /CreditNotes

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of newly created CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "HelloWorld",
                    "status": "AUTHORISED",
                    "type_": "ACCPAYCREDIT",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return await self._base_client.request(
            method="POST",
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Updates a specific credit note

        POST /CreditNotes/{CreditNoteID}

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array with updated CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.update(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "reference": "HelloWorld",
                    "sent_to_contact": True,
                    "status": "AUTHORISED",
                    "type_": "ACCPAYCREDIT",
                }
            ],
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/CreditNotes/{credit_note_id}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        credit_notes: typing.Union[
            typing.Optional[typing.List[params.CreditNote]], type_utils.NotGiven
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
    ) -> models.CreditNotes:
        """
        Creates a new credit note

        PUT /CreditNotes

        Args:
            credit_notes: typing.List[CreditNote]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            unitdp: e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Credit Notes array of newly created CreditNote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            credit_notes=[
                {
                    "date": "2019-01-05",
                    "line_items": [
                        {
                            "account_code": "400",
                            "description": "Foobar",
                            "quantity": 2.0,
                            "unit_amount": 20.0,
                        }
                    ],
                    "type_": "ACCPAYCREDIT",
                }
            ],
            summarize_errors=True,
            unitdp=4,
        )
        ```
        """
        params._SerializerCreditNotes.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.CreditNotes.model_rebuild(_types_namespace=models._types_namespace)
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
                "credit_notes": credit_notes,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerCreditNotes,
        )
        return await self._base_client.request(
            method="PUT",
            path="/CreditNotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.CreditNotes,
            request_options=request_options or default_request_options(),
        )
