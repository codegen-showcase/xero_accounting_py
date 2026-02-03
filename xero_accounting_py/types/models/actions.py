import pydantic
import typing

from .action import Action


class Actions(pydantic.BaseModel):
    """
    Actions
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.List[Action]] = pydantic.Field(
        alias="Actions", default=None
    )
