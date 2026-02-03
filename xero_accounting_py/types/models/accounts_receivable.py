import pydantic
import typing


class AccountsReceivable(pydantic.BaseModel):
    """
    AccountsReceivable
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    outstanding: typing.Optional[float] = pydantic.Field(
        alias="Outstanding", default=None
    )
    overdue: typing.Optional[float] = pydantic.Field(alias="Overdue", default=None)
