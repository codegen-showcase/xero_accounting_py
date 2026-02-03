import pydantic
import typing
import typing_extensions

from .ten_ninety_nine_contact import TenNinetyNineContact


class Report(pydantic.BaseModel):
    """
    Report
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contacts: typing.Optional[typing.List[TenNinetyNineContact]] = pydantic.Field(
        alias="Contacts", default=None
    )
    report_date: typing.Optional[str] = pydantic.Field(alias="ReportDate", default=None)
    """
    Date of report
    """
    report_name: typing.Optional[str] = pydantic.Field(alias="ReportName", default=None)
    """
    See Prepayment Types
    """
    report_title: typing.Optional[str] = pydantic.Field(
        alias="ReportTitle", default=None
    )
    """
    See Prepayment Types
    """
    report_type: typing.Optional[typing_extensions.Literal["AgedPayablesByContact"]] = (
        pydantic.Field(alias="ReportType", default=None)
    )
    """
    See Prepayment Types
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    Updated Date
    """
