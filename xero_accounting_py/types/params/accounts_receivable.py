import pydantic
import typing
import typing_extensions


class AccountsReceivable(typing_extensions.TypedDict):
    """
    AccountsReceivable
    """

    outstanding: typing_extensions.NotRequired[float]

    overdue: typing_extensions.NotRequired[float]


class _SerializerAccountsReceivable(pydantic.BaseModel):
    """
    Serializer for AccountsReceivable handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    outstanding: typing.Optional[float] = pydantic.Field(
        alias="Outstanding", default=None
    )
    overdue: typing.Optional[float] = pydantic.Field(alias="Overdue", default=None)
