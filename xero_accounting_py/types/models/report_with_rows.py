import pydantic
import typing

from .report_with_row import ReportWithRow


class ReportWithRows(pydantic.BaseModel):
    """
    ReportWithRows
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reports: typing.Optional[typing.List[ReportWithRow]] = pydantic.Field(
        alias="Reports", default=None
    )
