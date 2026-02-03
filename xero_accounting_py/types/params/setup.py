import pydantic
import typing
import typing_extensions

from .account import Account, _SerializerAccount
from .conversion_balances import ConversionBalances, _SerializerConversionBalances
from .conversion_date import ConversionDate, _SerializerConversionDate


class Setup(typing_extensions.TypedDict):
    """
    Setup
    """

    accounts: typing_extensions.NotRequired[typing.List[Account]]

    conversion_balances: typing_extensions.NotRequired[typing.List[ConversionBalances]]
    """
    Balance supplied for each account that has a value as at the conversion date.
    """

    conversion_date: typing_extensions.NotRequired[ConversionDate]
    """
    The date when the organisation starts using Xero
    """


class _SerializerSetup(pydantic.BaseModel):
    """
    Serializer for Setup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accounts: typing.Optional[typing.List[_SerializerAccount]] = pydantic.Field(
        alias="Accounts", default=None
    )
    conversion_balances: typing.Optional[typing.List[_SerializerConversionBalances]] = (
        pydantic.Field(alias="ConversionBalances", default=None)
    )
    conversion_date: typing.Optional[_SerializerConversionDate] = pydantic.Field(
        alias="ConversionDate", default=None
    )
