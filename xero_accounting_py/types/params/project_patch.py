import pydantic
import typing_extensions


class ProjectPatch(typing_extensions.TypedDict):
    """
    ProjectPatch
    """

    status: typing_extensions.Required[
        typing_extensions.Literal["CLOSED", "INPROGRESS"]
    ]
    """
    Status for project
    """


class _SerializerProjectPatch(pydantic.BaseModel):
    """
    Serializer for ProjectPatch handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    status: typing_extensions.Literal["CLOSED", "INPROGRESS"] = pydantic.Field(
        alias="status",
    )
