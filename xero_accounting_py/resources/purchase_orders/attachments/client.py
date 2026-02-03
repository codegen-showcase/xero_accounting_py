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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific purchase order

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Purchase Orders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.list(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific attachment for a specific purchase order using a unique attachment Id

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{attachment_id}",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment for a specific purchase order by filename

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Purchase Order as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.get_by_filename(
            content_type="image/jpg",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_as_pdf(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific purchase order as PDF files using a unique purchase order Id

        GET /PurchaseOrders/{PurchaseOrderID}/pdf

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of byte array pdf version of specified Purchase Orders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.get_as_pdf(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/pdf",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates a specific attachment for a specific purchase order by filename

        POST /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.update_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates attachment for a specific purchase order

        PUT /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.purchase_orders.attachments.create_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Retrieves attachments for a specific purchase order

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Purchase Orders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.list(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific attachment for a specific purchase order using a unique attachment Id

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{AttachmentID}

        Args:
            attachment_id: Unique identifier for Attachment object
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Account as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.get_by_id(
            attachment_id="00000000-0000-0000-0000-000000000000",
            content_type="image/jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{attachment_id}",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves a specific attachment for a specific purchase order by filename

        GET /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of attachment for Purchase Order as binary data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.get_by_filename(
            content_type="image/jpg",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["contentType"] = str(content_type)
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_as_pdf(
        self,
        *,
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves specific purchase order as PDF files using a unique purchase order Id

        GET /PurchaseOrders/{PurchaseOrderID}/pdf

        Args:
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of byte array pdf version of specified Purchase Orders

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.get_as_pdf(
            purchase_order_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/PurchaseOrders/{purchase_order_id}/pdf",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Updates a specific attachment for a specific purchase order by filename

        POST /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.update_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
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
        purchase_order_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Attachments:
        """
        Creates attachment for a specific purchase order

        PUT /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName}

        Args:
            data: str
            file_name: Name of the attachment
            purchase_order_id: Unique identifier for an Purchase Order
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Attachments array of Attachment

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.purchase_orders.attachments.create_by_filename(
            data="string",
            file_name="xero-dev.jpg",
            purchase_order_id="00000000-0000-0000-0000-000000000000",
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
            path=f"/PurchaseOrders/{purchase_order_id}/Attachments/{file_name}",
            auth_names=["OAuth2"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.Attachments,
            request_options=request_options or default_request_options(),
        )
