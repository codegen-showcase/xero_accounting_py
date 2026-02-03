import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .credit_note import CreditNote
    from .invoice import Invoice
    from .overpayment import Overpayment
    from .prepayment import Prepayment


class Allocation(pydantic.BaseModel):
    """
    Allocation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allocation_id: typing.Optional[str] = pydantic.Field(
        alias="AllocationID", default=None
    )
    """
    Xero generated unique identifier
    """
    amount: float = pydantic.Field(
        alias="Amount",
    )
    """
    the amount being applied to the invoice
    """
    credit_note: typing.Optional["CreditNote"] = pydantic.Field(
        alias="CreditNote", default=None
    )
    date: str = pydantic.Field(
        alias="Date",
    )
    """
    the date the allocation is applied YYYY-MM-DD.
    """
    invoice: "Invoice" = pydantic.Field(
        alias="Invoice",
    )
    is_deleted: typing.Optional[bool] = pydantic.Field(alias="IsDeleted", default=None)
    """
    A flag that returns true when the allocation is succesfully deleted
    """
    overpayment: typing.Optional["Overpayment"] = pydantic.Field(
        alias="Overpayment", default=None
    )
    prepayment: typing.Optional["Prepayment"] = pydantic.Field(
        alias="Prepayment", default=None
    )
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    A string to indicate if a invoice status
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
