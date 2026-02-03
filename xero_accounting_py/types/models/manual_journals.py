import pydantic
import typing

from .manual_journal import ManualJournal
from .pagination import Pagination
from .validation_error import ValidationError


class ManualJournals(pydantic.BaseModel):
    """
    ManualJournals
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    manual_journals: typing.Optional[typing.List[ManualJournal]] = pydantic.Field(
        alias="ManualJournals", default=None
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
