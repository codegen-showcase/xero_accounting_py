import pydantic
import typing
import typing_extensions

from .account import Account
from .line_item import LineItem
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact


class BankTransaction(pydantic.BaseModel):
    """
    BankTransaction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_account: Account = pydantic.Field(
        alias="BankAccount",
    )
    bank_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="BankTransactionID", default=None
    )
    """
    Xero generated unique identifier for bank transaction
    """
    contact: typing.Optional["Contact"] = pydantic.Field(alias="Contact", default=None)
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
    """
    3 letter alpha code for the currency – see list of currency codes
    """
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    """
    Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments.
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date of transaction – YYYY-MM-DD
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    Boolean to indicate if a bank transaction has an attachment
    """
    is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="IsReconciled", default=None
    )
    """
    Boolean to show if transaction is reconciled
    """
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """
    line_items: typing.List[LineItem] = pydantic.Field(
        alias="LineItems",
    )
    """
    See LineItems
    """
    overpayment_id: typing.Optional[str] = pydantic.Field(
        alias="OverpaymentID", default=None
    )
    """
    Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT
    """
    prepayment_id: typing.Optional[str] = pydantic.Field(
        alias="PrepaymentID", default=None
    )
    """
    Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    Reference for the transaction. Only supported for SPEND and RECEIVE transactions.
    """
    status: typing.Optional[
        typing_extensions.Literal["AUTHORISED", "DELETED", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Bank Transaction Status Codes
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    Total of bank transaction excluding taxes
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    Total of bank transaction tax inclusive
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    Total tax on bank transaction
    """
    type_: typing_extensions.Literal[
        "RECEIVE",
        "RECEIVE-OVERPAYMENT",
        "RECEIVE-PREPAYMENT",
        "RECEIVE-TRANSFER",
        "SPEND",
        "SPEND-OVERPAYMENT",
        "SPEND-PREPAYMENT",
        "SPEND-TRANSFER",
    ] = pydantic.Field(
        alias="Type",
    )
    """
    See Bank Transaction Types
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    URL link to a source document – shown as “Go to App Name”
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
