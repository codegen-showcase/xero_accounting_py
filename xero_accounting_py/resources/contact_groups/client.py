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
from xero_accounting_py.resources.contact_groups.contacts import (
    AsyncContactsClient,
    ContactsClient,
)
from xero_accounting_py.types import models, params


class ContactGroupsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.contacts = ContactsClient(base_client=self._base_client)

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
    ) -> models.ContactGroups:
        """
        Retrieves the contact Id and name of each contact group

        GET /ContactGroups

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/ContactGroups",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Retrieves a specific contact group by using a unique contact group Id

        GET /ContactGroups/{ContactGroupID}

        Args:
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array with a specific Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.get(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/ContactGroups/{contact_group_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        contact_groups: typing.Union[
            typing.Optional[typing.List[params.ContactGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Updates a specific contact group

        POST /ContactGroups/{ContactGroupID}

        Args:
            contact_groups: typing.List[ContactGroup]
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of updated Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.update(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_groups=[{"name": "Suppliers"}],
        )
        ```
        """
        params._SerializerContactGroups.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contact_groups": contact_groups},
            dump_with=params._SerializerContactGroups,
        )
        return self._base_client.request(
            method="POST",
            path=f"/ContactGroups/{contact_group_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        contact_groups: typing.Union[
            typing.Optional[typing.List[params.ContactGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Creates a contact group

        PUT /ContactGroups

        Args:
            contact_groups: typing.List[ContactGroup]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of newly created Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID", contact_groups=[{"name": "VIPs"}]
        )
        ```
        """
        params._SerializerContactGroups.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contact_groups": contact_groups},
            dump_with=params._SerializerContactGroups,
        )
        return self._base_client.request(
            method="PUT",
            path="/ContactGroups",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )


class AsyncContactGroupsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.contacts = AsyncContactsClient(base_client=self._base_client)

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
    ) -> models.ContactGroups:
        """
        Retrieves the contact Id and name of each contact group

        GET /ContactGroups

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
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
            path="/ContactGroups",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Retrieves a specific contact group by using a unique contact group Id

        GET /ContactGroups/{ContactGroupID}

        Args:
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array with a specific Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.get(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/ContactGroups/{contact_group_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        contact_groups: typing.Union[
            typing.Optional[typing.List[params.ContactGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Updates a specific contact group

        POST /ContactGroups/{ContactGroupID}

        Args:
            contact_groups: typing.List[ContactGroup]
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of updated Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.update(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_groups=[{"name": "Suppliers"}],
        )
        ```
        """
        params._SerializerContactGroups.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contact_groups": contact_groups},
            dump_with=params._SerializerContactGroups,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/ContactGroups/{contact_group_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        contact_groups: typing.Union[
            typing.Optional[typing.List[params.ContactGroup]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContactGroups:
        """
        Creates a contact group

        PUT /ContactGroups

        Args:
            contact_groups: typing.List[ContactGroup]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contact Groups array of newly created Contact Group

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID", contact_groups=[{"name": "VIPs"}]
        )
        ```
        """
        params._SerializerContactGroups.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.ContactGroups.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"contact_groups": contact_groups},
            dump_with=params._SerializerContactGroups,
        )
        return await self._base_client.request(
            method="PUT",
            path="/ContactGroups",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.ContactGroups,
            request_options=request_options or default_request_options(),
        )
