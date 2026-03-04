import pydantic
import typing

from .pagination import Pagination
from .time_entry import TimeEntry


class TimeEntries(pydantic.BaseModel):
    """
    TimeEntries
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[TimeEntry]] = pydantic.Field(
        alias="items", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
