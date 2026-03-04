import pydantic
import typing

from .pagination import Pagination
from .project import Project


class Projects(pydantic.BaseModel):
    """
    Projects
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[Project]] = pydantic.Field(
        alias="items", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
