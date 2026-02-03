import pydantic
import typing
import typing_extensions

from .account import Account, _SerializerAccount
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment, _SerializerPayment


class BatchPayment(typing_extensions.TypedDict):
    """
    BatchPayment
    """

    account: typing_extensions.NotRequired[Account]

    amount: typing_extensions.NotRequired[float]
    """
    The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00
    """

    batch_payment_id: typing_extensions.NotRequired[str]
    """
    The Xero generated unique identifier for the bank transaction (read-only)
    """

    code: typing_extensions.NotRequired[str]
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """

    date: typing_extensions.NotRequired[str]
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """

    date_string: typing_extensions.NotRequired[str]
    """
    Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06
    """

    details: typing_extensions.NotRequired[str]
    """
    (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18
    """

    is_reconciled: typing_extensions.NotRequired[bool]
    """
    Booelan that tells you if the batch payment has been reconciled (read-only)
    """

    narrative: typing_extensions.NotRequired[str]
    """
    (UK Only) Only shows on the statement line in Xero. Max length =18
    """

    particulars: typing_extensions.NotRequired[str]
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]
    """
    An array of payments
    """

    reference: typing_extensions.NotRequired[str]
    """
    (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["AUTHORISED", "DELETED"]
    ]
    """
    AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API.
    """

    total_amount: typing_extensions.NotRequired[float]
    """
    The total of the payments that make up the batch (read-only)
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["PAYBATCH", "RECBATCH"]
    ]
    """
    PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only)
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of last update to the payment
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerBatchPayment(pydantic.BaseModel):
    """
    Serializer for BatchPayment handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[_SerializerAccount] = pydantic.Field(
        alias="Account", default=None
    )
    amount: typing.Optional[float] = pydantic.Field(alias="Amount", default=None)
    batch_payment_id: typing.Optional[str] = pydantic.Field(
        alias="BatchPaymentID", default=None
    )
    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    date: typing.Optional[str] = pydantic.Field(alias="Date", default=None)
    date_string: typing.Optional[str] = pydantic.Field(alias="DateString", default=None)
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    is_reconciled: typing.Optional[bool] = pydantic.Field(
        alias="IsReconciled", default=None
    )
    narrative: typing.Optional[str] = pydantic.Field(alias="Narrative", default=None)
    particulars: typing.Optional[str] = pydantic.Field(
        alias="Particulars", default=None
    )
    payments: typing.Optional[typing.List["_SerializerPayment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    reference: typing.Optional[str] = pydantic.Field(alias="Reference", default=None)
    status: typing.Optional[typing_extensions.Literal["AUTHORISED", "DELETED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    total_amount: typing.Optional[float] = pydantic.Field(
        alias="TotalAmount", default=None
    )
    type_: typing.Optional[typing_extensions.Literal["PAYBATCH", "RECBATCH"]] = (
        pydantic.Field(alias="Type", default=None)
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
