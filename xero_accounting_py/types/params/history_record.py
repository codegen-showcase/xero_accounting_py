import pydantic
import typing
import typing_extensions


class HistoryRecord(typing_extensions.TypedDict):
    """
    HistoryRecord
    """

    changes: typing_extensions.NotRequired[str]
    """
    Name of branding theme
    """

    date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of creation date of branding theme
    """

    details: typing_extensions.NotRequired[str]
    """
    details
    """

    user: typing_extensions.NotRequired[str]
    """
    has a value of 0
    """


class _SerializerHistoryRecord(pydantic.BaseModel):
    """
    Serializer for HistoryRecord handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    changes: typing.Optional[str] = pydantic.Field(alias="Changes", default=None)
    date_utc: typing.Optional[str] = pydantic.Field(alias="DateUTC", default=None)
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    user: typing.Optional[str] = pydantic.Field(alias="User", default=None)
