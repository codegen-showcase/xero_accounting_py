import pydantic
import typing

from .linked_transaction import LinkedTransaction


class LinkedTransactions(pydantic.BaseModel):
    """
    LinkedTransactions
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    linked_transactions: typing.Optional[typing.List[LinkedTransaction]] = (
        pydantic.Field(alias="LinkedTransactions", default=None)
    )
