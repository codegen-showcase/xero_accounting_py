import pydantic
import typing
import typing_extensions


class RequestEmpty(typing_extensions.TypedDict):
    """
    RequestEmpty
    """

    status: typing_extensions.NotRequired[str]
    """
    Need at least one field to create an empty JSON payload
    """


class _SerializerRequestEmpty(pydantic.BaseModel):
    """
    Serializer for RequestEmpty handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    status: typing.Optional[str] = pydantic.Field(alias="Status", default=None)
