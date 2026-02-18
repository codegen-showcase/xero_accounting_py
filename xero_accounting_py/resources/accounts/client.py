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
from xero_accounting_py.resources.accounts.attachments import (
    AsyncAttachmentsClient,
    AttachmentsClient,
)
from xero_accounting_py.types import models, params


class AccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.attachments = AttachmentsClient(base_client=self._base_client)

    def delete(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Deletes a chart of accounts

        DELETE /Accounts/{AccountID}

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - delete existing Account and return response of type Accounts array with deleted Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.delete(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="DELETE",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.Accounts:
        """
        Retrieves the full chart of accounts

        GET /Accounts

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Accounts array with 0 to n Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
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
            path="/Accounts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Retrieves a single chart of accounts by using a unique account Id

        GET /Accounts/{AccountID}

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Accounts array with one Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.get(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        accounts: typing.Union[
            typing.Optional[typing.List[params.Account]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Updates a chart of accounts

        POST /Accounts/{AccountID}

        Args:
            accounts: typing.List[Account]
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - update existing Account and return response of type Accounts array with updated Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.update(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            accounts=[
                {
                    "account_id": "99ce6032-0678-4aa0-8148-240c75fee33a",
                    "class_": "EXPENSE",
                    "code": "123456",
                    "description": "GoodBye World",
                    "enable_payments_to_account": False,
                    "name": "BarFoo",
                    "reporting_code": "EXP",
                    "reporting_code_name": "Expense",
                    "show_in_expense_claims": False,
                    "tax_type": "INPUT",
                    "type_": "EXPENSE",
                    "updated_date_utc": "2019-02-21T16:29:47.96-08:00",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"accounts": accounts}, dump_with=params._SerializerAccounts
        )
        return self._base_client.request(
            method="POST",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        add_to_watchlist: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["BANK", "CREDITCARD", "NONE", "PAYPAL"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        class_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ASSET", "EQUITY", "EXPENSE", "LIABILITY", "REVENUE"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency_code: typing.Union[
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
        enable_payments_to_account: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_attachments: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reporting_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reporting_code_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        show_in_expense_claims: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        system_account: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "BANKCURRENCYGAIN",
                    "CISASSET",
                    "CISASSETS",
                    "CISLABOUR",
                    "CISLABOUREXPENSE",
                    "CISLABOURINCOME",
                    "CISLIABILITY",
                    "CISMATERIALS",
                    "CREDITORS",
                    "DEBTORS",
                    "GST",
                    "GSTONIMPORTS",
                    "HISTORICAL",
                    "REALISEDCURRENCYGAIN",
                    "RETAINEDEARNINGS",
                    "ROUNDING",
                    "TRACKINGTRANSFERS",
                    "UNPAIDEXPCLM",
                    "UNREALISEDCURRENCYGAIN",
                    "WAGEPAYABLES",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "BANK",
                    "CURRENT",
                    "CURRLIAB",
                    "DEPRECIATN",
                    "DIRECTCOSTS",
                    "EQUITY",
                    "EXPENSE",
                    "FIXED",
                    "INVENTORY",
                    "LIABILITY",
                    "NONCURRENT",
                    "OTHERINCOME",
                    "OVERHEADS",
                    "PAYG",
                    "PREPAYMENT",
                    "REVENUE",
                    "SALES",
                    "TERMLIAB",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Creates a new chart of accounts

        PUT /Accounts

        Args:
            account_id: The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9
            add_to_watchlist: Boolean – describes whether the account is shown in the watchlist widget on the dashboard
            bank_account_number: For bank accounts only (Account Type BANK)
            bank_account_type: For bank accounts only. See Bank Account types
            class_: See Account Class Types
            code: Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)
            currency_code: 3 letter alpha code for the currency – see list of currency codes
            description: Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)
            enable_payments_to_account: Boolean – describes whether account can have payments applied to it
            has_attachments: boolean to indicate if an account has an attachment (read only)
            name: Name of account (max length = 150)
            reporting_code: Shown if set
            reporting_code_name: Shown if set
            show_in_expense_claims: Boolean – describes whether account code is available for use with expense claims
            status: Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes
            system_account: If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null.
            tax_type: The tax type from taxRates
            type_: See Account Types
            updated_date_utc: Last modified date UTC format
            validation_errors: Displays array of validation error messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - created new Account and return response of type Accounts array with new Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            account_id="00000000-0000-0000-0000-000000000000",
            code="123456",
            description="Hello World",
            has_attachments=False,
            name="Foobar",
            type_="EXPENSE",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "account_id": account_id,
                "add_to_watchlist": add_to_watchlist,
                "bank_account_number": bank_account_number,
                "bank_account_type": bank_account_type,
                "class_": class_,
                "code": code,
                "currency_code": currency_code,
                "description": description,
                "enable_payments_to_account": enable_payments_to_account,
                "has_attachments": has_attachments,
                "name": name,
                "reporting_code": reporting_code,
                "reporting_code_name": reporting_code_name,
                "show_in_expense_claims": show_in_expense_claims,
                "status": status,
                "system_account": system_account,
                "tax_type": tax_type,
                "type_": type_,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
            },
            dump_with=params._SerializerAccount,
        )
        return self._base_client.request(
            method="PUT",
            path="/Accounts",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.attachments = AsyncAttachmentsClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Deletes a chart of accounts

        DELETE /Accounts/{AccountID}

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - delete existing Account and return response of type Accounts array with deleted Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.delete(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="DELETE",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.Accounts:
        """
        Retrieves the full chart of accounts

        GET /Accounts

        Args:
            order: Order by an any element
            where: Filter by an any element
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Accounts array with 0 to n Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            order="Name ASC",
            where="Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;",
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
            path="/Accounts",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Retrieves a single chart of accounts by using a unique account Id

        GET /Accounts/{AccountID}

        Args:
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Accounts array with one Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.get(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        account_id: str,
        xero_tenant_id: str,
        accounts: typing.Union[
            typing.Optional[typing.List[params.Account]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Updates a chart of accounts

        POST /Accounts/{AccountID}

        Args:
            accounts: typing.List[Account]
            account_id: Unique identifier for Account object
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - update existing Account and return response of type Accounts array with updated Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.update(
            account_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            accounts=[
                {
                    "account_id": "99ce6032-0678-4aa0-8148-240c75fee33a",
                    "class_": "EXPENSE",
                    "code": "123456",
                    "description": "GoodBye World",
                    "enable_payments_to_account": False,
                    "name": "BarFoo",
                    "reporting_code": "EXP",
                    "reporting_code_name": "Expense",
                    "show_in_expense_claims": False,
                    "tax_type": "INPUT",
                    "type_": "EXPENSE",
                    "updated_date_utc": "2019-02-21T16:29:47.96-08:00",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"accounts": accounts}, dump_with=params._SerializerAccounts
        )
        return await self._base_client.request(
            method="POST",
            path=f"/Accounts/{account_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        account_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        add_to_watchlist: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_number: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bank_account_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["BANK", "CREDITCARD", "NONE", "PAYPAL"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        class_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "ASSET", "EQUITY", "EXPENSE", "LIABILITY", "REVENUE"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        currency_code: typing.Union[
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
        enable_payments_to_account: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        has_attachments: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reporting_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reporting_code_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        show_in_expense_claims: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        system_account: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "BANKCURRENCYGAIN",
                    "CISASSET",
                    "CISASSETS",
                    "CISLABOUR",
                    "CISLABOUREXPENSE",
                    "CISLABOURINCOME",
                    "CISLIABILITY",
                    "CISMATERIALS",
                    "CREDITORS",
                    "DEBTORS",
                    "GST",
                    "GSTONIMPORTS",
                    "HISTORICAL",
                    "REALISEDCURRENCYGAIN",
                    "RETAINEDEARNINGS",
                    "ROUNDING",
                    "TRACKINGTRANSFERS",
                    "UNPAIDEXPCLM",
                    "UNREALISEDCURRENCYGAIN",
                    "WAGEPAYABLES",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "BANK",
                    "CURRENT",
                    "CURRLIAB",
                    "DEPRECIATN",
                    "DIRECTCOSTS",
                    "EQUITY",
                    "EXPENSE",
                    "FIXED",
                    "INVENTORY",
                    "LIABILITY",
                    "NONCURRENT",
                    "OTHERINCOME",
                    "OVERHEADS",
                    "PAYG",
                    "PREPAYMENT",
                    "REVENUE",
                    "SALES",
                    "TERMLIAB",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Accounts:
        """
        Creates a new chart of accounts

        PUT /Accounts

        Args:
            account_id: The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9
            add_to_watchlist: Boolean – describes whether the account is shown in the watchlist widget on the dashboard
            bank_account_number: For bank accounts only (Account Type BANK)
            bank_account_type: For bank accounts only. See Bank Account types
            class_: See Account Class Types
            code: Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)
            currency_code: 3 letter alpha code for the currency – see list of currency codes
            description: Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)
            enable_payments_to_account: Boolean – describes whether account can have payments applied to it
            has_attachments: boolean to indicate if an account has an attachment (read only)
            name: Name of account (max length = 150)
            reporting_code: Shown if set
            reporting_code_name: Shown if set
            show_in_expense_claims: Boolean – describes whether account code is available for use with expense claims
            status: Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes
            system_account: If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null.
            tax_type: The tax type from taxRates
            type_: See Account Types
            updated_date_utc: Last modified date UTC format
            validation_errors: Displays array of validation error messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - created new Account and return response of type Accounts array with new Account

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            account_id="00000000-0000-0000-0000-000000000000",
            code="123456",
            description="Hello World",
            has_attachments=False,
            name="Foobar",
            type_="EXPENSE",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "account_id": account_id,
                "add_to_watchlist": add_to_watchlist,
                "bank_account_number": bank_account_number,
                "bank_account_type": bank_account_type,
                "class_": class_,
                "code": code,
                "currency_code": currency_code,
                "description": description,
                "enable_payments_to_account": enable_payments_to_account,
                "has_attachments": has_attachments,
                "name": name,
                "reporting_code": reporting_code,
                "reporting_code_name": reporting_code_name,
                "show_in_expense_claims": show_in_expense_claims,
                "status": status,
                "system_account": system_account,
                "tax_type": tax_type,
                "type_": type_,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
            },
            dump_with=params._SerializerAccount,
        )
        return await self._base_client.request(
            method="PUT",
            path="/Accounts",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.Accounts,
            request_options=request_options or default_request_options(),
        )
