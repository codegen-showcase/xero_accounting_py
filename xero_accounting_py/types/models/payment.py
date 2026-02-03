import pydantic
import typing
import typing_extensions

from .account import Account
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .batch_payment import BatchPayment
    from .credit_note import CreditNote
    from .invoice import Invoice
    from .overpayment import Overpayment
    from .prepayment import Prepayment


class Payment(pydantic.BaseModel):
    """
    Payment
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[Account] = pydantic.Field(alias="Account", default=None)
    amount: typing.Optional[float] = pydantic.Field(alias="Amount", default=None)
    """
    The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00
    """
    bank_account_number: typing.Optional[str] = pydantic.Field(
        alias="BankAccountNumber", default=None
    )
    """
    The suppliers bank account number the payment is being made to
    """
    bank_amount: typing.Optional[float] = pydantic.Field(
        alias="BankAmount", default=None
    )
    """
    The amount of the payment in the currency of the bank account.
    """
    batch_payment: typing.Optional["BatchPayment"] = pydantic.Field(
        alias="BatchPayment", default=None
    )
    batch_payment_id: typing.Optional[str] = pydantic.Field(
        alias="BatchPaymentID", default=None
    )
    """
    Present if the payment was created as part of a batch.
    """
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    """
    Code of account you are using to make the payment e.g. 001 (note- not all accounts have a code value)
    """
    credit_note: typing.Optional["CreditNote"] = pydantic.Field(
        alias="CreditNote", default=None
    )
    credit_note_number: typing.Optional[str] = pydantic.Field(
        alias="CreditNoteNumber", default=None
    )
    """
    Number of invoice or credit note you are applying payment to e.g. INV-4003
    """
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
    """
    Exchange rate when payment is received. Only used for non base currency invoices and credit notes e.g. 0.7500
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    """
    The information to appear on the supplier's bank account
    """
    has_account: typing.Optional[bool] = pydantic.Field(
        alias="HasAccount", default=None
    )
    """
    A boolean to indicate if a contact has an validation errors
    """
    has_validation_errors: typing.Optional[bool] = pydantic.Field(
        alias="HasValidationErrors", default=None
    )
    """
    A boolean to indicate if a contact has an validation errors
    """
    invoice: typing.Optional["Invoice"] = pydantic.Field(alias="Invoice", default=None)
    invoice_number: typing.Optional[str] = pydantic.Field(
        alias="InvoiceNumber", default=None
    )
    """
    Number of invoice or credit note you are applying payment to e.g.INV-4003
    """
    is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="IsReconciled", default=None
    )
    """
    An optional parameter for the payment. A boolean indicating whether you would like the payment to be created as reconciled when using PUT, or whether a payment has been reconciled when using GET
    """
    overpayment: typing.Optional["Overpayment"] = pydantic.Field(
        alias="Overpayment", default=None
    )
    particulars: typing.Optional[str] = pydantic.Field(
        alias="Particulars", default=None
    )
    """
    The suppliers bank account number the payment is being made to
    """
    payment_id: typing.Optional[str] = pydantic.Field(alias="PaymentID", default=None)
    """
    The Xero identifier for an Payment e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
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
    """
    See Payment Types.
    """
    prepayment: typing.Optional["Prepayment"] = pydantic.Field(
        alias="Prepayment", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    An optional description for the payment e.g. Direct Debit
    """
    status: typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    """
    The status of the payment.
    """
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    UTC timestamp of last update to the payment
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
