import pydantic
import typing
import typing_extensions

from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment, _SerializerPayment


class Payments(typing_extensions.TypedDict):
    """
    Payments
    """

    payments: typing_extensions.NotRequired[typing.List["Payment"]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerPayments(pydantic.BaseModel):
    """
    Serializer for Payments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payments: typing.Optional[typing.List["_SerializerPayment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
