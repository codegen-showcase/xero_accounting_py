import pydantic
import typing
import typing_extensions

from .bill import Bill, _SerializerBill


class PaymentTerm(typing_extensions.TypedDict):
    """
    PaymentTerm
    """

    bills: typing_extensions.NotRequired[Bill]

    sales: typing_extensions.NotRequired[Bill]


class _SerializerPaymentTerm(pydantic.BaseModel):
    """
    Serializer for PaymentTerm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bills: typing.Optional[_SerializerBill] = pydantic.Field(
        alias="Bills", default=None
    )
    sales: typing.Optional[_SerializerBill] = pydantic.Field(
        alias="Sales", default=None
    )
