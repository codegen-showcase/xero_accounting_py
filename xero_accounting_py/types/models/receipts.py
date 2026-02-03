import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .receipt import Receipt


class Receipts(pydantic.BaseModel):
    """
    Receipts
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    receipts: typing.Optional[typing.List["Receipt"]] = pydantic.Field(
        alias="Receipts", default=None
    )
