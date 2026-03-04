import pydantic
import typing
import typing_extensions


class TimeEntry(pydantic.BaseModel):
    """
    TimeEntry
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date_entered_utc: typing.Optional[str] = pydantic.Field(
        alias="dateEnteredUtc", default=None
    )
    """
    The date time that time entry is created. UTC Date Time in ISO-8601 format. By default it is set to server time.
    """
    date_utc: typing.Optional[str] = pydantic.Field(alias="dateUtc", default=None)
    """
    The date time that time entry is logged on. UTC Date Time in ISO-8601 format.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A description of the time entry.
    """
    duration: typing.Optional[int] = pydantic.Field(alias="duration", default=None)
    """
    The duration of logged minutes.
    """
    project_id: typing.Optional[str] = pydantic.Field(alias="projectId", default=None)
    """
    Identifier of the project, that the task (which the time entry is logged against) belongs to.
    """
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "INVOICED", "LOCKED"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the time entry. By default a time entry is created with status of `ACTIVE`. A `LOCKED` state indicates that the time entry is currently changing state (for example being invoiced). Updates are not allowed when in this state. It will have a status of INVOICED once it is invoiced.
    """
    task_id: typing.Optional[str] = pydantic.Field(alias="taskId", default=None)
    """
    Identifier of the task that time entry is logged against.
    """
    time_entry_id: typing.Optional[str] = pydantic.Field(
        alias="timeEntryId", default=None
    )
    """
    Identifier of the time entry.
    """
    user_id: typing.Optional[str] = pydantic.Field(alias="userId", default=None)
    """
    The xero user identifier of the person who logged time.
    """
