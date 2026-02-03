import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .line_item import LineItem, _SerializerLineItem

if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation, _SerializerAllocation
    from .contact import Contact, _SerializerContact
    from .payment import Payment, _SerializerPayment


class Prepayment(typing_extensions.TypedDict):
    """
    Prepayment
    """

    allocations: typing_extensions.NotRequired[typing.List["Allocation"]]
    """
    See Allocations
    """

    applied_amount: typing_extensions.NotRequired[float]
    """
    The amount of applied to an invoice
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    See Attachments
    """

    contact: typing_extensions.NotRequired["Contact"]

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

    currency_rate: typing_extensions.NotRequired[float]
    """
    The currency rate for a multicurrency prepayment. If no rate is specified, the XE.com day rate is used
    """

    date: typing_extensions.NotRequired[str]
    """
    The date the prepayment is created YYYY-MM-DD
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if a prepayment has an attachment
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    line_items: typing_extensions.NotRequired[typing.List[LineItem]]
    """
    See Prepayment Line Items
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]
    """
    See Payments
    """

    prepayment_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier
    """

    reference: typing_extensions.NotRequired[str]
    """
    Returns Invoice number field. Reference field isn't available.
    """

    remaining_credit: typing_extensions.NotRequired[float]
    """
    The remaining credit balance on the prepayment
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["AUTHORISED", "PAID", "VOIDED"]
    ]
    """
    See Prepayment Status Codes
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    The subtotal of the prepayment excluding taxes
    """

    total: typing_extensions.NotRequired[float]
    """
    The total of the prepayment(subtotal + total tax)
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    The total tax on the prepayment
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "APPREPAYMENT", "ARPREPAYMENT", "RECEIVE-PREPAYMENT", "SPEND-PREPAYMENT"
        ]
    ]
    """
    See Prepayment Types
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of last update to the prepayment
    """


class _SerializerPrepayment(pydantic.BaseModel):
    """
    Serializer for Prepayment handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allocations: typing.Optional[typing.List["_SerializerAllocation"]] = pydantic.Field(
        alias="Allocations", default=None
    )
    applied_amount: typing.Optional[float] = pydantic.Field(
        alias="AppliedAmount", default=None
    )
    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    contact: typing.Optional["_SerializerContact"] = pydantic.Field(
        alias="Contact", default=None
    )
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
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    payments: typing.Optional[typing.List["_SerializerPayment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    prepayment_id: typing.Optional[str] = pydantic.Field(
        alias="PrepaymentID", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    remaining_credit: typing.Optional[float] = pydantic.Field(
        alias="RemainingCredit", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["AUTHORISED", "PAID", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "APPREPAYMENT", "ARPREPAYMENT", "RECEIVE-PREPAYMENT", "SPEND-PREPAYMENT"
        ]
    ] = pydantic.Field(alias="Type", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
