import pydantic
import typing

from .report_fields import ReportFields
from .report_rows import ReportRows


class ReportWithRow(pydantic.BaseModel):
    """
    ReportWithRow
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fields: typing.Optional[typing.List[ReportFields]] = pydantic.Field(
        alias="Fields", default=None
    )
    report_date: typing.Optional[str] = pydantic.Field(alias="ReportDate", default=None)
    """
    Date of report
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="ReportID", default=None)
    """
    ID of the Report
    """
    report_name: typing.Optional[str] = pydantic.Field(alias="ReportName", default=None)
    """
    Name of the report
    """
    report_title: typing.Optional[str] = pydantic.Field(
        alias="ReportTitle", default=None
    )
    """
    Title of the report
    """
    report_titles: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="ReportTitles", default=None
    )
    """
    Report titles array (3 to 4 strings with the report name, orgnisation name and time frame of report)
    """
    report_type: typing.Optional[str] = pydantic.Field(alias="ReportType", default=None)
    """
    The type of report (BalanceSheet,ProfitLoss, etc)
    """
    rows: typing.Optional[typing.List[ReportRows]] = pydantic.Field(
        alias="Rows", default=None
    )
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Updated Date
    """
