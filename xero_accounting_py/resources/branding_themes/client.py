import typing

from make_api_request import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from xero_accounting_py.resources.branding_themes.payment_services import (
    AsyncPaymentServicesClient,
    PaymentServicesClient,
)
from xero_accounting_py.types import models


class BrandingThemesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.payment_services = PaymentServicesClient(base_client=self._base_client)

    def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BrandingThemes:
        """
        Retrieves all the branding themes

        GET /BrandingThemes

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BrandingThemes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.branding_themes.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/BrandingThemes",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BrandingThemes,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BrandingThemes:
        """
        Retrieves a specific branding theme using a unique branding theme Id

        GET /BrandingThemes/{BrandingThemeID}

        Args:
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BrandingThemes with one BrandingTheme

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.branding_themes.get(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/BrandingThemes/{branding_theme_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BrandingThemes,
            request_options=request_options or default_request_options(),
        )


class AsyncBrandingThemesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.payment_services = AsyncPaymentServicesClient(
            base_client=self._base_client
        )

    async def list(
        self,
        *,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BrandingThemes:
        """
        Retrieves all the branding themes

        GET /BrandingThemes

        Args:
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BrandingThemes

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.branding_themes.list(xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/BrandingThemes",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BrandingThemes,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BrandingThemes:
        """
        Retrieves a specific branding theme using a unique branding theme Id

        GET /BrandingThemes/{BrandingThemeID}

        Args:
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type BrandingThemes with one BrandingTheme

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.branding_themes.get(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/BrandingThemes/{branding_theme_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.BrandingThemes,
            request_options=request_options or default_request_options(),
        )
