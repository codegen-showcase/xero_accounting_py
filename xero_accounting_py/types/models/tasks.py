import pydantic
import typing

from .pagination import Pagination
from .task import Task


class Tasks(pydantic.BaseModel):
    """
    Tasks
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[Task]] = pydantic.Field(
        alias="items", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
