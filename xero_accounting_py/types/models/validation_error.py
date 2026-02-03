import pydantic
import typing


class ValidationError(pydantic.BaseModel):
    """
    ValidationError
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    message: typing.Optional[str] = pydantic.Field(alias="Message", default=None)
    """
    Validation error message
    """
