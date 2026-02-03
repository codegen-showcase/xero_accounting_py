import pydantic
import typing
import typing_extensions

from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .invoice import Invoice, _SerializerInvoice


class Invoices(typing_extensions.TypedDict):
    """
    Invoices
    """

    invoices: typing_extensions.NotRequired[typing.List["Invoice"]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerInvoices(pydantic.BaseModel):
    """
    Serializer for Invoices handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    invoices: typing.Optional[typing.List["_SerializerInvoice"]] = pydantic.Field(
        alias="Invoices", default=None
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
