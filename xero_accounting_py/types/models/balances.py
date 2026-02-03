import pydantic
import typing

from .accounts_payable import AccountsPayable
from .accounts_receivable import AccountsReceivable


class Balances(pydantic.BaseModel):
    """
    The raw AccountsReceivable(sales invoices) and AccountsPayable(bills) outstanding and overdue amounts, not converted to base currency (read only)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accounts_payable: typing.Optional[AccountsPayable] = pydantic.Field(
        alias="AccountsPayable", default=None
    )
    accounts_receivable: typing.Optional[AccountsReceivable] = pydantic.Field(
        alias="AccountsReceivable", default=None
    )
