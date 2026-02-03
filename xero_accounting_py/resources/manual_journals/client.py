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
from xero_accounting_py.resources.manual_journals.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.manual_journals.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class ManualJournalsClient:
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
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Retrieves manual journals

        GET /ManualJournals

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment
            page_size: Number of records to retrieve per page
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with a all ManualJournals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.manual_journals.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Date ASC",
            page=1,
            page_size=100,
            where='Status=="DRAFT"',
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
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        manual_journal_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Retrieves a specific manual journal

        GET /ManualJournals/{ManualJournalID}

        Args:
            manual_journal_id: Unique identifier for a ManualJournal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with a specified ManualJournals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.manual_journals.get(
            manual_journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/ManualJournals/{manual_journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Updates or creates a single manual journal

        POST /ManualJournals

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with newly created ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.manual_journals.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "date": "2019-03-14",
                    "journal_lines": [
                        {
                            "account_code": "400",
                            "description": "Money Movement",
                            "line_amount": 100.0,
                        },
                        {
                            "account_code": "400",
                            "description": "Prepayment of things",
                            "line_amount": -100.0,
                            "tracking": [{"name": "North", "option": "Region"}],
                        },
                    ],
                    "narration": "Journal Desc",
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
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return self._base_client.request(
            method="POST",
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        manual_journal_id: str,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Updates a specific manual journal

        POST /ManualJournals/{ManualJournalID}

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            manual_journal_id: Unique identifier for a ManualJournal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with an updated ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.manual_journals.update(
            manual_journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "journal_lines": [
                        {
                            "account_code": "string",
                            "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                            "is_blank": False,
                            "line_amount": -2569.0,
                            "tax_amount": 0.0,
                        }
                    ],
                    "manual_journal_id": "00000000-0000-0000-0000-000000000000",
                    "narration": "Hello Xero",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return self._base_client.request(
            method="POST",
            path=f"/ManualJournals/{manual_journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Creates one or more manual journals

        PUT /ManualJournals

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with newly created ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.manual_journals.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "date": "2019-03-14",
                    "journal_lines": [
                        {
                            "account_code": "400",
                            "description": "Money Movement",
                            "line_amount": 100.0,
                        },
                        {
                            "account_code": "400",
                            "description": "Prepayment of things",
                            "line_amount": -100.0,
                            "tracking": [{"name": "North", "option": "Region"}],
                        },
                    ],
                    "narration": "Journal Desc",
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
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return self._base_client.request(
            method="PUT",
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )


class AsyncManualJournalsClient:
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
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Retrieves manual journals

        GET /ManualJournals

        Args:
            order: Order by an any element
            page: e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment
            page_size: Number of records to retrieve per page
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with a all ManualJournals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.manual_journals.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Date ASC",
            page=1,
            page_size=100,
            where='Status=="DRAFT"',
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
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        manual_journal_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Retrieves a specific manual journal

        GET /ManualJournals/{ManualJournalID}

        Args:
            manual_journal_id: Unique identifier for a ManualJournal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with a specified ManualJournals

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.manual_journals.get(
            manual_journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/ManualJournals/{manual_journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Updates or creates a single manual journal

        POST /ManualJournals

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with newly created ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.manual_journals.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "date": "2019-03-14",
                    "journal_lines": [
                        {
                            "account_code": "400",
                            "description": "Money Movement",
                            "line_amount": 100.0,
                        },
                        {
                            "account_code": "400",
                            "description": "Prepayment of things",
                            "line_amount": -100.0,
                            "tracking": [{"name": "North", "option": "Region"}],
                        },
                    ],
                    "narration": "Journal Desc",
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
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return await self._base_client.request(
            method="POST",
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        manual_journal_id: str,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Updates a specific manual journal

        POST /ManualJournals/{ManualJournalID}

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            manual_journal_id: Unique identifier for a ManualJournal
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with an updated ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.manual_journals.update(
            manual_journal_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "journal_lines": [
                        {
                            "account_code": "string",
                            "description": "Coded incorrectly Office Equipment should be Computer Equipment",
                            "is_blank": False,
                            "line_amount": -2569.0,
                            "tax_amount": 0.0,
                        }
                    ],
                    "manual_journal_id": "00000000-0000-0000-0000-000000000000",
                    "narration": "Hello Xero",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/ManualJournals/{manual_journal_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        manual_journals: typing.Union[
            typing.Optional[typing.List[params.ManualJournal]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ManualJournals:
        """
        Creates one or more manual journals

        PUT /ManualJournals

        Args:
            manual_journals: typing.List[ManualJournal]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type ManualJournals array with newly created ManualJournal

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.manual_journals.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            manual_journals=[
                {
                    "date": "2019-03-14",
                    "journal_lines": [
                        {
                            "account_code": "400",
                            "description": "Money Movement",
                            "line_amount": 100.0,
                        },
                        {
                            "account_code": "400",
                            "description": "Prepayment of things",
                            "line_amount": -100.0,
                            "tracking": [{"name": "North", "option": "Region"}],
                        },
                    ],
                    "narration": "Journal Desc",
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
            item={
                "manual_journals": manual_journals,
                "pagination": pagination,
                "warnings": warnings,
            },
            dump_with=params._SerializerManualJournals,
        )
        return await self._base_client.request(
            method="PUT",
            path="/ManualJournals",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.ManualJournals,
            request_options=request_options or default_request_options(),
        )
