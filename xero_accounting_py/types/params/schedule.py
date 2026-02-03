import pydantic
import typing
import typing_extensions


class Schedule(typing_extensions.TypedDict):
    """
    Schedule
    """

    due_date: typing_extensions.NotRequired[int]
    """
    Integer used with due date type e.g 20 (of following month), 31 (of current month)
    """

    due_date_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "DAYSAFTERINVOICEDATE",
            "DAYSAFTERINVOICEMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
        ]
    ]
    """
    the payment terms
    """

    end_date: typing_extensions.NotRequired[str]
    """
    Invoice end date – only returned if the template has an end date set
    """

    next_scheduled_date: typing_extensions.NotRequired[str]
    """
    The calendar date of the next invoice in the schedule to be generated
    """

    period: typing_extensions.NotRequired[int]
    """
    Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months)
    """

    start_date: typing_extensions.NotRequired[str]
    """
    Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited)
    """

    unit: typing_extensions.NotRequired[typing_extensions.Literal["MONTHLY", "WEEKLY"]]
    """
    One of the following - WEEKLY or MONTHLY
    """


class _SerializerSchedule(pydantic.BaseModel):
    """
    Serializer for Schedule handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    due_date: typing.Optional[int] = pydantic.Field(alias="DueDate", default=None)
    due_date_type: typing.Optional[
        typing_extensions.Literal[
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "DAYSAFTERINVOICEDATE",
            "DAYSAFTERINVOICEMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
        ]
    ] = pydantic.Field(alias="DueDateType", default=None)
    end_date: typing.Optional[str] = pydantic.Field(alias="EndDate", default=None)
    next_scheduled_date: typing.Optional[str] = pydantic.Field(
        alias="NextScheduledDate", default=None
    )
    period: typing.Optional[int] = pydantic.Field(alias="Period", default=None)
    start_date: typing.Optional[str] = pydantic.Field(alias="StartDate", default=None)
    unit: typing.Optional[typing_extensions.Literal["MONTHLY", "WEEKLY"]] = (
        pydantic.Field(alias="Unit", default=None)
    )
