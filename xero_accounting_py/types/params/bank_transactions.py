import pydantic
import typing
import typing_extensions

from .pagination import Pagination, _SerializerPagination
from .validation_error import ValidationError, _SerializerValidationError

if typing_extensions.TYPE_CHECKING:
    from .bank_transaction import BankTransaction, _SerializerBankTransaction


class BankTransactions(typing_extensions.TypedDict):
    """
    BankTransactions
    """

    bank_transactions: typing_extensions.NotRequired[typing.List["BankTransaction"]]

    warnings: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of warning messages from the API
    """

    pagination: typing_extensions.NotRequired[Pagination]


class _SerializerBankTransactions(pydantic.BaseModel):
    """
    Serializer for BankTransactions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transactions: typing.Optional[typing.List["_SerializerBankTransaction"]] = (
        pydantic.Field(alias="BankTransactions", default=None)
    )
    warnings: typing.Optional[typing.List[_SerializerValidationError]] = pydantic.Field(
        alias="Warnings", default=None
    )
    pagination: typing.Optional[_SerializerPagination] = pydantic.Field(
        alias="pagination", default=None
    )
