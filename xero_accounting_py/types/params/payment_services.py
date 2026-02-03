import pydantic
import typing
import typing_extensions

from .payment_service import PaymentService, _SerializerPaymentService


class PaymentServices(typing_extensions.TypedDict):
    """
    PaymentServices
    """

    payment_services: typing_extensions.NotRequired[typing.List[PaymentService]]


class _SerializerPaymentServices(pydantic.BaseModel):
    """
    Serializer for PaymentServices handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payment_services: typing.Optional[typing.List[_SerializerPaymentService]] = (
        pydantic.Field(alias="PaymentServices", default=None)
    )
