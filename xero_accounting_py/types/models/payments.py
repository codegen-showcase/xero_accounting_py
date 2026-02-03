import pydantic
import typing
import typing_extensions

from .pagination import Pagination
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .payment import Payment


class Payments(pydantic.BaseModel):
    """
    Payments
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payments: typing.Optional[typing.List["Payment"]] = pydantic.Field(
        alias="Payments", default=None
    )
    warnings: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    """
    Displays array of warning messages from the API
    """
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
