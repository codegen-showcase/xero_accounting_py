import pydantic
import typing

from .user import User


class Users(pydantic.BaseModel):
    """
    Users
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    users: typing.Optional[typing.List[User]] = pydantic.Field(
        alias="Users", default=None
    )
