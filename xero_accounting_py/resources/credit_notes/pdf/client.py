import typing

from make_api_request import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)


class PdfClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves credit notes as PDF files

        GET /CreditNotes/{CreditNoteID}/pdf

        Args:
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of binary data from the Attachment to a Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.pdf.get(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/pdf",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPdfClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Retrieves credit notes as PDF files

        GET /CreditNotes/{CreditNoteID}/pdf

        Args:
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of binary data from the Attachment to a Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.pdf.get(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/CreditNotes/{credit_note_id}/pdf",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
