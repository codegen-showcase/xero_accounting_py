import pydantic
import typing
import typing_extensions


class TimeEntryCreateOrUpdate(typing_extensions.TypedDict):
    """
    TimeEntryCreateOrUpdate
    """

    date_utc: typing_extensions.Required[str]
    """
    Date time entry is logged on. UTC Date Time in ISO-8601 format.
    """

    description: typing_extensions.NotRequired[str]
    """
    An optional description of the time entry, will be set to null if not provided during update.
    """

    duration: typing_extensions.Required[int]
    """
    Number of minutes to be logged. Duration is between 1 and 59940 inclusively.
    """

    task_id: typing_extensions.Required[str]
    """
    Identifier of the task that time entry is logged against.
    """

    user_id: typing_extensions.Required[str]
    """
    The xero user identifier of the person logging the time.
    """


class _SerializerTimeEntryCreateOrUpdate(pydantic.BaseModel):
    """
    Serializer for TimeEntryCreateOrUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date_utc: str = pydantic.Field(
        alias="dateUtc",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    duration: int = pydantic.Field(
        alias="duration",
    )
    task_id: str = pydantic.Field(
        alias="taskId",
    )
    user_id: str = pydantic.Field(
        alias="userId",
    )
