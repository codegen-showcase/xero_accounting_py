import pydantic
import typing
import typing_extensions

from .account import Account, _SerializerAccount


class Accounts(typing_extensions.TypedDict):
    """
    Accounts
    """

    accounts: typing_extensions.NotRequired[typing.List[Account]]


class _SerializerAccounts(pydantic.BaseModel):
    """
    Serializer for Accounts handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accounts: typing.Optional[typing.List[_SerializerAccount]] = pydantic.Field(
        alias="Accounts", default=None
    )
