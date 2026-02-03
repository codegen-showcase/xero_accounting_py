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
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific invoice or purchase bill

        GET /Invoices/{InvoiceID}/Attachments

        Args:
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachments for specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.attachments.list(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments",
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
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id

        GET /Invoices/{InvoiceID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Invoice as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_by_filename(
        self,
        *,
        content_type: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves an attachment from a specific invoice or purchase bill by filename

        GET /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Invoice as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.attachments.get_by_filename(
            content_type="image/jpg",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update_by_filename(
        self,
        *,
        data: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates an attachment from a specific invoices or purchase bill by filename

        POST /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with updated Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.attachments.update_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
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
        data: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        include_online: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific invoice or purchase bill by filename

        PUT /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            include_online: Allows an attachment to be seen by the end customer within their online invoice
            data: str
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with newly created Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invoices.attachments.create_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
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
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific invoice or purchase bill

        GET /Invoices/{InvoiceID}/Attachments

        Args:
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachments for specified Invoices

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.attachments.list(
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments",
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
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id

        GET /Invoices/{InvoiceID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Invoice as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_by_filename(
        self,
        *,
        content_type: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves an attachment from a specific invoice or purchase bill by filename

        GET /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Invoice as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.attachments.get_by_filename(
            content_type="image/jpg",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update_by_filename(
        self,
        *,
        data: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates an attachment from a specific invoices or purchase bill by filename

        POST /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with updated Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.attachments.update_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
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
        data: str,
        file_name: str,
        invoice_id: str,
        xero_tenant_id: str,
        include_online: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific invoice or purchase bill by filename

        PUT /Invoices/{InvoiceID}/Attachments/{FileName}

        Args:
            include_online: Allows an attachment to be seen by the end customer within their online invoice
            data: str
            file_name: Name of the attachment
            invoice_id: Unique identifier for an Invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with newly created Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invoices.attachments.create_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            invoice_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Invoices/{invoice_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )
