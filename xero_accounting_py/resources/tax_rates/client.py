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
from xero_accounting_py.types import models, params


class TaxRatesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
    ) -> models.TaxRates:
        """
        Retrieves tax rates

        GET /TaxRates

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array with TaxRates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rates.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
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
            path="/TaxRates",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        tax_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Retrieves a specific tax rate according to given TaxType code

        GET /TaxRates/{TaxType}

        Args:
            tax_type: A valid TaxType code
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array with one TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rates.get(tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/TaxRates/{tax_type}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        xero_tenant_id: str,
        tax_rates: typing.Union[
            typing.Optional[typing.List[params.TaxRate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Updates tax rates

        POST /TaxRates

        Args:
            tax_rates: typing.List[TaxRate]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array updated TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rates.update(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            tax_rates=[
                {
                    "name": "State Tax NY",
                    "report_tax_type": "INPUT",
                    "status": "DELETED",
                    "tax_components": [{"name": "State Tax", "rate": 2.25}],
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"tax_rates": tax_rates}, dump_with=params._SerializerTaxRates
        )
        return self._base_client.request(
            method="POST",
            path="/TaxRates",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        tax_rates: typing.Union[
            typing.Optional[typing.List[params.TaxRate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Creates one or more tax rates

        PUT /TaxRates

        Args:
            tax_rates: typing.List[TaxRate]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array newly created TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax_rates.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            tax_rates=[
                {
                    "name": "CA State Tax",
                    "tax_components": [{"name": "State Tax", "rate": 2.25}],
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"tax_rates": tax_rates}, dump_with=params._SerializerTaxRates
        )
        return self._base_client.request(
            method="PUT",
            path="/TaxRates",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )


class AsyncTaxRatesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
    ) -> models.TaxRates:
        """
        Retrieves tax rates

        GET /TaxRates

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array with TaxRates

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rates.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where='Status=="ACTIVE"',
        )
        ```
        """
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
            path="/TaxRates",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        tax_type: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Retrieves a specific tax rate according to given TaxType code

        GET /TaxRates/{TaxType}

        Args:
            tax_type: A valid TaxType code
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array with one TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rates.get(
            tax_type="INPUT2", xero_tenant_id="YOUR_XERO_TENANT_ID"
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/TaxRates/{tax_type}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        xero_tenant_id: str,
        tax_rates: typing.Union[
            typing.Optional[typing.List[params.TaxRate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Updates tax rates

        POST /TaxRates

        Args:
            tax_rates: typing.List[TaxRate]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array updated TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rates.update(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            tax_rates=[
                {
                    "name": "State Tax NY",
                    "report_tax_type": "INPUT",
                    "status": "DELETED",
                    "tax_components": [{"name": "State Tax", "rate": 2.25}],
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"tax_rates": tax_rates}, dump_with=params._SerializerTaxRates
        )
        return await self._base_client.request(
            method="POST",
            path="/TaxRates",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        tax_rates: typing.Union[
            typing.Optional[typing.List[params.TaxRate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRates:
        """
        Creates one or more tax rates

        PUT /TaxRates

        Args:
            tax_rates: typing.List[TaxRate]
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type TaxRates array newly created TaxRate

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax_rates.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            tax_rates=[
                {
                    "name": "CA State Tax",
                    "tax_components": [{"name": "State Tax", "rate": 2.25}],
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"tax_rates": tax_rates}, dump_with=params._SerializerTaxRates
        )
        return await self._base_client.request(
            method="PUT",
            path="/TaxRates",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.TaxRates,
            request_options=request_options or default_request_options(),
        )
