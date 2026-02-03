import pydantic
import typing

from .journal import Journal
from .validation_error import ValidationError


class Journals(pydantic.BaseModel):
    """
    Journals
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    journals: typing.Optional[typing.List[Journal]] = pydantic.Field(
        alias="Journals", default=None
    )
    warnings: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    """
    Displays array of warning messages from the API
    """
