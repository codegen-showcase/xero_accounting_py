import pydantic
import typing
import typing_extensions


class TrackingOption(typing_extensions.TypedDict):
    """
    TrackingOption
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the tracking option e.g. Marketing, East (max length = 100)
    """

    status: typing_extensions.NotRequired[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ]
    """
    The status of a tracking option
    """

    tracking_category_id: typing_extensions.NotRequired[str]
    """
    Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """

    tracking_option_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
    """


class _SerializerTrackingOption(pydantic.BaseModel):
    """
    Serializer for TrackingOption handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ] = pydantic.Field(alias="Status", default=None)
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
