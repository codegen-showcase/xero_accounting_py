import pydantic
import typing


class LineItemTracking1(pydantic.BaseModel):
    """
    LineItemTracking1
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the tracking category
    """
    option: typing.Optional[str] = pydantic.Field(alias="Option", default=None)
    """
    See Tracking Options
    """
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    """
    The Xero identifier for a tracking category
    """
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
    """
    The Xero identifier for a tracking category option
    """
