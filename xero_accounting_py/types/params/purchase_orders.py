import pydantic
import typing
import typing_extensions

from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .purchase_order import PurchaseOrder, _SerializerPurchaseOrder


class PurchaseOrders(typing_extensions.TypedDict):
    """
    PurchaseOrders
    """

    purchase_orders: typing_extensions.NotRequired[typing.List["PurchaseOrder"]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerPurchaseOrders(pydantic.BaseModel):
    """
    Serializer for PurchaseOrders handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    purchase_orders: typing.Optional[typing.List["_SerializerPurchaseOrder"]] = (
        pydantic.Field(alias="PurchaseOrders", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
