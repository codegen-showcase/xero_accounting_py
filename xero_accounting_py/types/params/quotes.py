import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quote import Quote, _SerializerQuote


class Quotes(typing_extensions.TypedDict):
    """
    Quotes
    """

    quotes: typing_extensions.NotRequired[typing.List["Quote"]]


class _SerializerQuotes(pydantic.BaseModel):
    """
    Serializer for Quotes handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    quotes: typing.Optional[typing.List["_SerializerQuote"]] = pydantic.Field(
        alias="Quotes", default=None
    )
