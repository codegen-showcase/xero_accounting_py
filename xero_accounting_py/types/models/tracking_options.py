import pydantic
import typing

from .tracking_option import TrackingOption


class TrackingOptions(pydantic.BaseModel):
    """
    TrackingOptions
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    options: typing.Optional[typing.List[TrackingOption]] = pydantic.Field(
        alias="Options", default=None
    )
