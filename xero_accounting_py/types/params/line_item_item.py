import pydantic
import typing
import typing_extensions


class LineItemItem(typing_extensions.TypedDict):
    """
    LineItemItem
    """

    code: typing_extensions.NotRequired[str]
    """
    User defined item code (max length = 30)
    """

    item_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an Item
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the item (max length = 50)
    """


class _SerializerLineItemItem(pydantic.BaseModel):
    """
    Serializer for LineItemItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    item_id: typing.Optional[str] = pydantic.Field(alias="ItemID", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
