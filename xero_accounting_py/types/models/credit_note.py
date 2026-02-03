import pydantic
import typing
import typing_extensions

from .invoice_address import InvoiceAddress
from .line_item import LineItem
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .allocation import Allocation
    from .contact import Contact
    from .payment import Payment


class CreditNote(pydantic.BaseModel):
    """
    CreditNote
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
    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
    )
    """
    See BrandingThemes
    """
    cis_deduction: typing.Optional[float] = pydantic.Field(
        alias="CISDeduction", default=None
    )
    """
    CIS deduction for UK contractors
    """
    cis_rate: typing.Optional[float] = pydantic.Field(alias="CISRate", default=None)
    """
    CIS Deduction rate for the organisation
    """
    contact: typing.Optional["Contact"] = pydantic.Field(alias="Contact", default=None)
    credit_note_id: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteID", default=None
    )
    """
    Xero generated unique identifier
    """
    credit_note_number: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteNumber", default=None
    )
    """
    ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings)
    """
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
    The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation
    """
    due_date: typing.Optional[str] = pydantic.Field(alias="DueDate", default=None)
    """
    Date invoice is due – YYYY-MM-DD
    """
    fully_paid_on_date: typing.Optional[str] = pydantic.Field(
        alias="FullyPaidOnDate", default=None
    )
    """
    Date when credit note was fully paid(UTC format)
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    boolean to indicate if a credit note has an attachment
    """
    has_errors: typing.Optional[bool] = pydantic.Field(alias="HasErrors", default=None)
    """
    A boolean to indicate if a credit note has an validation errors
    """
    invoice_addresses: typing.Optional[typing.List[InvoiceAddress]] = pydantic.Field(
        alias="InvoiceAddresses", default=None
    )
    """
    An array of addresses used to auto calculate sales tax
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
    See Invoice Line Items
    """
    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    """
    See Payments
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    ACCRECCREDIT only – additional reference number
    """
    remaining_credit: typing.Optional[float] = pydantic.Field(
        alias="RemainingCredit", default=None
    )
    """
    The remaining credit balance on the Credit Note
    """
    sent_to_contact: typing.Optional[bool] = pydantic.Field(
        alias="SentToContact", default=None
    )
    """
    Boolean to set whether the credit note in the Xero app should be marked as “sent”. This can be set only on credit notes that have been approved
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "DRAFT", "PAID", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Credit Note Status Codes
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    The subtotal of the credit note excluding taxes
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    The total of the Credit Note(subtotal + total tax)
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    The total tax on the credit note
    """
    type_: typing.Optional[
        typing_extensions.Literal["ACCPAYCREDIT", "ACCRECCREDIT"]
    ] = pydantic.Field(alias="Type", default=None)
    """
    See Credit Note Types
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    UTC timestamp of last update to the credit note
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
    warnings: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    """
    Displays array of warning messages from the API
    """
