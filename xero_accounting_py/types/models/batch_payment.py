import pydantic
import typing
import typing_extensions

from .account import Account
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment


class BatchPayment(pydantic.BaseModel):
    """
    BatchPayment
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
    batch_payment_id: typing.Optional[str] = pydantic.Field(
        alias="BatchPaymentID", default=None
    )
    """
    The Xero generated unique identifier for the bank transaction (read-only)
    """
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """
    date_string: typing.Optional[str] = pydantic.Field(alias="DateString", default=None)
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    """
    (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18
    """
    is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="IsReconciled", default=None
    )
    """
    Booelan that tells you if the batch payment has been reconciled (read-only)
    """
    narrative: typing.Optional[str] = pydantic.Field(alias="Narrative", default=None)
    """
    (UK Only) Only shows on the statement line in Xero. Max length =18
    """
    particulars: typing.Optional[str] = pydantic.Field(
        alias="Particulars", default=None
    )
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """
    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    """
    An array of payments
    """
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """
    status: typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    """
    AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API.
    """
    total_amount: typing.Optional[float] = pydantic.Field(
        alias="TotalAmount", default=None
    )
    """
    The total of the payments that make up the batch (read-only)
    """
    type_: typing.Optional[typing_extensions.Literal["PAYBATCH", "RECBATCH"]] = (
        pydantic.Field(alias="Type", default=None)
    )
    """
    PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only)
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
