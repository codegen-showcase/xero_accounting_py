import pydantic
import typing


class SalesTrackingCategory(pydantic.BaseModel):
    """
    SalesTrackingCategory
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tracking_category_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryName", default=None
    )
    """
    The default sales tracking category name for contacts
    """
    tracking_option_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionName", default=None
    )
    """
    The default purchase tracking category name for contacts
    """
