import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .repeating_invoice import RepeatingInvoice, _SerializerRepeatingInvoice


class RepeatingInvoices(typing_extensions.TypedDict):
    """
    RepeatingInvoices
    """

    repeating_invoices: typing_extensions.NotRequired[typing.List["RepeatingInvoice"]]


class _SerializerRepeatingInvoices(pydantic.BaseModel):
    """
    Serializer for RepeatingInvoices handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    repeating_invoices: typing.Optional[typing.List["_SerializerRepeatingInvoice"]] = (
        pydantic.Field(alias="RepeatingInvoices", default=None)
    )
