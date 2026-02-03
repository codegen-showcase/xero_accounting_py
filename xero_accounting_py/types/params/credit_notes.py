import pydantic
import typing
import typing_extensions

from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .credit_note import CreditNote, _SerializerCreditNote


class CreditNotes(typing_extensions.TypedDict):
    """
    CreditNotes
    """

    credit_notes: typing_extensions.NotRequired[typing.List["CreditNote"]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerCreditNotes(pydantic.BaseModel):
    """
    Serializer for CreditNotes handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    credit_notes: typing.Optional[typing.List["_SerializerCreditNote"]] = (
        pydantic.Field(alias="CreditNotes", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
