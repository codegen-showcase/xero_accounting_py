import pydantic
import typing
import typing_extensions

from .report_cell import ReportCell


class ReportRow(pydantic.BaseModel):
    """
    ReportRow
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cells: typing.Optional[typing.List[ReportCell]] = pydantic.Field(
        alias="Cells", default=None
    )
    row_type: typing.Optional[
        typing_extensions.Literal["Header", "Row", "Section", "SummaryRow"]
    ] = pydantic.Field(alias="RowType", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="Title", default=None)
