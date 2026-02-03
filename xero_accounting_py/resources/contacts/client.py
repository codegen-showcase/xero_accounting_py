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
from xero_accounting_py.resources.contacts.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.resources.contacts.cis_settings import (
    AsyncCisSettingsClient,
    CisSettingsClient,
)
from xero_accounting_py.resources.contacts.history import (
    AsyncHistoryClient,
    HistoryClient,
)
from xero_accounting_py.types import models, params


class ContactsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)
        self.cis_settings = CisSettingsClient(base_client=self._base_client)
        self.history = HistoryClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
        summary_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves all contacts in a Xero organisation

        GET /Contacts

        Args:
            i_ds: Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.
            include_archived: e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
            order: Order by an any element
            page: e.g. page=1 - Up to 100 contacts will be returned in a single API call.
            page_size: Number of records to retrieve per page
            search_term: Search parameter that performs a case-insensitive text search across the Name, FirstName, LastName, ContactNumber and EmailAddress fields.
            summary_only: Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient.
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with 0 to N Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
            include_archived=True,
            order="Name ASC",
            page=1,
            page_size=100,
            search_term="Joe Bloggs",
            summary_only=True,
            where="ContactStatus==&quot;ACTIVE&quot;",
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
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
        if not isinstance(summary_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summaryOnly",
                to_encodable(item=summary_only, dump_with=bool),
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
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves a specific contacts in a Xero organisation using a unique contact Id

        GET /Contacts/{ContactID}

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with a unique Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.get(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    def get_by_contact_number(
        self,
        *,
        contact_number: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves a specific contact by contact number in a Xero organisation

        GET /Contacts/{ContactNumber}

        Args:
            contact_number: This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50).
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with a unique Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.get_by_contact_number(
            contact_number="SB2", xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_number}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
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
    ) -> models.Contacts:
        """
        Updates or creates one or more contacts in a Xero organisation

        POST /Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with newly created Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {
                    "email_address": "hulk@avengers.com",
                    "name": "Bruce Banner",
                    "payment_terms": {
                        "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                        "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
                    },
                    "phones": [
                        {
                            "phone_area_code": "415",
                            "phone_number": "555-1212",
                            "phone_type": "MOBILE",
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return self._base_client.request(
            method="POST",
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Updates a specific contact in a Xero organisation

        POST /Contacts/{ContactID}

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with an updated Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.update(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {"contact_id": "00000000-0000-0000-0000-000000000000", "name": "Thanos"}
            ],
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return self._base_client.request(
            method="POST",
            path=f"/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
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
    ) -> models.Contacts:
        """
        Creates multiple contacts (bulk) in a Xero organisation

        PUT /Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with newly created Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contacts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {
                    "addresses": [
                        {
                            "address_type": "STREET",
                            "city": "",
                            "country": "",
                            "postal_code": "",
                            "region": "",
                        },
                        {
                            "address_type": "POBOX",
                            "city": "",
                            "country": "",
                            "postal_code": "",
                            "region": "",
                        },
                    ],
                    "bank_account_details": "",
                    "contact_id": "3ff6d40c-af9a-40a3-89ce-3c1556a25591",
                    "contact_persons": [{}],
                    "contact_status": "ACTIVE",
                    "email_address": "sid32476@blah.com",
                    "is_customer": False,
                    "is_supplier": False,
                    "name": "Foo9987",
                    "payment_terms": {
                        "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                        "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
                    },
                    "phones": [
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "DEFAULT",
                        },
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "DDI",
                        },
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "FAX",
                        },
                        {
                            "phone_area_code": "415",
                            "phone_country_code": "",
                            "phone_number": "555-1212",
                            "phone_type": "MOBILE",
                        },
                    ],
                    "purchases_tracking_categories": [{}],
                    "sales_tracking_categories": [{}],
                    "updated_date_utc": "/Date(1551399321043+0000)/",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return self._base_client.request(
            method="PUT",
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )


class AsyncContactsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)
        self.cis_settings = AsyncCisSettingsClient(base_client=self._base_client)
        self.history = AsyncHistoryClient(base_client=self._base_client)

    async def list(
        self,
        *,
        xero_tenant_id: str,
        i_ds: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        include_archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
        summary_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        where: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves all contacts in a Xero organisation

        GET /Contacts

        Args:
            i_ds: Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.
            include_archived: e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
            order: Order by an any element
            page: e.g. page=1 - Up to 100 contacts will be returned in a single API call.
            page_size: Number of records to retrieve per page
            search_term: Search parameter that performs a case-insensitive text search across the Name, FirstName, LastName, ContactNumber and EmailAddress fields.
            summary_only: Use summaryOnly=true in GET Contacts and Invoices endpoint to retrieve a smaller version of the response object. This returns only lightweight fields, excluding computation-heavy fields from the response, making the API calls quick and efficient.
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with 0 to N Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            i_ds=["&quot;00000000-0000-0000-0000-000000000000&quot;"],
            include_archived=True,
            order="Name ASC",
            page=1,
            page_size=100,
            search_term="Joe Bloggs",
            summary_only=True,
            where="ContactStatus==&quot;ACTIVE&quot;",
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
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
        if not isinstance(summary_only, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summaryOnly",
                to_encodable(item=summary_only, dump_with=bool),
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
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves a specific contacts in a Xero organisation using a unique contact Id

        GET /Contacts/{ContactID}

        Args:
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with a unique Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.get(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    async def get_by_contact_number(
        self,
        *,
        contact_number: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Retrieves a specific contact by contact number in a Xero organisation

        GET /Contacts/{ContactNumber}

        Args:
            contact_number: This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50).
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with a unique Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.get_by_contact_number(
            contact_number="SB2", xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Contacts/{contact_number}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    async def update_or_create(
        self,
        *,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
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
    ) -> models.Contacts:
        """
        Updates or creates one or more contacts in a Xero organisation

        POST /Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with newly created Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.update_or_create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {
                    "email_address": "hulk@avengers.com",
                    "name": "Bruce Banner",
                    "payment_terms": {
                        "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                        "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
                    },
                    "phones": [
                        {
                            "phone_area_code": "415",
                            "phone_number": "555-1212",
                            "phone_type": "MOBILE",
                        }
                    ],
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return await self._base_client.request(
            method="POST",
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        contact_id: str,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pagination: typing.Union[
            typing.Optional[params.Pagination], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        warnings: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Contacts:
        """
        Updates a specific contact in a Xero organisation

        POST /Contacts/{ContactID}

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with an updated Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.update(
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {"contact_id": "00000000-0000-0000-0000-000000000000", "name": "Thanos"}
            ],
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        contacts: typing.Union[
            typing.Optional[typing.List[params.Contact]], type_utils.NotGiven
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
    ) -> models.Contacts:
        """
        Creates multiple contacts (bulk) in a Xero organisation

        PUT /Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            warnings: Displays array of warning messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array with newly created Contact

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contacts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {
                    "addresses": [
                        {
                            "address_type": "STREET",
                            "city": "",
                            "country": "",
                            "postal_code": "",
                            "region": "",
                        },
                        {
                            "address_type": "POBOX",
                            "city": "",
                            "country": "",
                            "postal_code": "",
                            "region": "",
                        },
                    ],
                    "bank_account_details": "",
                    "contact_id": "3ff6d40c-af9a-40a3-89ce-3c1556a25591",
                    "contact_persons": [{}],
                    "contact_status": "ACTIVE",
                    "email_address": "sid32476@blah.com",
                    "is_customer": False,
                    "is_supplier": False,
                    "name": "Foo9987",
                    "payment_terms": {
                        "bills": {"day": 15, "type_": "OFCURRENTMONTH"},
                        "sales": {"day": 10, "type_": "DAYSAFTERBILLMONTH"},
                    },
                    "phones": [
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "DEFAULT",
                        },
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "DDI",
                        },
                        {
                            "phone_area_code": "",
                            "phone_country_code": "",
                            "phone_number": "",
                            "phone_type": "FAX",
                        },
                        {
                            "phone_area_code": "415",
                            "phone_country_code": "",
                            "phone_number": "555-1212",
                            "phone_type": "MOBILE",
                        },
                    ],
                    "purchases_tracking_categories": [{}],
                    "sales_tracking_categories": [{}],
                    "updated_date_utc": "/Date(1551399321043+0000)/",
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerContacts.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Contacts.model_rebuild(_types_namespace=models._types_namespace)
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
            item={"contacts": contacts, "pagination": pagination, "warnings": warnings},
            dump_with=params._SerializerContacts,
        )
        return await self._base_client.request(
            method="PUT",
            path="/Contacts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )
