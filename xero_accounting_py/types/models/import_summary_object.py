import pydantic
import typing

from .import_summary import ImportSummary


class ImportSummaryObject(pydantic.BaseModel):
    """
    ImportSummaryObject
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    import_summary: typing.Optional[ImportSummary] = pydantic.Field(
        alias="ImportSummary", default=None
    )
    """
    A summary of the import from setup endpoint
    """
