import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError, _SerializerValidationError


class Account(typing_extensions.TypedDict):
    """
    Account
    """

    account_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    add_to_watchlist: typing_extensions.NotRequired[bool]
    """
    Boolean – describes whether the account is shown in the watchlist widget on the dashboard
    """

    bank_account_number: typing_extensions.NotRequired[str]
    """
    For bank accounts only (Account Type BANK)
    """

    bank_account_type: typing_extensions.NotRequired[
        typing_extensions.Literal["BANK", "CREDITCARD", "NONE", "PAYPAL"]
    ]
    """
    For bank accounts only. See Bank Account types
    """

    class_: typing_extensions.NotRequired[
        typing_extensions.Literal["ASSET", "EQUITY", "EXPENSE", "LIABILITY", "REVENUE"]
    ]
    """
    See Account Class Types
    """

    code: typing_extensions.NotRequired[str]
    """
    Customer defined alpha numeric account code e.g 200 or SALES (max length = 10)
    """

    currency_code: typing_extensions.NotRequired[
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
    ]
    """
    3 letter alpha code for the currency – see list of currency codes
    """

    description: typing_extensions.NotRequired[str]
    """
    Description of the Account. Valid for all types of accounts except bank accounts (max length = 4000)
    """

    enable_payments_to_account: typing_extensions.NotRequired[bool]
    """
    Boolean – describes whether account can have payments applied to it
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if an account has an attachment (read only)
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of account (max length = 150)
    """

    reporting_code: typing_extensions.NotRequired[str]
    """
    Shown if set
    """

    reporting_code_name: typing_extensions.NotRequired[str]
    """
    Shown if set
    """

    show_in_expense_claims: typing_extensions.NotRequired[bool]
    """
    Boolean – describes whether account code is available for use with expense claims
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ]
    """
    Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes
    """

    system_account: typing_extensions.NotRequired[
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
    ]
    """
    If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null.
    """

    tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from taxRates
    """

    type_: typing_extensions.NotRequired[
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
    ]
    """
    See Account Types
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerAccount(pydantic.BaseModel):
    """
    Serializer for Account handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="AccountID", default=None)
    add_to_watchlist: typing.Optional[bool] = pydantic.Field(
        alias="AddToWatchlist", default=None
    )
    bank_account_number: typing.Optional[str] = pydantic.Field(
        alias="BankAccountNumber", default=None
    )
    bank_account_type: typing.Optional[
        typing_extensions.Literal["BANK", "CREDITCARD", "NONE", "PAYPAL"]
    ] = pydantic.Field(alias="BankAccountType", default=None)
    class_: typing.Optional[
        typing_extensions.Literal["ASSET", "EQUITY", "EXPENSE", "LIABILITY", "REVENUE"]
    ] = pydantic.Field(alias="Class", default=None)
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    currency_code: typing.Optional[
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
    ] = pydantic.Field(alias="CurrencyCode", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    enable_payments_to_account: typing.Optional[bool] = pydantic.Field(
        alias="EnablePaymentsToAccount", default=None
    )
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    reporting_code: typing.Optional[str] = pydantic.Field(
        alias="ReportingCode", default=None
    )
    reporting_code_name: typing.Optional[str] = pydantic.Field(
        alias="ReportingCodeName", default=None
    )
    show_in_expense_claims: typing.Optional[bool] = pydantic.Field(
        alias="ShowInExpenseClaims", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ] = pydantic.Field(alias="Status", default=None)
    system_account: typing.Optional[
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
    ] = pydantic.Field(alias="SystemAccount", default=None)
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    type_: typing.Optional[
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
    ] = pydantic.Field(alias="Type", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
