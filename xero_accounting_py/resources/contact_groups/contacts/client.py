import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models, params


class ContactsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete_all(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes all contacts from a specific contact group

        DELETE /ContactGroups/{ContactGroupID}/Contacts

        Args:
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.contacts.delete_all(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/ContactGroups/{contact_group_id}/Contacts",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        contact_group_id: str,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific contact from a contact group using a unique contact Id

        DELETE /ContactGroups/{ContactGroupID}/Contacts/{ContactID}

        Args:
            contact_group_id: Unique identifier for a Contact Group
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.contacts.delete(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/ContactGroups/{contact_group_id}/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        contact_group_id: str,
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
        Creates contacts to a specific contact group

        PUT /ContactGroups/{ContactGroupID}/Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array of added Contacts

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.contact_groups.contacts.create(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {"contact_id": "a3675fc4-f8dd-4f03-ba5b-f1870566bcd7"},
                {"contact_id": "4e1753b9-018a-4775-b6aa-1bc7871cfee3"},
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
            method="PUT",
            path=f"/ContactGroups/{contact_group_id}/Contacts",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )


class AsyncContactsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete_all(
        self,
        *,
        contact_group_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes all contacts from a specific contact group

        DELETE /ContactGroups/{ContactGroupID}/Contacts

        Args:
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.contacts.delete_all(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/ContactGroups/{contact_group_id}/Contacts",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        contact_group_id: str,
        contact_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific contact from a contact group using a unique contact Id

        DELETE /ContactGroups/{ContactGroupID}/Contacts/{ContactID}

        Args:
            contact_group_id: Unique identifier for a Contact Group
            contact_id: Unique identifier for a Contact
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.contacts.delete(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            contact_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/ContactGroups/{contact_group_id}/Contacts/{contact_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        contact_group_id: str,
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
        Creates contacts to a specific contact group

        PUT /ContactGroups/{ContactGroupID}/Contacts

        Args:
            contacts: typing.List[Contact]
            pagination: Pagination
            warnings: Displays array of warning messages from the API
            contact_group_id: Unique identifier for a Contact Group
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Contacts array of added Contacts

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.contact_groups.contacts.create(
            contact_group_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contacts=[
                {"contact_id": "a3675fc4-f8dd-4f03-ba5b-f1870566bcd7"},
                {"contact_id": "4e1753b9-018a-4775-b6aa-1bc7871cfee3"},
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
            method="PUT",
            path=f"/ContactGroups/{contact_group_id}/Contacts",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Contacts,
            request_options=request_options or default_request_options(),
        )
