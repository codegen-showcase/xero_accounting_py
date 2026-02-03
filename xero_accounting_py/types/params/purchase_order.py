import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .line_item import LineItem, _SerializerLineItem
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact


class PurchaseOrder(typing_extensions.TypedDict):
    """
    PurchaseOrder
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
    """

    attention_to: typing_extensions.NotRequired[str]
    """
    The person that the delivery is going to
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

    currency_rate: typing_extensions.NotRequired[float]
    """
    The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used.
    """

    date: typing_extensions.NotRequired[str]
    """
    Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation
    """

    delivery_address: typing_extensions.NotRequired[str]
    """
    The address the goods are to be delivered to
    """

    delivery_date: typing_extensions.NotRequired[str]
    """
    Date the goods are to be delivered – YYYY-MM-DD
    """

    delivery_instructions: typing_extensions.NotRequired[str]
    """
    A free text feild for instructions (500 characters max)
    """

    expected_arrival_date: typing_extensions.NotRequired[str]
    """
    The date the goods are expected to arrive.
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if a purchase order has an attachment
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

    purchase_order_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for purchase order
    """

    purchase_order_number: typing_extensions.NotRequired[str]
    """
    Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings)
    """

    reference: typing_extensions.NotRequired[str]
    """
    Additional reference number
    """

    sent_to_contact: typing_extensions.NotRequired[bool]
    """
    Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
        ]
    ]
    """
    See Purchase Order Status Codes
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    Total of purchase order excluding taxes
    """

    telephone: typing_extensions.NotRequired[str]
    """
    The phone number for the person accepting the delivery
    """

    total: typing_extensions.NotRequired[float]
    """
    Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax)
    """

    total_discount: typing_extensions.NotRequired[float]
    """
    Total of discounts applied on the purchase order line items
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    Total tax on purchase order
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerPurchaseOrder(pydantic.BaseModel):
    """
    Serializer for PurchaseOrder handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    attention_to: typing.Optional[str] = pydantic.Field(
        alias="AttentionTo", default=None
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
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    delivery_address: typing.Optional[str] = pydantic.Field(
        alias="DeliveryAddress", default=None
    )
    delivery_date: typing.Optional[str] = pydantic.Field(
        alias="DeliveryDate", default=None
    )
    delivery_instructions: typing.Optional[str] = pydantic.Field(
        alias="DeliveryInstructions", default=None
    )
    expected_arrival_date: typing.Optional[str] = pydantic.Field(
        alias="ExpectedArrivalDate", default=None
    )
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    purchase_order_id: typing.Optional[str] = pydantic.Field(
        alias="PurchaseOrderID", default=None
    )
    purchase_order_number: typing.Optional[str] = pydantic.Field(
        alias="PurchaseOrderNumber", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    sent_to_contact: typing.Optional[bool] = pydantic.Field(
        alias="SentToContact", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "BILLED", "DELETED", "DRAFT", "SUBMITTED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    telephone: typing.Optional[str] = pydantic.Field(alias="Telephone", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    total_discount: typing.Optional[float] = pydantic.Field(
        alias="TotalDiscount", default=None
    )
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
