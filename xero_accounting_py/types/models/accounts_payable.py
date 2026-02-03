import pydantic
import typing


class AccountsPayable(pydantic.BaseModel):
    """
    AccountsPayable
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    outstanding: typing.Optional[float] = pydantic.Field(
        alias="Outstanding", default=None
    )
    overdue: typing.Optional[float] = pydantic.Field(alias="Overdue", default=None)
