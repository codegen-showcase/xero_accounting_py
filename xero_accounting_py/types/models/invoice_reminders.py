import pydantic
import typing

from .invoice_reminder import InvoiceReminder


class InvoiceReminders(pydantic.BaseModel):
    """
    InvoiceReminders
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    invoice_reminders: typing.Optional[typing.List[InvoiceReminder]] = pydantic.Field(
        alias="InvoiceReminders", default=None
    )
