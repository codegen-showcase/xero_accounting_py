import pydantic
import typing

from .pagination import Pagination
from .project_user import ProjectUser


class ProjectUsers(pydantic.BaseModel):
    """
    ProjectUsers
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[ProjectUser]] = pydantic.Field(
        alias="items", default=None
    )
    pagination: typing.Optional[Pagination] = pydantic.Field(
        alias="pagination", default=None
    )
