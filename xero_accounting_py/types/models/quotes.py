import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quote import Quote


class Quotes(pydantic.BaseModel):
    """
    Quotes
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    quotes: typing.Optional[typing.List["Quote"]] = pydantic.Field(
        alias="Quotes", default=None
    )
