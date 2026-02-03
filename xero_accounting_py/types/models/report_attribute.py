import pydantic
import typing


class ReportAttribute(pydantic.BaseModel):
    """
    ReportAttribute
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = pydantic.Field(alias="Id", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="Value", default=None)
