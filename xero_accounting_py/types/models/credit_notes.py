import pydantic
import typing
import typing_extensions

from .pagination import Pagination
from .validation_error import ValidationError

if typing_extensions.TYPE_CHECKING:
    from .credit_note import CreditNote


class CreditNotes(pydantic.BaseModel):
    """
    CreditNotes
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credit_notes: typing.Optional[typing.List["CreditNote"]] = pydantic.Field(
        alias="CreditNotes", default=None
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
