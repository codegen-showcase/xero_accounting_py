import pydantic
import typing

from .report import Report


class Reports(pydantic.BaseModel):
    """
    Reports
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reports: typing.Optional[typing.List[Report]] = pydantic.Field(
        alias="Reports", default=None
    )
