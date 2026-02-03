import pydantic
import typing
import typing_extensions

from .line_item import LineItem
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact


class Quote(pydantic.BaseModel):
    """
    Quote
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
    )
    """
    See BrandingThemes
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
    The currency rate for a multicurrency quote
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date quote was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation
    """
    date_string: typing.Optional[str] = pydantic.Field(alias="DateString", default=None)
    """
    Date the quote was issued (YYYY-MM-DD)
    """
    expiry_date: typing.Optional[str] = pydantic.Field(alias="ExpiryDate", default=None)
    """
    Date the quote expires – YYYY-MM-DD.
    """
    expiry_date_string: typing.Optional[str] = pydantic.Field(
        alias="ExpiryDateString", default=None
    )
    """
    Date the quote expires – YYYY-MM-DD.
    """
    line_amount_types: typing.Optional[
        typing_extensions.Literal["EXCLUSIVE", "INCLUSIVE", "NOTAX"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """
    line_items: typing.Optional[typing.List[LineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    """
    See LineItems
    """
    quote_id: typing.Optional[str] = pydantic.Field(alias="QuoteID", default=None)
    """
    QuoteID GUID is automatically generated and is returned after create or GET.
    """
    quote_number: typing.Optional[str] = pydantic.Field(
        alias="QuoteNumber", default=None
    )
    """
    Unique alpha numeric code identifying a quote (Max Length = 255)
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    Additional reference number
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "ACCEPTED", "DECLINED", "DELETED", "DRAFT", "INVOICED", "SENT"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    """
    The status of the quote.
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    Total of quote excluding taxes.
    """
    summary: typing.Optional[str] = pydantic.Field(alias="Summary", default=None)
    """
    Summary text for the quote
    """
    terms: typing.Optional[str] = pydantic.Field(alias="Terms", default=None)
    """
    Terms of the quote
    """
    title: typing.Optional[str] = pydantic.Field(alias="Title", default=None)
    """
    Title text for the quote
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    Total of Quote tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts
    """
    total_discount: typing.Optional[float] = pydantic.Field(
        alias="TotalDiscount", default=None
    )
    """
    Total of discounts applied on the quote line items
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    Total tax on quote
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
