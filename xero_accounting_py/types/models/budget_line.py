import pydantic
import typing

from .budget_balance import BudgetBalance


class BudgetLine(pydantic.BaseModel):
    """
    BudgetLine
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    """
    See Accounts
    """
    account_id: typing.Optional[str] = pydantic.Field(alias="AccountID", default=None)
    """
    See Accounts
    """
    budget_balances: typing.Optional[typing.List[BudgetBalance]] = pydantic.Field(
        alias="BudgetBalances", default=None
    )
