import pydantic
import typing
import typing_extensions


class Action(pydantic.BaseModel):
    """
    Action
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Name of the actions for this organisation
    """
    status: typing.Optional[typing_extensions.Literal["ALLOWED", "NOT-ALLOWED"]] = (
        pydantic.Field(alias="Status", default=None)
    )
    """
    Status of the action for this organisation
    """
