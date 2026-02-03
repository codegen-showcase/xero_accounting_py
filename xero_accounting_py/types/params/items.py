import pydantic
import typing
import typing_extensions

from .item import Item, _SerializerItem


class Items(typing_extensions.TypedDict):
    """
    Items
    """

    items: typing_extensions.NotRequired[typing.List[Item]]


class _SerializerItems(pydantic.BaseModel):
    """
    Serializer for Items handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    items: typing.Optional[typing.List[_SerializerItem]] = pydantic.Field(
        alias="Items", default=None
    )
