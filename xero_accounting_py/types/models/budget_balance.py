import pydantic
import typing


class BudgetBalance(pydantic.BaseModel):
    """
    BudgetBalance
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: typing.Optional[float] = pydantic.Field(alias="Amount", default=None)
    """
    LineItem Quantity
    """
    notes: typing.Optional[str] = pydantic.Field(alias="Notes", default=None)
    """
    Any footnotes associated with this balance
    """
    period: typing.Optional[str] = pydantic.Field(alias="Period", default=None)
    """
    Period the amount applies to (e.g. “2019-08”)
    """
    unit_amount: typing.Optional[float] = pydantic.Field(
        alias="UnitAmount", default=None
    )
    """
    Budgeted amount
    """
