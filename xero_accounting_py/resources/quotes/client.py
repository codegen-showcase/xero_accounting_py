import typing

from make_api_request import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from xero_accounting_py.resources.quotes.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.quotes.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class QuotesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expiry_date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expiry_date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quote_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Retrieves sales quotes

        GET /Quotes

        Args:
            contact_id: Filter for quotes belonging to a particular contact
            date_from: Filter for quotes after a particular date
            date_to: Filter for quotes before a particular date
            expiry_date_from: Filter for quotes expiring after a particular date
            expiry_date_to: Filter for quotes before a particular date
            order: Order by an any element
            page: e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote
            quote_number: Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber=QU-0001)
            status: Filter for quotes of a particular Status
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type quotes array with all quotes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_id="00000000-0000-0000-0000-000000000000",
            date_from="2019-10-31",
            date_to="2019-10-31",
            expiry_date_from="2019-10-31",
            expiry_date_to="2019-10-31",
            order="Status ASC",
            page=1,
            quote_number="QU-0001",
            status="DRAFT",
        )
        ```
        """
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactID",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(expiry_date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ExpiryDateFrom",
                to_encodable(item=expiry_date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(expiry_date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ExpiryDateTo",
                to_encodable(item=expiry_date_to, dump_with=str),
                style="form",
                explode=True,
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
        if not isinstance(quote_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "QuoteNumber",
                to_encodable(item=quote_number, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Retrieves a specific quote using a unique quote Id

        GET /Quotes/{QuoteID}

        Args:
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with specified Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.get(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Quotes/{quote_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    def get_as_pdf(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific quote as a PDF file using a unique quote Id

        GET /Quotes/{QuoteID}/pdf

        Args:
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of byte array pdf version of specified Quotes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.get_as_pdf(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Quotes/{quote_id}/pdf",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Updates or creates one or more quotes

        POST /Quotes

        Args:
            quotes: typing.List[Quote]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with updated or created Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[
                {
                    "date": "2020-02-01",
                    "line_items": [
                        {
                            "account_code": "12775",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return self._base_client.request(
            method="POST",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Updates a specific quote

        POST /Quotes/{QuoteID}

        Args:
            quotes: typing.List[Quote]
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with updated Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.update(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[{"date": "2020-02-01", "reference": "I am an update"}],
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return self._base_client.request(
            method="POST",
            path=f"/Quotes/{quote_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Create one or more quotes

        PUT /Quotes

        Args:
            quotes: typing.List[Quote]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes with array with newly created Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.quotes.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[
                {
                    "date": "2020-02-01",
                    "line_items": [
                        {
                            "account_code": "12775",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return self._base_client.request(
            method="PUT",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )


class AsyncQuotesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expiry_date_from: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expiry_date_to: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        order: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quote_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Retrieves sales quotes

        GET /Quotes

        Args:
            contact_id: Filter for quotes belonging to a particular contact
            date_from: Filter for quotes after a particular date
            date_to: Filter for quotes before a particular date
            expiry_date_from: Filter for quotes expiring after a particular date
            expiry_date_to: Filter for quotes before a particular date
            order: Order by an any element
            page: e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote
            quote_number: Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber=QU-0001)
            status: Filter for quotes of a particular Status
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type quotes array with all quotes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_id="00000000-0000-0000-0000-000000000000",
            date_from="2019-10-31",
            date_to="2019-10-31",
            expiry_date_from="2019-10-31",
            expiry_date_to="2019-10-31",
            order="Status ASC",
            page=1,
            quote_number="QU-0001",
            status="DRAFT",
        )
        ```
        """
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactID",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
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
        if not isinstance(expiry_date_from, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ExpiryDateFrom",
                to_encodable(item=expiry_date_from, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(expiry_date_to, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ExpiryDateTo",
                to_encodable(item=expiry_date_to, dump_with=str),
                style="form",
                explode=True,
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
        if not isinstance(quote_number, type_utils.NotGiven):
            encode_query_param(
                _query,
                "QuoteNumber",
                to_encodable(item=quote_number, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Retrieves a specific quote using a unique quote Id

        GET /Quotes/{QuoteID}

        Args:
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with specified Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.get(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Quotes/{quote_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    async def get_as_pdf(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific quote as a PDF file using a unique quote Id

        GET /Quotes/{QuoteID}/pdf

        Args:
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of byte array pdf version of specified Quotes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.get_as_pdf(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Quotes/{quote_id}/pdf",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Updates or creates one or more quotes

        POST /Quotes

        Args:
            quotes: typing.List[Quote]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with updated or created Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[
                {
                    "date": "2020-02-01",
                    "line_items": [
                        {
                            "account_code": "12775",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return await self._base_client.request(
            method="POST",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        quote_id: str,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Updates a specific quote

        POST /Quotes/{QuoteID}

        Args:
            quotes: typing.List[Quote]
            quote_id: Unique identifier for an Quote
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes array with updated Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.update(
            quote_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[{"date": "2020-02-01", "reference": "I am an update"}],
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Quotes/{quote_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        quotes: typing.Union[
            typing.Optional[typing.List[params.Quote]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Quotes:
        """
        Create one or more quotes

        PUT /Quotes

        Args:
            quotes: typing.List[Quote]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Quotes with array with newly created Quote

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.quotes.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            quotes=[
                {
                    "date": "2020-02-01",
                    "line_items": [
                        {
                            "account_code": "12775",
                            "description": "Foobar",
                            "quantity": 1.0,
                            "unit_amount": 20.0,
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerQuotes.model_rebuild(_types_namespace=params._types_namespace)
        models.Quotes.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"quotes": quotes}, dump_with=params._SerializerQuotes
        )
        return await self._base_client.request(
            method="PUT",
            path="/Quotes",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Quotes,
            request_options=request_options or default_request_options(),
        )
