import pydantic
import typing
import typing_extensions

from .balance_details import BalanceDetails, _SerializerBalanceDetails


class ConversionBalances(typing_extensions.TypedDict):
    """
    Balance supplied for each account that has a value as at the conversion date.
    """

    account_code: typing_extensions.NotRequired[str]
    """
    The account code for a account
    """

    balance: typing_extensions.NotRequired[float]
    """
    The opening balances of the account. Debits are positive, credits are negative values
    """

    balance_details: typing_extensions.NotRequired[typing.List[BalanceDetails]]


class _SerializerConversionBalances(pydantic.BaseModel):
    """
    Serializer for ConversionBalances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    balance: typing.Optional[float] = pydantic.Field(alias="Balance", default=None)
    balance_details: typing.Optional[typing.List[_SerializerBalanceDetails]] = (
        pydantic.Field(alias="BalanceDetails", default=None)
    )
