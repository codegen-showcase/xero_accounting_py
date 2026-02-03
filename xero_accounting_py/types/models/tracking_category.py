import pydantic
import typing
import typing_extensions

from .tracking_option import TrackingOption


class TrackingCategory(pydantic.BaseModel):
    """
    TrackingCategory
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the tracking category e.g. Department, Region (max length = 100)
    """
    option: typing.Optional[str] = pydantic.Field(alias="Option", default=None)
    """
    The option name of the tracking option e.g. East, West (max length = 100)
    """
    options: typing.Optional[typing.List[TrackingOption]] = pydantic.Field(
        alias="Options", default=None
    )
    """
    See Tracking Options
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    The status of a tracking category
    """
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    """
    The Xero identifier for a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
    """
    The Xero identifier for a tracking option e.g. dc54c220-0140-495a-b925-3246adc0075f
    """
