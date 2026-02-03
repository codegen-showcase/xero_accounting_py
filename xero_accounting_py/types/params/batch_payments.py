import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .batch_payment import BatchPayment, _SerializerBatchPayment


class BatchPayments(typing_extensions.TypedDict):
    """
    BatchPayments
    """

    batch_payments: typing_extensions.NotRequired[typing.List["BatchPayment"]]


class _SerializerBatchPayments(pydantic.BaseModel):
    """
    Serializer for BatchPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    batch_payments: typing.Optional[typing.List["_SerializerBatchPayment"]] = (
        pydantic.Field(alias="BatchPayments", default=None)
    )
