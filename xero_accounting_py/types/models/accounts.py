import pydantic
import typing

from .account import Account


class Accounts(pydantic.BaseModel):
    """
    Accounts
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accounts: typing.Optional[typing.List[Account]] = pydantic.Field(
        alias="Accounts", default=None
    )
