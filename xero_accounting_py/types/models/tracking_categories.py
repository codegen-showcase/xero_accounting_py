import pydantic
import typing

from .tracking_category import TrackingCategory


class TrackingCategories(pydantic.BaseModel):
    """
    TrackingCategories
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tracking_categories: typing.Optional[typing.List[TrackingCategory]] = (
        pydantic.Field(alias="TrackingCategories", default=None)
    )
