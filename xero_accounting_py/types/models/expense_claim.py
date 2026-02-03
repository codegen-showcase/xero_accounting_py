import pydantic
import typing
import typing_extensions

from .user import User

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment
    from .receipt import Receipt


class ExpenseClaim(pydantic.BaseModel):
    """
    ExpenseClaim
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_due: typing.Optional[float] = pydantic.Field(alias="AmountDue", default=None)
    """
    The amount due to be paid for an expense claim
    """
    amount_paid: typing.Optional[float] = pydantic.Field(
        alias="AmountPaid", default=None
    )
    """
    The amount still to pay for an expense claim
    """
    expense_claim_id: typing.Optional[str] = pydantic.Field(
        alias="ExpenseClaimID", default=None
    )
    """
    Xero generated unique identifier for an expense claim
    """
    payment_due_date: typing.Optional[str] = pydantic.Field(
        alias="PaymentDueDate", default=None
    )
    """
    The date when the expense claim is due to be paid YYYY-MM-DD
    """
    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    """
    See Payments
    """
    receipt_id: typing.Optional[str] = pydantic.Field(alias="ReceiptID", default=None)
    """
    The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9
    """
    receipts: typing.Optional[typing.List["Receipt"]] = pydantic.Field(
        alias="Receipts", default=None
    )
    reporting_date: typing.Optional[str] = pydantic.Field(
        alias="ReportingDate", default=None
    )
    """
    The date the expense claim will be reported in Xero YYYY-MM-DD
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "PAID", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    """
    Current status of an expense claim – see status types
    """
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    """
    The total of an expense claim being paid
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date UTC format
    """
    user: typing.Optional[User] = pydantic.Field(alias="User", default=None)
