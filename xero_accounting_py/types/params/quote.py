import pydantic
import typing
import typing_extensions

from .line_item import LineItem, _SerializerLineItem
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact


class Quote(typing_extensions.TypedDict):
    """
    Quote
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
    The currency rate for a multicurrency quote
    """

    date: typing_extensions.NotRequired[str]
    """
    Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation
    """

    date_string: typing_extensions.NotRequired[str]
    """
    Date the quote was issued (YYYY-MM-DD)
    """

    expiry_date: typing_extensions.NotRequired[str]
    """
    Date the quote expires – YYYY-MM-DD.
    """

    expiry_date_string: typing_extensions.NotRequired[str]
    """
    Date the quote expires – YYYY-MM-DD.
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NOTAX"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    line_items: typing_extensions.NotRequired[typing.List[LineItem]]
    """
    See LineItems
    """

    quote_id: typing_extensions.NotRequired[str]
    """
    QuoteID GUID is automatically generated and is returned after create or GET.
    """

    quote_number: typing_extensions.NotRequired[str]
    """
    Unique alpha numeric code identifying a quote (Max Length = 255)
    """

    reference: typing_extensions.NotRequired[str]
    """
    Additional reference number
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ACCEPTED", "DECLINED", "DELETED", "DRAFT", "INVOICED", "SENT"
        ]
    ]
    """
    The status of the quote.
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    Total of quote excluding taxes.
    """

    summary: typing_extensions.NotRequired[str]
    """
    Summary text for the quote
    """

    terms: typing_extensions.NotRequired[str]
    """
    Terms of the quote
    """

    title: typing_extensions.NotRequired[str]
    """
    Title text for the quote
    """

    total: typing_extensions.NotRequired[float]
    """
    Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts
    """

    total_discount: typing_extensions.NotRequired[float]
    """
    Total of discounts applied on the quote line items
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    Total tax on quote
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerQuote(pydantic.BaseModel):
    """
    Serializer for Quote handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
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
    date_string: typing.Optional[str] = pydantic.Field(alias="DateString", default=None)
    expiry_date: typing.Optional[str] = pydantic.Field(alias="ExpiryDate", default=None)
    expiry_date_string: typing.Optional[str] = pydantic.Field(
        alias="ExpiryDateString", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NOTAX"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    quote_id: typing.Optional[str] = pydantic.Field(alias="QuoteID", default=None)
    quote_number: typing.Optional[str] = pydantic.Field(
        alias="QuoteNumber", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    status: typing.Optional[
        typing_extensions.Literal[
            "ACCEPTED", "DECLINED", "DELETED", "DRAFT", "INVOICED", "SENT"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    summary: typing.Optional[str] = pydantic.Field(alias="Summary", default=None)
    terms: typing.Optional[str] = pydantic.Field(alias="Terms", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="Title", default=None)
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
