import pydantic
import typing
import typing_extensions

from .user import User, _SerializerUser

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment, _SerializerPayment
    from .receipt import Receipt, _SerializerReceipt


class ExpenseClaim(typing_extensions.TypedDict):
    """
    ExpenseClaim
    """

    amount_due: typing_extensions.NotRequired[float]
    """
    The amount due to be paid for an expense claim
    """

    amount_paid: typing_extensions.NotRequired[float]
    """
    The amount still to pay for an expense claim
    """

    expense_claim_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier for an expense claim
    """

    payment_due_date: typing_extensions.NotRequired[str]
    """
    The date when the expense claim is due to be paid YYYY-MM-DD
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]
    """
    See Payments
    """

    receipt_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9
    """

    receipts: typing_extensions.NotRequired[typing.List["Receipt"]]

    reporting_date: typing_extensions.NotRequired[str]
    """
    The date the expense claim will be reported in Xero YYYY-MM-DD
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "PAID", "SUBMITTED", "VOIDED"
        ]
    ]
    """
    Current status of an expense claim – see status types
    """

    total: typing_extensions.NotRequired[float]
    """
    The total of an expense claim being paid
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date UTC format
    """

    user: typing_extensions.NotRequired[User]


class _SerializerExpenseClaim(pydantic.BaseModel):
    """
    Serializer for ExpenseClaim handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_due: typing.Optional[float] = pydantic.Field(alias="AmountDue", default=None)
    amount_paid: typing.Optional[float] = pydantic.Field(
        alias="AmountPaid", default=None
    )
    expense_claim_id: typing.Optional[str] = pydantic.Field(
        alias="ExpenseClaimID", default=None
    )
    payment_due_date: typing.Optional[str] = pydantic.Field(
        alias="PaymentDueDate", default=None
    )
    payments: typing.Optional[typing.List["_SerializerPayment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    receipt_id: typing.Optional[str] = pydantic.Field(alias="ReceiptID", default=None)
    receipts: typing.Optional[typing.List["_SerializerReceipt"]] = pydantic.Field(
        alias="Receipts", default=None
    )
    reporting_date: typing.Optional[str] = pydantic.Field(
        alias="ReportingDate", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal[
            "AUTHORISED", "DELETED", "PAID", "SUBMITTED", "VOIDED"
        ]
    ] = pydantic.Field(alias="Status", default=None)
    total: typing.Optional[float] = pydantic.Field(alias="Total", default=None)
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    user: typing.Optional[_SerializerUser] = pydantic.Field(alias="User", default=None)
