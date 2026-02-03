import pydantic
import typing
import typing_extensions

from .validation_error import ValidationError, _SerializerValidationError


class PaymentService(typing_extensions.TypedDict):
    """
    PaymentService
    """

    pay_now_text: typing_extensions.NotRequired[str]
    """
    The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card
    """

    payment_service_id: typing_extensions.NotRequired[str]
    """
    Xero identifier
    """

    payment_service_name: typing_extensions.NotRequired[str]
    """
    Name of payment service
    """

    payment_service_type: typing_extensions.NotRequired[str]
    """
    This will always be CUSTOM for payment services created via the API.
    """

    payment_service_url: typing_extensions.NotRequired[str]
    """
    The custom payment URL
    """

    validation_errors: typing_extensions.NotRequired[typing.List[ValidationError]]
    """
    Displays array of validation error messages from the API
    """


class _SerializerPaymentService(pydantic.BaseModel):
    """
    Serializer for PaymentService handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    pay_now_text: typing.Optional[str] = pydantic.Field(
        alias="PayNowText", default=None
    )
    payment_service_id: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceID", default=None
    )
    payment_service_name: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceName", default=None
    )
    payment_service_type: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceType", default=None
    )
    payment_service_url: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceUrl", default=None
    )
    validation_errors: typing.Optional[typing.List[_SerializerValidationError]] = (
        pydantic.Field(alias="ValidationErrors", default=None)
    )
