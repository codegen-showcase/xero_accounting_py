import pydantic
import typing
import typing_extensions


class LineItemTracking1(typing_extensions.TypedDict):
    """
    LineItemTracking1
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the tracking category
    """

    option: typing_extensions.NotRequired[str]
    """
    See Tracking Options
    """

    tracking_category_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a tracking category
    """

    tracking_option_id: typing_extensions.NotRequired[str]
    """
    The Xero identifier for a tracking category option
    """


class _SerializerLineItemTracking1(pydantic.BaseModel):
    """
    Serializer for LineItemTracking1 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    option: typing.Optional[str] = pydantic.Field(alias="Option", default=None)
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
