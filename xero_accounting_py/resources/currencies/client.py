import typing
import typing_extensions

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


class CurrenciesClient:
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
    ) -> models.Currencies:
        """
        Retrieves currencies for your Xero organisation

        GET /Currencies

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Currencies array with all Currencies

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.currencies.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID", order="Code ASC", where='Code=="USD"'
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
            path="/Currencies",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Currencies,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        code: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AED",
                    "AFN",
                    "ALL",
                    "AMD",
                    "ANG",
                    "AOA",
                    "ARS",
                    "AUD",
                    "AWG",
                    "AZN",
                    "BAM",
                    "BBD",
                    "BDT",
                    "BGN",
                    "BHD",
                    "BIF",
                    "BMD",
                    "BND",
                    "BOB",
                    "BRL",
                    "BSD",
                    "BTN",
                    "BWP",
                    "BYN",
                    "BYR",
                    "BZD",
                    "CAD",
                    "CDF",
                    "CHF",
                    "CLF",
                    "CLP",
                    "CNY",
                    "COP",
                    "CRC",
                    "CUC",
                    "CUP",
                    "CVE",
                    "CZK",
                    "DJF",
                    "DKK",
                    "DOP",
                    "DZD",
                    "EEK",
                    "EGP",
                    "ERN",
                    "ETB",
                    "EUR",
                    "FJD",
                    "FKP",
                    "GBP",
                    "GEL",
                    "GHS",
                    "GIP",
                    "GMD",
                    "GNF",
                    "GTQ",
                    "GYD",
                    "HKD",
                    "HNL",
                    "HRK",
                    "HTG",
                    "HUF",
                    "IDR",
                    "ILS",
                    "INR",
                    "IQD",
                    "IRR",
                    "ISK",
                    "JMD",
                    "JOD",
                    "JPY",
                    "KES",
                    "KGS",
                    "KHR",
                    "KMF",
                    "KPW",
                    "KRW",
                    "KWD",
                    "KYD",
                    "KZT",
                    "LAK",
                    "LBP",
                    "LKR",
                    "LRD",
                    "LSL",
                    "LTL",
                    "LVL",
                    "LYD",
                    "MAD",
                    "MDL",
                    "MGA",
                    "MKD",
                    "MMK",
                    "MNT",
                    "MOP",
                    "MRO",
                    "MRU",
                    "MUR",
                    "MVR",
                    "MWK",
                    "MXN",
                    "MXV",
                    "MYR",
                    "MZN",
                    "NAD",
                    "NGN",
                    "NIO",
                    "NOK",
                    "NPR",
                    "NZD",
                    "OMR",
                    "PAB",
                    "PEN",
                    "PGK",
                    "PHP",
                    "PKR",
                    "PLN",
                    "PYG",
                    "QAR",
                    "RON",
                    "RSD",
                    "RUB",
                    "RWF",
                    "SAR",
                    "SBD",
                    "SCR",
                    "SDG",
                    "SEK",
                    "SGD",
                    "SHP",
                    "SKK",
                    "SLE",
                    "SLL",
                    "SOS",
                    "SRD",
                    "STD",
                    "STN",
                    "SVC",
                    "SYP",
                    "SZL",
                    "THB",
                    "TJS",
                    "TMT",
                    "TND",
                    "TOP",
                    "TRY",
                    "TTD",
                    "TWD",
                    "TZS",
                    "UAH",
                    "UGX",
                    "USD",
                    "UYU",
                    "UZS",
                    "VEF",
                    "VES",
                    "VND",
                    "VUV",
                    "WST",
                    "XAF",
                    "XCD",
                    "XOF",
                    "XPF",
                    "YER",
                    "ZAR",
                    "ZMK",
                    "ZMW",
                    "ZWD",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Currencies:
        """
        Create a new currency for a Xero organisation

        PUT /Currencies

        Args:
            code: 3 letter alpha code for the currency – see list of currency codes
            description: Name of Currency
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Unsupported - return response incorrect exception, API is not able to create new Currency

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.currencies.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            code="USD",
            description="United States Dollar",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"code": code, "description": description},
            dump_with=params._SerializerCurrency,
        )
        return self._base_client.request(
            method="PUT",
            path="/Currencies",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Currencies,
            request_options=request_options or default_request_options(),
        )


class AsyncCurrenciesClient:
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
    ) -> models.Currencies:
        """
        Retrieves currencies for your Xero organisation

        GET /Currencies

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Currencies array with all Currencies

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.currencies.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID", order="Code ASC", where='Code=="USD"'
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
            path="/Currencies",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Currencies,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        code: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "AED",
                    "AFN",
                    "ALL",
                    "AMD",
                    "ANG",
                    "AOA",
                    "ARS",
                    "AUD",
                    "AWG",
                    "AZN",
                    "BAM",
                    "BBD",
                    "BDT",
                    "BGN",
                    "BHD",
                    "BIF",
                    "BMD",
                    "BND",
                    "BOB",
                    "BRL",
                    "BSD",
                    "BTN",
                    "BWP",
                    "BYN",
                    "BYR",
                    "BZD",
                    "CAD",
                    "CDF",
                    "CHF",
                    "CLF",
                    "CLP",
                    "CNY",
                    "COP",
                    "CRC",
                    "CUC",
                    "CUP",
                    "CVE",
                    "CZK",
                    "DJF",
                    "DKK",
                    "DOP",
                    "DZD",
                    "EEK",
                    "EGP",
                    "ERN",
                    "ETB",
                    "EUR",
                    "FJD",
                    "FKP",
                    "GBP",
                    "GEL",
                    "GHS",
                    "GIP",
                    "GMD",
                    "GNF",
                    "GTQ",
                    "GYD",
                    "HKD",
                    "HNL",
                    "HRK",
                    "HTG",
                    "HUF",
                    "IDR",
                    "ILS",
                    "INR",
                    "IQD",
                    "IRR",
                    "ISK",
                    "JMD",
                    "JOD",
                    "JPY",
                    "KES",
                    "KGS",
                    "KHR",
                    "KMF",
                    "KPW",
                    "KRW",
                    "KWD",
                    "KYD",
                    "KZT",
                    "LAK",
                    "LBP",
                    "LKR",
                    "LRD",
                    "LSL",
                    "LTL",
                    "LVL",
                    "LYD",
                    "MAD",
                    "MDL",
                    "MGA",
                    "MKD",
                    "MMK",
                    "MNT",
                    "MOP",
                    "MRO",
                    "MRU",
                    "MUR",
                    "MVR",
                    "MWK",
                    "MXN",
                    "MXV",
                    "MYR",
                    "MZN",
                    "NAD",
                    "NGN",
                    "NIO",
                    "NOK",
                    "NPR",
                    "NZD",
                    "OMR",
                    "PAB",
                    "PEN",
                    "PGK",
                    "PHP",
                    "PKR",
                    "PLN",
                    "PYG",
                    "QAR",
                    "RON",
                    "RSD",
                    "RUB",
                    "RWF",
                    "SAR",
                    "SBD",
                    "SCR",
                    "SDG",
                    "SEK",
                    "SGD",
                    "SHP",
                    "SKK",
                    "SLE",
                    "SLL",
                    "SOS",
                    "SRD",
                    "STD",
                    "STN",
                    "SVC",
                    "SYP",
                    "SZL",
                    "THB",
                    "TJS",
                    "TMT",
                    "TND",
                    "TOP",
                    "TRY",
                    "TTD",
                    "TWD",
                    "TZS",
                    "UAH",
                    "UGX",
                    "USD",
                    "UYU",
                    "UZS",
                    "VEF",
                    "VES",
                    "VND",
                    "VUV",
                    "WST",
                    "XAF",
                    "XCD",
                    "XOF",
                    "XPF",
                    "YER",
                    "ZAR",
                    "ZMK",
                    "ZMW",
                    "ZWD",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Currencies:
        """
        Create a new currency for a Xero organisation

        PUT /Currencies

        Args:
            code: 3 letter alpha code for the currency – see list of currency codes
            description: Name of Currency
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Unsupported - return response incorrect exception, API is not able to create new Currency

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.currencies.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            code="USD",
            description="United States Dollar",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"code": code, "description": description},
            dump_with=params._SerializerCurrency,
        )
        return await self._base_client.request(
            method="PUT",
            path="/Currencies",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Currencies,
            request_options=request_options or default_request_options(),
        )
