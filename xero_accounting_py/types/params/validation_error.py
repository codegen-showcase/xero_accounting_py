import pydantic
import typing
import typing_extensions


class ValidationError(typing_extensions.TypedDict):
    """
    ValidationError
    """

    message: typing_extensions.NotRequired[str]
    """
    Validation error message
    """


class _SerializerValidationError(pydantic.BaseModel):
    """
    Serializer for ValidationError handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message: typing.Optional[str] = pydantic.Field(alias="Message", default=None)
