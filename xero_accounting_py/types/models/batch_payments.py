import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .batch_payment import BatchPayment


class BatchPayments(pydantic.BaseModel):
    """
    BatchPayments
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    batch_payments: typing.Optional[typing.List["BatchPayment"]] = pydantic.Field(
        alias="BatchPayments", default=None
    )
