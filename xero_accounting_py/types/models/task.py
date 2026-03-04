import pydantic
import typing
import typing_extensions

from .amount import Amount


class Task(pydantic.BaseModel):
    """
    Task
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="amountInvoiced", default=None
    )
    amount_to_be_invoiced: typing.Optional[Amount] = pydantic.Field(
        alias="amountToBeInvoiced", default=None
    )
    charge_type: typing.Optional[
        typing_extensions.Literal["FIXED", "NON_CHARGEABLE", "TIME"]
    ] = pydantic.Field(alias="chargeType", default=None)
    """
    Can be `TIME`, `FIXED` or `NON_CHARGEABLE`, defines how the task will be charged. Use `TIME` when you want to charge per hour and `FIXED` to charge as a fixed amount. If the task will not be charged use `NON_CHARGEABLE`.
    """
    estimate_minutes: typing.Optional[int] = pydantic.Field(
        alias="estimateMinutes", default=None
    )
    """
    An estimated time to perform the task
    """
    fixed_minutes: typing.Optional[int] = pydantic.Field(
        alias="fixedMinutes", default=None
    )
    """
    Minutes logged against this task if its charge type is `FIXED`.
    """
    minutes_invoiced: typing.Optional[int] = pydantic.Field(
        alias="minutesInvoiced", default=None
    )
    """
    Minutes on this task which have been invoiced.
    """
    minutes_to_be_invoiced: typing.Optional[int] = pydantic.Field(
        alias="minutesToBeInvoiced", default=None
    )
    """
    Minutes on this task which have not been invoiced.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of the task.
    """
    non_chargeable_minutes: typing.Optional[int] = pydantic.Field(
        alias="nonChargeableMinutes", default=None
    )
    """
    Minutes logged against this task if its charge type is `NON_CHARGEABLE`.
    """
    project_id: typing.Optional[str] = pydantic.Field(alias="projectId", default=None)
    """
    Identifier of the project task belongs to.
    """
    rate: typing.Optional[Amount] = pydantic.Field(alias="rate", default=None)
    status: typing.Optional[
        typing_extensions.Literal["ACTIVE", "INVOICED", "LOCKED"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the task. When a task of ChargeType is `FIXED` and the rate amount is invoiced the status will be set to `INVOICED` and can't be modified. A task with ChargeType of `TIME` or `NON_CHARGEABLE` cannot have a status of `INVOICED`. A `LOCKED` state indicates that the task is currently changing state (for example being invoiced) and can't be modified.
    """
    task_id: typing.Optional[str] = pydantic.Field(alias="taskId", default=None)
    """
    Identifier of the task.
    """
    total_amount: typing.Optional[Amount] = pydantic.Field(
        alias="totalAmount", default=None
    )
    total_minutes: typing.Optional[int] = pydantic.Field(
        alias="totalMinutes", default=None
    )
    """
    Total minutes which have been logged against the task. Logged by assigning a time entry to a task
    """
