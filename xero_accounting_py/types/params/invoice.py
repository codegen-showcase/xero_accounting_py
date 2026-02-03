import pydantic
import typing
import typing_extensions

from .attachment import Attachment, _SerializerAttachment
from .invoice_address import InvoiceAddress, _SerializerInvoiceAddress
from .line_item import LineItem, _SerializerLineItem
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact, _SerializerContact
    from .credit_note import CreditNote, _SerializerCreditNote
    from .overpayment import Overpayment, _SerializerOverpayment
    from .payment import Payment, _SerializerPayment
    from .prepayment import Prepayment, _SerializerPrepayment


class Invoice(typing_extensions.TypedDict):
    """
    Invoice
    """

    amount_credited: typing_extensions.NotRequired[float]
    """
    Sum of all credit notes, over-payments and pre-payments applied to invoice
    """

    amount_due: typing_extensions.NotRequired[float]
    """
    Amount remaining to be paid on invoice
    """

    amount_paid: typing_extensions.NotRequired[float]
    """
    Sum of payments received for invoice
    """

    attachments: typing_extensions.NotRequired[typing.List[Attachment]]
    """
    Displays array of attachments from the API
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

    credit_notes: typing_extensions.NotRequired[typing.List["CreditNote"]]
    """
    Details of credit notes that have been applied to an invoice
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
    The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length = [18].[6])
    """

    date: typing_extensions.NotRequired[str]
    """
    Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation
    """

    due_date: typing_extensions.NotRequired[str]
    """
    Date invoice is due – YYYY-MM-DD
    """

    expected_payment_date: typing_extensions.NotRequired[str]
    """
    Shown on sales invoices (Accounts Receivable) when this has been set
    """

    fully_paid_on_date: typing_extensions.NotRequired[str]
    """
    The date the invoice was fully paid. Only returned on fully paid invoices
    """

    has_attachments: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if an invoice has an attachment
    """

    has_errors: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a invoice has an validation errors
    """

    invoice_addresses: typing_extensions.NotRequired[typing.List[InvoiceAddress]]
    """
    An array of addresses used to auto calculate sales tax
    """

    invoice_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for invoice
    """

    invoice_number: typing_extensions.NotRequired[str]
    """
    ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length = 255)
    """

    is_discounted: typing_extensions.NotRequired[bool]
    """
    boolean to indicate if an invoice has a discount
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

    overpayments: typing_extensions.NotRequired[typing.List["Overpayment"]]
    """
    See Overpayments
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]
    """
    See Payments
    """

    planned_payment_date: typing_extensions.NotRequired[str]
    """
    Shown on bills (Accounts Payable) when this has been set
    """

    prepayments: typing_extensions.NotRequired[typing.List["Prepayment"]]
    """
    See Prepayments
    """

    reference: typing_extensions.NotRequired[str]
    """
    ACCREC only – additional reference number
    """

    repeating_invoice_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for repeating invoices
    """

    sent_to_contact: typing_extensions.NotRequired[bool]
    """
    Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "DRAFT", "PAID", "SUBMITTED", "VOIDED"
        ]
    ]
    """
    See Invoice Status Codes
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    sub_total: typing_extensions.NotRequired[float]
    """
    Total of invoice excluding taxes
    """

    total: typing_extensions.NotRequired[float]
    """
    Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts
    """

    total_discount: typing_extensions.NotRequired[float]
    """
    Total of discounts applied on the invoice line items
    """

    total_tax: typing_extensions.NotRequired[float]
    """
    Total tax on invoice
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ACCPAY",
            "ACCPAYCREDIT",
            "ACCREC",
            "ACCRECCREDIT",
            "APOVERPAYMENT",
            "APPREPAYMENT",
            "AROVERPAYMENT",
            "ARPREPAYMENT",
        ]
    ]
    """
    See Invoice Types
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    url: typing_extensions.NotRequired[str]
    """
    URL link to a source document – shown as “Go to [appName]” in the Xero app
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerInvoice(pydantic.BaseModel):
    """
    Serializer for Invoice handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_credited: typing.Optional[float] = pydantic.Field(
        alias="AmountCredited", default=None
    )
    amount_due: typing.Optional[float] = pydantic.Field(alias="AmountDue", default=None)
    amount_paid: typing.Optional[float] = pydantic.Field(
        alias="AmountPaid", default=None
    )
    attachments: typing.Optional[typing.List[_SerializerAttachment]] = pydantic.Field(
        alias="Attachments", default=None
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
    credit_notes: typing.Optional[typing.List["_SerializerCreditNote"]] = (
        pydantic.Field(alias="CreditNotes", default=None)
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
    expected_payment_date: typing.Optional[str] = pydantic.Field(
        alias="ExpectedPaymentDate", default=None
    )
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
    invoice_id: typing.Optional[str] = pydantic.Field(alias="InvoiceID", default=None)
    invoice_number: typing.Optional[str] = pydantic.Field(
        alias="InvoiceNumber", default=None
    )
    is_discounted: typing.Optional[bool] = pydantic.Field(
        alias="IsDiscounted", default=None
    )
    line_amount_types: typing.Optional[
        typing_extensions.Literal["Exclusive", "Inclusive", "NoTax"]
    ] = pydantic.Field(alias="LineAmountTypes", default=None)
    line_items: typing.Optional[typing.List[_SerializerLineItem]] = pydantic.Field(
        alias="LineItems", default=None
    )
    overpayments: typing.Optional[typing.List["_SerializerOverpayment"]] = (
        pydantic.Field(alias="Overpayments", default=None)
    )
    payments: typing.Optional[typing.List["_SerializerPayment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    planned_payment_date: typing.Optional[str] = pydantic.Field(
        alias="PlannedPaymentDate", default=None
    )
    prepayments: typing.Optional[typing.List["_SerializerPrepayment"]] = pydantic.Field(
        alias="Prepayments", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    repeating_invoice_id: typing.Optional[str] = pydantic.Field(
        alias="RepeatingInvoiceID", default=None
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
    total_discount: typing.Optional[float] = pydantic.Field(
        alias="TotalDiscount", default=None
    )
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "ACCPAY",
            "ACCPAYCREDIT",
            "ACCREC",
            "ACCRECCREDIT",
            "APOVERPAYMENT",
            "APPREPAYMENT",
            "AROVERPAYMENT",
            "ARPREPAYMENT",
        ]
    ] = pydantic.Field(alias="Type", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
