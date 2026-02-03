import pydantic
import typing


class ReportFields(pydantic.BaseModel):
    """
    ReportFields
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    field_id: typing.Optional[str] = pydantic.Field(alias="FieldID", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="Value", default=None)
