import pydantic
import typing
import typing_extensions

from .bank_transfer import BankTransfer, _SerializerBankTransfer


class BankTransfers(typing_extensions.TypedDict):
    """
    BankTransfers
    """

    bank_transfers: typing_extensions.NotRequired[typing.List[BankTransfer]]


class _SerializerBankTransfers(pydantic.BaseModel):
    """
    Serializer for BankTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfers: typing.Optional[typing.List[_SerializerBankTransfer]] = (
        pydantic.Field(alias="BankTransfers", default=None)
    )
