import pydantic
import typing


class InvoiceReminder(pydantic.BaseModel):
    """
    InvoiceReminder
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="Enabled", default=None)
    """
    setting for on or off
    """
