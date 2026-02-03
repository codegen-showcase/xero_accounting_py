import pydantic
import typing
import typing_extensions


class BalanceDetails(typing_extensions.TypedDict):
    """
    An array to specify multiple currency balances of an account
    """

    balance: typing_extensions.NotRequired[float]
    """
    The opening balances of the account. Debits are positive, credits are negative values
    """

    currency_code: typing_extensions.NotRequired[str]
    """
    The currency of the balance (Not required for base currency)
    """

    currency_rate: typing_extensions.NotRequired[float]
    """
    (Optional) Exchange rate to base currency when money is spent or received. If not specified, XE rate for the day is applied
    """


class _SerializerBalanceDetails(pydantic.BaseModel):
    """
    Serializer for BalanceDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    balance: typing.Optional[float] = pydantic.Field(alias="Balance", default=None)
    currency_code: typing.Optional[str] = pydantic.Field(
        alias="CurrencyCode", default=None
    )
    currency_rate: typing.Optional[float] = pydantic.Field(
        alias="CurrencyRate", default=None
    )
