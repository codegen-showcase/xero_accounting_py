import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .line_item import LineItem, _SerializerLineItem
from .schedule import Schedule, _SerializerSchedule

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact


class RepeatingInvoice(typing_extensions.TypedDict):
    """
    RepeatingInvoice
    """

    approved_for_sending: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate whether the invoice has been approved for sending
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
    """

    branding_theme_id: typing_extensions.NotRequired[str]
    """
    See BrandingThemes
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

    has_attachments: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate if an invoice has an attachment
    """

    id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for repeating invoice template
    """

    include_pdf: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate whether to include PDF attachment
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    line_items: typing_extensions.NotRequired[typing.List[LineItem]]
    """
    See LineItems
    """

    mark_as_sent: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate whether the invoice in the Xero app displays as "sent"
    """

    reference: typing_extensions.NotRequired[str]
    """
    ACCREC only – additional reference number
    """

    repeating_invoice_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for repeating invoice template
    """

    schedule: typing_extensions.NotRequired[Schedule]

    send_copy: typing_extensions.NotRequired[bool]
    """
    Boolean to indicate whether a copy is sent to sender's email
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["AUTHORISED", "DELETED", "DRAFT"]
    ]
    """
    One of the following - DRAFT or AUTHORISED – See Invoice Status Codes
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    Total of invoice excluding taxes
    """

    total: typing_extensions.NotRequired[float]
    """
    Total of Invoice tax inclusive (i.e. SubTotal + TotalTax)
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    Total tax on invoice
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["ACCPAY", "ACCREC"]]
    """
    See Invoice Types
    """


class _SerializerRepeatingInvoice(pydantic.BaseModel):
    """
    Serializer for RepeatingInvoice handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    approved_for_sending: typing.Optional[bool] = pydantic.Field(
        alias="ApprovedForSending", default=None
    )
    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
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
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="ID", default=None)
    include_pdf: typing.Optional[bool] = pydantic.Field(
        alias="IncludePDF", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    mark_as_sent: typing.Optional[bool] = pydantic.Field(
        alias="MarkAsSent", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    repeating_invoice_id: typing.Optional[str] = pydantic.Field(
        alias="RepeatingInvoiceID", default=None
    )
    schedule: typing.Optional[_SerializerSchedule] = pydantic.Field(
        alias="Schedule", default=None
    )
    send_copy: typing.Optional[bool] = pydantic.Field(alias="SendCopy", default=None)
    status: typing.Optional[
        typing_extensions.Literal["AUTHORISED", "DELETED", "DRAFT"]
    ] = pydantic.Field(alias="Status", default=None)
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    type_: typing.Optional[typing_extensions.Literal["ACCPAY", "ACCREC"]] = (
        pydantic.Field(alias="Type", default=None)
    )
