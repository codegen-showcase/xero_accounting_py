import pydantic
import typing
import typing_extensions

from .accounts_payable import AccountsPayable, _SerializerAccountsPayable
from .accounts_receivable import AccountsReceivable, _SerializerAccountsReceivable


class Balances(typing_extensions.TypedDict):
    """
    The raw AccountsReceivable(sales invoices) and AccountsPayable(bills) outstanding and overdue amounts, not converted to base currency (read only)
    """

    accounts_payable: typing_extensions.NotRequired[AccountsPayable]

    accounts_receivable: typing_extensions.NotRequired[AccountsReceivable]


class _SerializerBalances(pydantic.BaseModel):
    """
    Serializer for Balances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accounts_payable: typing.Optional[_SerializerAccountsPayable] = pydantic.Field(
        alias="AccountsPayable", default=None
    )
    accounts_receivable: typing.Optional[_SerializerAccountsReceivable] = (
        pydantic.Field(alias="AccountsReceivable", default=None)
    )
