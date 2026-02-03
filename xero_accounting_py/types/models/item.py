import pydantic
import typing

from .purchase import Purchase
from .validation_error import ValidationError


class Item(pydantic.BaseModel):
    """
    Item
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: str = pydantic.Field(
        alias="Code",
    )
    """
    User defined item code (max length = 30)
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    """
    The sales description of the item (max length = 4000)
    """
    inventory_asset_account_code: typing.Optional[str] = pydantic.Field(
        alias="InventoryAssetAccountCode", default=None
    )
    """
    The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item
    """
    is_purchased: typing.Optional[bool] = pydantic.Field(
        alias="IsPurchased", default=None
    )
    """
    Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled.
    """
    is_sold: typing.Optional[bool] = pydantic.Field(alias="IsSold", default=None)
    """
    Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled.
    """
    is_tracked_as_inventory: typing.Optional[bool] = pydantic.Field(
        alias="IsTrackedAsInventory", default=None
    )
    """
    True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set.
    """
    item_id: typing.Optional[str] = pydantic.Field(alias="ItemID", default=None)
    """
    The Xero identifier for an Item
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the item (max length = 50)
    """
    purchase_description: typing.Optional[str] = pydantic.Field(
        alias="PurchaseDescription", default=None
    )
    """
    The purchase description of the item (max length = 4000)
    """
    purchase_details: typing.Optional[Purchase] = pydantic.Field(
        alias="PurchaseDetails", default=None
    )
    quantity_on_hand: typing.Optional[float] = pydantic.Field(
        alias="QuantityOnHand", default=None
    )
    """
    The quantity of the item on hand
    """
    sales_details: typing.Optional[Purchase] = pydantic.Field(
        alias="SalesDetails", default=None
    )
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    """
    Status of object
    """
    total_cost_pool: typing.Optional[float] = pydantic.Field(
        alias="TotalCostPool", default=None
    )
    """
    The value of the item on hand. Calculated using average cost accounting.
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Last modified date in UTC format
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
