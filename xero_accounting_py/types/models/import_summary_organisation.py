import pydantic
import typing


class ImportSummaryOrganisation(pydantic.BaseModel):
    """
    ImportSummaryOrganisation
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    present: typing.Optional[bool] = pydantic.Field(alias="Present", default=None)
