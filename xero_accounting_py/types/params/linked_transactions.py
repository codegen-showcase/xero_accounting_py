import pydantic
import typing
import typing_extensions

from .linked_transaction import LinkedTransaction, _SerializerLinkedTransaction


class LinkedTransactions(typing_extensions.TypedDict):
    """
    LinkedTransactions
    """

    linked_transactions: typing_extensions.NotRequired[typing.List[LinkedTransaction]]


class _SerializerLinkedTransactions(pydantic.BaseModel):
    """
    Serializer for LinkedTransactions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    linked_transactions: typing.Optional[typing.List[_SerializerLinkedTransaction]] = (
        pydantic.Field(alias="LinkedTransactions", default=None)
    )
