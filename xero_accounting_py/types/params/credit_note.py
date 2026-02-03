import pydantic
import typing
import typing_extensions

from .invoice_address import InvoiceAddress, _SerializerInvoiceAddress
from .line_item import LineItem, _SerializerLineItem
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation, _SerializerAllocation
    from .contact import Contact, _SerializerContact
    from .payment import Payment, _SerializerPayment


class CreditNote(typing_extensions.TypedDict):
    """
    CreditNote
    """

    allocations: typing_extensions.NotRequired[typing.List["Allocation"]]
    """
    See Allocations
    """

    applied_amount: typing_extensions.NotRequired[float]
    """
    The amount of applied to an invoice
    """

    branding_theme_id: typing_extensions.NotRequired[str]
    """
    See BrandingThemes
    """

    cis_deduction: typing_extensions.NotRequired[float]
    """
    CIS deduction for UK contractors
    """

    cis_rate: typing_extensions.NotRequired[float]
    """
    CIS Deduction rate for the organisation
    """

    contact: typing_extensions.NotRequired["Contact"]

    credit_note_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier
    """

    credit_note_number: typing_extensions.NotRequired[str]
    """
    ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings)
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

    currency_rate: typing_extensions.NotRequired[float]
    """
    The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used
    """

    date: typing_extensions.NotRequired[str]
    """
    The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation
    """

    due_date: typing_extensions.NotRequired[str]
    """
    Date invoice is due – YYYY-MM-DD
    """

    fully_paid_on_date: typing_extensions.NotRequired[str]
    """
    Date when credit note was fully paid(UTC format)
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if a credit note has an attachment
    """

    has_errors: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a credit note has an validation errors
    """

    invoice_addresses: typing_extensions.NotRequired[typing.List[InvoiceAddress]]
    """
    An array of addresses used to auto calculate sales tax
    """

    line_amount_types: typing_extensions.NotRequired[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ]
    """
    Line amounts are exclusive of tax by default if you don’t specify this element. See Line Amount Types
    """

    line_items: typing_extensions.NotRequired[typing.List[LineItem]]
    """
    See Invoice Line Items
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]
    """
    See Payments
    """

    reference: typing_extensions.NotRequired[str]
    """
    ACCRECCREDIT only – additional reference number
    """

    remaining_credit: typing_extensions.NotRequired[float]
    """
    The remaining credit balance on the Credit Note
    """

    sent_to_contact: typing_extensions.NotRequired[bool]
    """
    Boolean to set whether the credit note in the Xero app should be marked as “sent”. This can be set only on credit notes that have been approved
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "DRAFT", "PAID", "SUBMITTED", "VOIDED"
        ]
    ]
    """
    See Credit Note Status Codes
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    The subtotal of the credit note excluding taxes
    """

    total: typing_extensions.NotRequired[float]
    """
    The total of the Credit Note(subtotal + total tax)
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    The total tax on the credit note
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["ACCPAYCREDIT", "ACCRECCREDIT"]
    ]
    """
    See Credit Note Types
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of last update to the credit note
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerCreditNote(pydantic.BaseModel):
    """
    Serializer for CreditNote handling case conversions
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
    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
    )
    cis_deduction: typing.Optional[float] = pydantic.Field(
        alias="CISDeduction", default=None
    )
    cis_rate: typing.Optional[float] = pydantic.Field(alias="CISRate", default=None)
    contact: typing.Optional["_SerializerContact"] = pydantic.Field(
        alias="Contact", default=None
    )
    credit_note_id: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteID", default=None
    )
    credit_note_number: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteNumber", default=None
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
    due_date: typing.Optional[str] = pydantic.Field(alias="DueDate", default=None)
    fully_paid_on_date: typing.Optional[str] = pydantic.Field(
        alias="FullyPaidOnDate", default=None
    )
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    has_errors: typing.Optional[bool] = pydantic.Field(alias="HasErrors", default=None)
    invoice_addresses: typing.Optional[typing.List[_SerializerInvoiceAddress]] = (
        pydantic.Field(alias="InvoiceAddresses", default=None)
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
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    remaining_credit: typing.Optional[float] = pydantic.Field(
        alias="RemainingCredit", default=None
    )
    sent_to_contact: typing.Optional[bool] = pydantic.Field(
        alias="SentToContact", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "DRAFT", "PAID", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    type_: typing.Optional[
        typing_extensions.Literal["ACCPAYCREDIT", "ACCRECCREDIT"]
    ] = pydantic.Field(alias="Type", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
