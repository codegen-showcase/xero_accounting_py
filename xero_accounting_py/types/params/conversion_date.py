import pydantic
import typing
import typing_extensions


class ConversionDate(typing_extensions.TypedDict):
    """
    The date when the organisation starts using Xero
    """

    month: typing_extensions.NotRequired[int]
    """
    The month the organisation starts using Xero. Value is an integer between 1 and 12
    """

    year: typing_extensions.NotRequired[int]
    """
    The year the organisation starts using Xero. Value is an integer greater than 2006
    """


class _SerializerConversionDate(pydantic.BaseModel):
    """
    Serializer for ConversionDate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    month: typing.Optional[int] = pydantic.Field(alias="Month", default=None)
    year: typing.Optional[int] = pydantic.Field(alias="Year", default=None)
