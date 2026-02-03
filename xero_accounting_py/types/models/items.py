import pydantic
import typing

from .item import Item


class Items(pydantic.BaseModel):
    """
    Items
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[Item]] = pydantic.Field(
        alias="Items", default=None
    )
