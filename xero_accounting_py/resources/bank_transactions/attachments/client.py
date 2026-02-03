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
        bank_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves any attachments from a specific bank transactions

        GET /BankTransactions/{BankTransactionID}/Attachments

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with 0 to n Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.attachments.list(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/BankTransactions/{bank_transaction_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    def get_by_id(
        self,
        *,
        attachment_id: str,
        bank_transaction_id: str,
        content_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific attachments from a specific BankTransaction using a unique attachment Id

        GET /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for BankTransaction as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_by_filename(
        self,
        *,
        bank_transaction_id: str,
        content_type: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific bank transaction by filename

        GET /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for BankTransaction as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.attachments.get_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def update_by_filename(
        self,
        *,
        bank_transaction_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates a specific attachment from a specific bank transaction by filename

        POST /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.attachments.update_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
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
        bank_transaction_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific bank transaction by filename

        PUT /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.bank_transactions.attachments.create_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
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
        bank_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves any attachments from a specific bank transactions

        GET /BankTransactions/{BankTransactionID}/Attachments

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array with 0 to n Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.attachments.list(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/BankTransactions/{bank_transaction_id}/Attachments",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )

    async def get_by_id(
        self,
        *,
        attachment_id: str,
        bank_transaction_id: str,
        content_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific attachments from a specific BankTransaction using a unique attachment Id

        GET /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for BankTransaction as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{attachment_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_by_filename(
        self,
        *,
        bank_transaction_id: str,
        content_type: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment from a specific bank transaction by filename

        GET /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for BankTransaction as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.attachments.get_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def update_by_filename(
        self,
        *,
        bank_transaction_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates a specific attachment from a specific bank transaction by filename

        POST /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.attachments.update_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
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
        bank_transaction_id: str,
        data: str,
        file_name: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates an attachment for a specific bank transaction by filename

        PUT /BankTransactions/{BankTransactionID}/Attachments/{FileName}

        Args:
            bank_transaction_id: Xero generated unique identifier for a bank transaction
            data: str
            file_name: Name of the attachment
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.bank_transactions.attachments.create_by_filename(
            bank_transaction_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/BankTransactions/{bank_transaction_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )
