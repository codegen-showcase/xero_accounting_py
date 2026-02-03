import pydantic
import typing


class LineItemItem(pydantic.BaseModel):
    """
    LineItemItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing.Optional[str] = pydantic.Field(alias="Code", default=None)
    """
    User defined item code (max length = 30)
    """
    item_id: typing.Optional[str] = pydantic.Field(alias="ItemID", default=None)
    """
    The Xero identifier for an Item
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the item (max length = 50)
    """
