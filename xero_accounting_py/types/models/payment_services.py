import pydantic
import typing

from .payment_service import PaymentService


class PaymentServices(pydantic.BaseModel):
    """
    PaymentServices
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_services: typing.Optional[typing.List[PaymentService]] = pydantic.Field(
        alias="PaymentServices", default=None
    )
