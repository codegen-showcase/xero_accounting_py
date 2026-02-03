import pydantic
import typing

from .report_attribute import ReportAttribute


class ReportCell(pydantic.BaseModel):
    """
    ReportCell
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[typing.List[ReportAttribute]] = pydantic.Field(
        alias="Attributes", default=None
    )
    value: typing.Optional[str] = pydantic.Field(alias="Value", default=None)
