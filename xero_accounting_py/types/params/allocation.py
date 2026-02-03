import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .credit_note import CreditNote, _SerializerCreditNote
    from .invoice import Invoice, _SerializerInvoice
    from .overpayment import Overpayment, _SerializerOverpayment
    from .prepayment import Prepayment, _SerializerPrepayment


class Allocation(typing_extensions.TypedDict):
    """
    Allocation
    """

    allocation_id: typing_extensions.NotRequired[str]
    """
    Xero generated unique identifier
    """

    amount: typing_extensions.Required[float]
    """
    the amount being applied to the invoice
    """

    credit_note: typing_extensions.NotRequired["CreditNote"]

    date: typing_extensions.Required[str]
    """
    the date the allocation is applied YYYY-MM-DD.
    """

    invoice: typing_extensions.Required["Invoice"]

    is_deleted: typing_extensions.NotRequired[bool]
    """
    A flag that returns true when the allocation is succesfully deleted
    """

    overpayment: typing_extensions.NotRequired["Overpayment"]

    prepayment: typing_extensions.NotRequired["Prepayment"]

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    A string to indicate if a invoice status
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerAllocation(pydantic.BaseModel):
    """
    Serializer for Allocation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allocation_id: typing.Optional[str] = pydantic.Field(
        alias="AllocationID", default=None
    )
    amount: float = pydantic.Field(
        alias="Amount",
    )
    credit_note: typing.Optional["_SerializerCreditNote"] = pydantic.Field(
        alias="CreditNote", default=None
    )
    date: str = pydantic.Field(
        alias="Date",
    )
    invoice: "_SerializerInvoice" = pydantic.Field(
        alias="Invoice",
    )
    is_deleted: typing.Optional[bool] = pydantic.Field(alias="IsDeleted", default=None)
    overpayment: typing.Optional["_SerializerOverpayment"] = pydantic.Field(
        alias="Overpayment", default=None
    )
    prepayment: typing.Optional["_SerializerPrepayment"] = pydantic.Field(
        alias="Prepayment", default=None
    )
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
