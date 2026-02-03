import pydantic
import typing
import typing_extensions


class Schedule(pydantic.BaseModel):
    """
    Schedule
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    due_date: typing.Optional[int] = pydantic.Field(alias="DueDate", default=None)
    """
    Integer used with due date type e.g 20 (of following month), 31 (of current month)
    """
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
    """
    the payment terms
    """
    end_date: typing.Optional[str] = pydantic.Field(alias="EndDate", default=None)
    """
    Invoice end date – only returned if the template has an end date set
    """
    next_scheduled_date: typing.Optional[str] = pydantic.Field(
        alias="NextScheduledDate", default=None
    )
    """
    The calendar date of the next invoice in the schedule to be generated
    """
    period: typing.Optional[int] = pydantic.Field(alias="Period", default=None)
    """
    Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months)
    """
    start_date: typing.Optional[str] = pydantic.Field(alias="StartDate", default=None)
    """
    Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited)
    """
    unit: typing.Optional[typing_extensions.Literal["MONTHLY", "WEEKLY"]] = (
        pydantic.Field(alias="Unit", default=None)
    )
    """
    One of the following - WEEKLY or MONTHLY
    """
