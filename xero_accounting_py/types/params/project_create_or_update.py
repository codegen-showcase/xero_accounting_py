import pydantic
import typing
import typing_extensions


class ProjectCreateOrUpdate(typing_extensions.TypedDict):
    """
    ProjectCreateOrUpdate
    """

    contact_id: typing_extensions.NotRequired[str]
    """
    Identifier of the contact this project was created for.
    """

    deadline_utc: typing_extensions.NotRequired[str]
    """
    Deadline for the project. UTC Date Time in ISO-8601 format.
    """

    estimate_amount: typing_extensions.NotRequired[float]

    name: typing_extensions.Required[str]
    """
    Name of the project.
    """


class _SerializerProjectCreateOrUpdate(pydantic.BaseModel):
    """
    Serializer for ProjectCreateOrUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_id: typing.Optional[str] = pydantic.Field(alias="contactId", default=None)
    deadline_utc: typing.Optional[str] = pydantic.Field(
        alias="deadlineUtc", default=None
    )
    estimate_amount: typing.Optional[float] = pydantic.Field(
        alias="estimateAmount", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
