import pydantic
import typing
import typing_extensions

from .account import Account, _SerializerAccount
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .batch_payment import BatchPayment, _SerializerBatchPayment
    from .credit_note import CreditNote, _SerializerCreditNote
    from .invoice import Invoice, _SerializerInvoice
    from .overpayment import Overpayment, _SerializerOverpayment
    from .prepayment import Prepayment, _SerializerPrepayment


class Payment(typing_extensions.TypedDict):
    """
    Payment
    """

    account: typing_extensions.NotRequired[Account]

    amount: typing_extensions.NotRequired[float]
    """
    The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00
    """

    bank_account_number: typing_extensions.NotRequired[str]
    """
    The suppliers bank account number the payment is being made to
    """

    bank_amount: typing_extensions.NotRequired[float]
    """
    The amount of the payment in the currency of the bank account.
    """

    batch_payment: typing_extensions.NotRequired["BatchPayment"]

    batch_payment_id: typing_extensions.NotRequired[str]
    """
    Present if the payment was created as part of a batch.
    """

    code: typing_extensions.NotRequired[str]
    """
    Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)
    """

    credit_note: typing_extensions.NotRequired["CreditNote"]

    credit_note_number: typing_extensions.NotRequired[str]
    """
    Number of invoice or credit note you are applying payment to e.g. INV-4003
    """

    currency_rate: typing_extensions.NotRequired[float]
    """
    Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500
    """

    date: typing_extensions.NotRequired[str]
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """

    details: typing_extensions.NotRequired[str]
    """
    The information to appear on the supplier's bank account
    """

    has_account: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a contact has an validation errors
    """

    has_validation_errors: typing_extensions.NotRequired[bool]
    """
    A boolean to indicate if a contact has an validation errors
    """

    invoice: typing_extensions.NotRequired["Invoice"]

    invoice_number: typing_extensions.NotRequired[str]
    """
    Number of invoice or credit note you are applying payment to e.g.INV-4003
    """

    is_reconciled: typing_extensions.NotRequired[bool]
    """
    An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET
    """

    overpayment: typing_extensions.NotRequired["Overpayment"]

    particulars: typing_extensions.NotRequired[str]
    """
    The suppliers bank account number the payment is being made to
    """

    payment_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    payment_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "ACCPAYPAYMENT",
            "ACCRECPAYMENT",
            "APCREDITPAYMENT",
            "APOVERPAYMENTPAYMENT",
            "APPREPAYMENTPAYMENT",
            "ARCREDITPAYMENT",
            "AROVERPAYMENTPAYMENT",
            "ARPREPAYMENTPAYMENT",
        ]
    ]
    """
    See Payment Types.
    """

    prepayment: typing_extensions.NotRequired["Prepayment"]

    reference: typing_extensions.NotRequired[str]
    """
    An optional description for the payment e.g. Direct Debit
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["AUTHORISED", "DELETED"]
    ]
    """
    The status of the payment.
    """

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of last update to the payment
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """


class _SerializerPayment(pydantic.BaseModel):
    """
    Serializer for Payment handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[_SerializerAccount] = pydantic.Field(
        alias="Account", default=None
    )
    amount: typing.Optional[float] = pydantic.Field(alias="Amount", default=None)
    bank_account_number: typing.Optional[str] = pydantic.Field(
        alias="BankAccountNumber", default=None
    )
    bank_amount: typing.Optional[float] = pydantic.Field(
        alias="BankAmount", default=None
    )
    batch_payment: typing.Optional["_SerializerBatchPayment"] = pydantic.Field(
        alias="BatchPayment", default=None
    )
    batch_payment_id: typing.Optional[str] = pydantic.Field(
        alias="BatchPaymentID", default=None
    )
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    credit_note: typing.Optional["_SerializerCreditNote"] = pydantic.Field(
        alias="CreditNote", default=None
    )
    credit_note_number: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteNumber", default=None
    )
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    has_account: typing.Optional[bool] = pydantic.Field(
        alias="HasAccount", default=None
    )
    has_validation_errors: typing.Optional[bool] = pydantic.Field(
        alias="HasValidationErrors", default=None
    )
    invoice: typing.Optional["_SerializerInvoice"] = pydantic.Field(
        alias="Invoice", default=None
    )
    invoice_number: typing.Optional[str] = pydantic.Field(
        alias="InvoiceNumber", default=None
    )
    is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="IsReconciled", default=None
    )
    overpayment: typing.Optional["_SerializerOverpayment"] = pydantic.Field(
        alias="Overpayment", default=None
    )
    particulars: typing.Optional[str] = pydantic.Field(
        alias="Particulars", default=None
    )
    payment_id: typing.Optional[str] = pydantic.Field(alias="PaymentID", default=None)
    payment_type: typing.Optional[
        typing_extensions.Literal[
            "ACCPAYPAYMENT",
            "ACCRECPAYMENT",
            "APCREDITPAYMENT",
            "APOVERPAYMENTPAYMENT",
            "APPREPAYMENTPAYMENT",
            "ARCREDITPAYMENT",
            "AROVERPAYMENTPAYMENT",
            "ARPREPAYMENTPAYMENT",
        ]
    ] = pydantic.Field(alias="PaymentType", default=None)
    prepayment: typing.Optional["_SerializerPrepayment"] = pydantic.Field(
        alias="Prepayment", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    status: typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
