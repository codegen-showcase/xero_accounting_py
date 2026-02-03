import pydantic
import typing
import typing_extensions

from .manual_journal import ManualJournal, _SerializerManualJournal
from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError


class ManualJournals(typing_extensions.TypedDict):
    """
    ManualJournals
    """

    manual_journals: typing_extensions.NotRequired[typing.List[ManualJournal]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerManualJournals(pydantic.BaseModel):
    """
    Serializer for ManualJournals handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    manual_journals: typing.Optional[typing.List[_SerializerManualJournal]] = (
        pydantic.Field(alias="ManualJournals", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
