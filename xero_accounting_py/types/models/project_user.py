import pydantic
import typing


class ProjectUser(pydantic.BaseModel):
    """
    ProjectUser
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email address of the user.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Full name of the user.
    """
    user_id: typing.Optional[str] = pydantic.Field(alias="userId", default=None)
    """
    Identifier of the user of the project.
    """
