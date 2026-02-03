import typing

from make_api_request import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_content,
)
from xero_accounting_py.types import models


class AttachmentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific accounts by using a unique account Id

        GET /Accounts/{AccountID}/Attachments

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.attachments.list(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    def get_by_id(
        self,
        *,
        account_id: str,
        attachment_id: str,
        content_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific account using a unique attachment Id

        GET /Accounts/{AccountID}/Attachments/{AttachmentID}

        Args:
            account_id: Unique identifier for Account object
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.attachments.get_by_id(
            account_id="00000000-0000-0000-0000-000000000000",
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_by_filename(
        self,
        *,
        account_id: str,
        content_type: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves an attachment for a specific account by filename

        GET /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.attachments.get_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
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
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update_by_filename(
        self,
        *,
        account_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates attachment on a specific account by filename

        POST /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.attachments.update_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
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
        account_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment on a specific account

        PUT /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.attachments.create_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
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
            method="PUT",
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
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
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific accounts by using a unique account Id

        GET /Accounts/{AccountID}/Attachments

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.attachments.list(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    async def get_by_id(
        self,
        *,
        account_id: str,
        attachment_id: str,
        content_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific account using a unique attachment Id

        GET /Accounts/{AccountID}/Attachments/{AttachmentID}

        Args:
            account_id: Unique identifier for Account object
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.attachments.get_by_id(
            account_id="00000000-0000-0000-0000-000000000000",
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_by_filename(
        self,
        *,
        account_id: str,
        content_type: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves an attachment for a specific account by filename

        GET /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.attachments.get_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
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
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update_by_filename(
        self,
        *,
        account_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates attachment on a specific account by filename

        POST /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.attachments.update_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
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
        account_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment on a specific account

        PUT /Accounts/{AccountID}/Attachments/{FileName}

        Args:
            account_id: Unique identifier for Account object
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.attachments.create_by_filename(
            account_id="00000000-0000-0000-0000-000000000000",
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
            method="PUT",
            path=f"/Accounts/{account_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )
