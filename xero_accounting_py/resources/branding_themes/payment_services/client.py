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


class PaymentServicesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentServices:
        """
        Retrieves the payment services for a specific branding theme

        GET /BrandingThemes/{BrandingThemeID}/PaymentServices

        Args:
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PaymentServices array with 0 to N PaymentService

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.branding_themes.payment_services.list(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/BrandingThemes/{branding_theme_id}/PaymentServices",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PaymentServices,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        payment_services: typing.Union[
            typing.Optional[typing.List[params.PaymentService]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentServices:
        """
        Creates a new custom payment service for a specific branding theme

        POST /BrandingThemes/{BrandingThemeID}/PaymentServices

        Args:
            payment_services: typing.List[PaymentService]
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PaymentServices array with newly created PaymentService

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.branding_themes.payment_services.create(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            payment_services=[
                {
                    "pay_now_text": "Time To Pay",
                    "payment_service_id": "54b3b4f6-0443-4fba-bcd1-61ec0c35ca55",
                    "payment_service_name": "PayUpNow",
                    "payment_service_type": "Custom",
                    "payment_service_url": "https://www.payupnow.com/",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"payment_services": payment_services},
            dump_with=params._SerializerPaymentServices,
        )
        return self._base_client.request(
            method="POST",
            path=f"/BrandingThemes/{branding_theme_id}/PaymentServices",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.PaymentServices,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentServicesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentServices:
        """
        Retrieves the payment services for a specific branding theme

        GET /BrandingThemes/{BrandingThemeID}/PaymentServices

        Args:
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PaymentServices array with 0 to N PaymentService

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.branding_themes.payment_services.list(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/BrandingThemes/{branding_theme_id}/PaymentServices",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.PaymentServices,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        branding_theme_id: str,
        xero_tenant_id: str,
        payment_services: typing.Union[
            typing.Optional[typing.List[params.PaymentService]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentServices:
        """
        Creates a new custom payment service for a specific branding theme

        POST /BrandingThemes/{BrandingThemeID}/PaymentServices

        Args:
            payment_services: typing.List[PaymentService]
            branding_theme_id: Unique identifier for a Branding Theme
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type PaymentServices array with newly created PaymentService

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.branding_themes.payment_services.create(
            branding_theme_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            payment_services=[
                {
                    "pay_now_text": "Time To Pay",
                    "payment_service_id": "54b3b4f6-0443-4fba-bcd1-61ec0c35ca55",
                    "payment_service_name": "PayUpNow",
                    "payment_service_type": "Custom",
                    "payment_service_url": "https://www.payupnow.com/",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"payment_services": payment_services},
            dump_with=params._SerializerPaymentServices,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/BrandingThemes/{branding_theme_id}/PaymentServices",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.PaymentServices,
            request_options=request_options or default_request_options(),
        )
