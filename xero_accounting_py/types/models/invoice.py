import pydantic
import typing
import typing_extensions

from .attachment import Attachment
from .invoice_address import InvoiceAddress
from .line_item import LineItem
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .contact import Contact
    from .credit_note import CreditNote
    from .overpayment import Overpayment
    from .payment import Payment
    from .prepayment import Prepayment


class Invoice(pydantic.BaseModel):
    """
    Invoice
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_credited: typing.Optional[float] = pydantic.Field(
        alias="AmountCredited", default=None
    )
    """
    Sum of all credit notes, over-payments and pre-payments applied to invoice
    """
    amount_due: typing.Optional[float] = pydantic.Field(alias="AmountDue", default=None)
    """
    Amount remaining to be paid on invoice
    """
    amount_paid: typing.Optional[float] = pydantic.Field(
        alias="AmountPaid", default=None
    )
    """
    Sum of payments received for invoice
    """
    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(
        alias="Attachments", default=None
    )
    """
    Displays array of attachments from the API
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
    credit_notes: typing.Optional[typing.List["CreditNote"]] = pydantic.Field(
        alias="CreditNotes", default=None
    )
    """
    Details of credit notes that have been applied to an invoice
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
    The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. (max length = [18].[6])
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date invoice was issued – YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation
    """
    due_date: typing.Optional[str] = pydantic.Field(alias="DueDate", default=None)
    """
    Date invoice is due – YYYY-MM-DD
    """
    expected_payment_date: typing.Optional[str] = pydantic.Field(
        alias="ExpectedPaymentDate", default=None
    )
    """
    Shown on sales invoices (Accounts Receivable) when this has been set
    """
    fully_paid_on_date: typing.Optional[str] = pydantic.Field(
        alias="FullyPaidOnDate", default=None
    )
    """
    The date the invoice was fully paid. Only returned on fully paid invoices
    """
    has_attachments: typing.Optional[bool] = pydantic.Field(
        alias="HasAttachments", default=None
    )
    """
    boolean to indicate if an invoice has an attachment
    """
    has_errors: typing.Optional[bool] = pydantic.Field(alias="HasErrors", default=None)
    """
    A boolean to indicate if a invoice has an validation errors
    """
    invoice_addresses: typing.Optional[typing.List[InvoiceAddress]] = pydantic.Field(
        alias="InvoiceAddresses", default=None
    )
    """
    An array of addresses used to auto calculate sales tax
    """
    invoice_id: typing.Optional[str] = pydantic.Field(alias="InvoiceID", default=None)
    """
    Xero generated unique identifier for invoice
    """
    invoice_number: typing.Optional[str] = pydantic.Field(
        alias="InvoiceNumber", default=None
    )
    """
    ACCREC – Unique alpha numeric code identifying invoice (when missing will auto-generate from your Organisation Invoice Settings) (max length = 255)
    """
    is_discounted: typing.Optional[bool] = pydantic.Field(
        alias="IsDiscounted", default=None
    )
    """
    boolean to indicate if an invoice has a discount
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
    See LineItems
    """
    overpayments: typing.Optional[typing.List["Overpayment"]] = pydantic.Field(
        alias="Overpayments", default=None
    )
    """
    See Overpayments
    """
    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    """
    See Payments
    """
    planned_payment_date: typing.Optional[str] = pydantic.Field(
        alias="PlannedPaymentDate", default=None
    )
    """
    Shown on bills (Accounts Payable) when this has been set
    """
    prepayments: typing.Optional[typing.List["Prepayment"]] = pydantic.Field(
        alias="Prepayments", default=None
    )
    """
    See Prepayments
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    ACCREC only – additional reference number
    """
    repeating_invoice_id: typing.Optional[str] = pydantic.Field(
        alias="RepeatingInvoiceID", default=None
    )
    """
    Xero generated unique identifier for repeating invoices
    """
    sent_to_contact: typing.Optional[bool] = pydantic.Field(
        alias="SentToContact", default=None
    )
    """
    Boolean to set whether the invoice in the Xero app should be marked as “sent”. This can be set only on invoices that have been approved
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "DRAFT", "PAID", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    """
    See Invoice Status Codes
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    sub_total: typing.Optional[float] = pydantic.Field(alias="SubTotal", default=None)
    """
    Total of invoice excluding taxes
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    Total of Invoice tax inclusive (i.e. SubTotal + TotalTax). This will be ignored if it doesn’t equal the sum of the LineAmounts
    """
    total_discount: typing.Optional[float] = pydantic.Field(
        alias="TotalDiscount", default=None
    )
    """
    Total of discounts applied on the invoice line items
    """
    total_tax: typing.Optional[float] = pydantic.Field(alias="TotalTax", default=None)
    """
    Total tax on invoice
    """
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
    """
    See Invoice Types
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    URL link to a source document – shown as “Go to [appName]” in the Xero app
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
