import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .repeating_invoice import RepeatingInvoice


class RepeatingInvoices(pydantic.BaseModel):
    """
    RepeatingInvoices
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    repeating_invoices: typing.Optional[typing.List["RepeatingInvoice"]] = (
        pydantic.Field(alias="RepeatingInvoices", default=None)
    )
