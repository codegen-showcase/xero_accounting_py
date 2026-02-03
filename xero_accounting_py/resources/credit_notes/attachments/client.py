import typing

from make_api_request import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_content,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models


class AttachmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific credit notes

        GET /CreditNotes/{CreditNoteID}/Attachments

        Args:
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with all Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.attachments.list(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    def get_by_id(
        self,
        *,
        attachment_id: str,
        content_type: str,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific credit note using a unique attachment Id

        GET /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Credit Note as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_by_filename(
        self,
        *,
        content_type: str,
        credit_note_id: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment on a specific credit note by file name

        GET /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            credit_note_id: Unique identifier for a Credit Note
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Credit Note as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.attachments.get_by_filename(
            content_type="image/jpg",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update_by_filename(
        self,
        *,
        credit_note_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates attachments on a specific credit note by file name

        POST /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            credit_note_id: Unique identifier for a Credit Note
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with updated Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.attachments.update_by_filename(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            data="string",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="POST",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    def create_by_filename(
        self,
        *,
        credit_note_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        include_online: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific credit note

        PUT /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            include_online: Allows an attachment to be seen by the end customer within their online invoice
            credit_note_id: Unique identifier for a Credit Note
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with newly created Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.attachments.create_by_filename(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            data="string",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            include_online=True,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_online, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IncludeOnline",
                to_encodable(item=include_online, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return self._base_client.request(
            method="PUT",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )


class AsyncAttachmentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific credit notes

        GET /CreditNotes/{CreditNoteID}/Attachments

        Args:
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with all Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.attachments.list(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    async def get_by_id(
        self,
        *,
        attachment_id: str,
        content_type: str,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific credit note using a unique attachment Id

        GET /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Credit Note as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_by_filename(
        self,
        *,
        content_type: str,
        credit_note_id: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment on a specific credit note by file name

        GET /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            credit_note_id: Unique identifier for a Credit Note
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Credit Note as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.attachments.get_by_filename(
            content_type="image/jpg",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update_by_filename(
        self,
        *,
        credit_note_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates attachments on a specific credit note by file name

        POST /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            credit_note_id: Unique identifier for a Credit Note
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with updated Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.attachments.update_by_filename(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            data="string",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="POST",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    async def create_by_filename(
        self,
        *,
        credit_note_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        include_online: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific credit note

        PUT /CreditNotes/{CreditNoteID}/Attachments/{FileName}

        Args:
            include_online: Allows an attachment to be seen by the end customer within their online invoice
            credit_note_id: Unique identifier for a Credit Note
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with newly created Attachment for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.attachments.create_by_filename(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            data="string",
            file_name="xero-dev.jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            include_online=True,
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_online, type_utils.NotGiven):
            encode_query_param(
                _query,
                "IncludeOnline",
                to_encodable(item=include_online, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _content = to_content(file=data)
        _content_type = "application/octet-stream"
        return await self._base_client.request(
            method="PUT",
            path=f"/CreditNotes/{credit_note_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )
