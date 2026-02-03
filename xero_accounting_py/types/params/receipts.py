import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .receipt import Receipt, _SerializerReceipt


class Receipts(typing_extensions.TypedDict):
    """
    Receipts
    """

    receipts: typing_extensions.NotRequired[typing.List["Receipt"]]


class _SerializerReceipts(pydantic.BaseModel):
    """
    Serializer for Receipts handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    receipts: typing.Optional[typing.List["_SerializerReceipt"]] = pydantic.Field(
        alias="Receipts", default=None
    )
