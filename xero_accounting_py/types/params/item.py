import pydantic
import typing
import typing_extensions

from .purchase import Purchase, _SerializerPurchase
from .validation_error import ValidationError, _SerializerValidationError


class Item(typing_extensions.TypedDict):
    """
    Item
    """

    code: typing_extensions.Required[str]
    """
    User defined item code (max length = 30)
    """

    description: typing_extensions.NotRequired[str]
    """
    The sales description of the item (max length = 4000)
    """

    inventory_asset_account_code: typing_extensions.NotRequired[str]
    """
    The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item
    """

    is_purchased: typing_extensions.NotRequired[bool]
    """
    Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled.
    """

    is_sold: typing_extensions.NotRequired[bool]
    """
    Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled.
    """

    is_tracked_as_inventory: typing_extensions.NotRequired[bool]
    """
    True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set.
    """

    item_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for an Item
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the item (max length = 50)
    """

    purchase_description: typing_extensions.NotRequired[str]
    """
    The purchase description of the item (max length = 4000)
    """

    purchase_details: typing_extensions.NotRequired[Purchase]

    quantity_on_hand: typing_extensions.NotRequired[float]
    """
    The quantity of the item on hand
    """

    sales_details: typing_extensions.NotRequired[Purchase]

    status_attribute_string: typing_extensions.NotRequired[str]
    """
    Status of object
    """

    total_cost_pool: typing_extensions.NotRequired[float]
    """
    The value of the item on hand. Calculated using average cost accounting.
    """

    updated_date_utc: typing_extensions.NotRequired[str]
    """
    Last modified date in UTC format
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerItem(pydantic.BaseModel):
    """
    Serializer for Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    code: str = pydantic.Field(
        alias="Code",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    inventory_asset_account_code: typing.Optional[str] = pydantic.Field(
        alias="InventoryAssetAccountCode", default=None
    )
    is_purchased: typing.Optional[bool] = pydantic.Field(
        alias="IsPurchased", default=None
    )
    is_sold: typing.Optional[bool] = pydantic.Field(alias="IsSold", default=None)
    is_tracked_as_inventory: typing.Optional[bool] = pydantic.Field(
        alias="IsTrackedAsInventory", default=None
    )
    item_id: typing.Optional[str] = pydantic.Field(alias="ItemID", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    purchase_description: typing.Optional[str] = pydantic.Field(
        alias="PurchaseDescription", default=None
    )
    purchase_details: typing.Optional[_SerializerPurchase] = pydantic.Field(
        alias="PurchaseDetails", default=None
    )
    quantity_on_hand: typing.Optional[float] = pydantic.Field(
        alias="QuantityOnHand", default=None
    )
    sales_details: typing.Optional[_SerializerPurchase] = pydantic.Field(
        alias="SalesDetails", default=None
    )
    status_attribute_string: typing.Optional[str] = pydantic.Field(
        alias="StatusAttributeString", default=None
    )
    total_cost_pool: typing.Optional[float] = pydantic.Field(
        alias="TotalCostPool", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
