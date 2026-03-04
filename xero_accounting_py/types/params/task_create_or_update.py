import pydantic
import typing
import typing_extensions

from .amount import Amount, _SerializerAmount


class TaskCreateOrUpdate(typing_extensions.TypedDict):
    """
    TaskCreateOrUpdate
    """

    charge_type: typing_extensions.Required[
        typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"]
    ]
    """
    Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
    """

    estimate_minutes: typing_extensions.NotRequired[int]
    """
    An estimated time to perform the task
    """

    name: typing_extensions.Required[str]
    """
    Name of the task. Max length 100 characters.
    """

    rate: typing_extensions.Required[Amount]


class _SerializerTaskCreateOrUpdate(pydantic.BaseModel):
    """
    Serializer for TaskCreateOrUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    charge_type: typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"] = (
        pydantic.Field(
            alias="chargeType",
        )
    )
    estimate_minutes: typing.Optional[int] = pydantic.Field(
        alias="estimateMinutes", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    rate: _SerializerAmount = pydantic.Field(
        alias="rate",
    )
