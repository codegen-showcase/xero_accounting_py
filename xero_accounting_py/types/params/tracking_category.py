import pydantic
import typing
import typing_extensions

from .tracking_option import TrackingOption, _SerializerTrackingOption


class TrackingCategory(typing_extensions.TypedDict):
    """
    TrackingCategory
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the tracking category e.g. Department, Region (max length = 100)
    """

    option: typing_extensions.NotRequired[str]
    """
    The option name of the tracking option e.g. East, West (max length = 100)
    """

    options: typing_extensions.NotRequired[typing.List[TrackingOption]]
    """
    See Tracking Options
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ]
    """
    The status of a tracking category
    """

    tracking_category_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    tracking_option_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
    """


class _SerializerTrackingCategory(pydantic.BaseModel):
    """
    Serializer for TrackingCategory handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    option: typing.Optional[str] = pydantic.Field(alias="Option", default=None)
    options: typing.Optional[typing.List[_SerializerTrackingOption]] = pydantic.Field(
        alias="Options", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ] = pydantic.Field(alias="Status", default=None)
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
