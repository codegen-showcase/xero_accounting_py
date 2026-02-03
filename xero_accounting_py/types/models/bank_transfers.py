import pydantic
import typing

from .bank_transfer import BankTransfer


class BankTransfers(pydantic.BaseModel):
    """
    BankTransfers
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_transfers: typing.Optional[typing.List[BankTransfer]] = pydantic.Field(
        alias="BankTransfers", default=None
    )
