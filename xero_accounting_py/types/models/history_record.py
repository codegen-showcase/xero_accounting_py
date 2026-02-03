import pydantic
import typing


class HistoryRecord(pydantic.BaseModel):
    """
    HistoryRecord
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    changes: typing.Optional[str] = pydantic.Field(alias="Changes", default=None)
    """
    Name of branding theme
    """
    date_utc: typing.Optional[str] = pydantic.Field(alias="DateUTC", default=None)
    """
    UTC timestamp of creation date of branding theme
    """
    details: typing.Optional[str] = pydantic.Field(alias="Details", default=None)
    """
    details
    """
    user: typing.Optional[str] = pydantic.Field(alias="User", default=None)
    """
    has a value of 0
    """
