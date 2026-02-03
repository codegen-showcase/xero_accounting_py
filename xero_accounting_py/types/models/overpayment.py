import pydantic
import typing
import typing_extensions

from .attachment import Attachment
from .line_item import LineItem

if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation
    from .contact import Contact
    from .payment import Payment


class Overpayment(pydantic.BaseModel):
    """
    Overpayment
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allocations: typing.Optional[typing.List["Allocation"]] = pydantic.Field(
        alias="Allocations", default=None
    )
    """
    See Allocations
    """
    applied_amount: typing.Optional[float] = pydantic.Field(
        alias="AppliedAmount", default=None
    )
    """
    The amount of applied to an invoice
    """
    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    """
    See Attachments
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
    The currency rate for a multicurrency overpayment. If no rate is specified, the XE.com day rate is used
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    The date the overpayment is created YYYY-MM-DD
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    boolean to indicate if a overpayment has an attachment
    """
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """
    line_items: typing.Optional[typing.List[LineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    """
    See Overpayment Line Items
    """
    overpayment_id: typing.Optional[str] = pydantic.Field(
        alias="OverpaymentID", default=None
    )
    """
    Xero generated unique identifier
    """
    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    """
    See Payments
    """
    remaining_credit: typing.Optional[float] = pydantic.Field(
        alias="RemainingCredit", default=None
    )
    """
    The remaining credit balance on the overpayment
    """
    status: typing.Optional[
        typing_extensions.Literal["AUTHORISED", "PAID", "VOIDED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Overpayment Status Codes
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    The subtotal of the overpayment excluding taxes
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    The total of the overpayment (subtotal + total tax)
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    The total tax on the overpayment
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "AROVERPAYMENT", "RECEIVE-OVERPAYMENT", "SPEND-OVERPAYMENT"
        ]
    ] = pydantic.Field(alias="Type", default=None)
    """
    See Overpayment Types
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    UTC timestamp of last update to the overpayment
    """
