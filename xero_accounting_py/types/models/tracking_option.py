import pydantic
import typing
import typing_extensions


class TrackingOption(pydantic.BaseModel):
    """
    TrackingOption
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the tracking option e.g. Marketing, East (max length = 100)
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "ARCHIVED", "DELETED"]
    ] = pydantic.Field(alias="Status", default=None)
    """
    The status of a tracking option
    """
    tracking_category_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryID", default=None
    )
    """
    Filter by a tracking category e.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9
    """
    tracking_option_id: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionID", default=None
    )
    """
    The Xero identifier for a tracking option e.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a
    """
