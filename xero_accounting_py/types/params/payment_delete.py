import pydantic
import typing_extensions


class PaymentDelete(typing_extensions.TypedDict):
    """
    PaymentDelete
    """

    status: typing_extensions.Required[str]
    """
    The status of the payment.
    """


class _SerializerPaymentDelete(pydantic.BaseModel):
    """
    Serializer for PaymentDelete handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    status: str = pydantic.Field(
        alias="Status",
    )
