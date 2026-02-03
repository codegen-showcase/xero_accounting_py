import pydantic
import typing

from .validation_error import ValidationError


class PaymentService(pydantic.BaseModel):
    """
    PaymentService
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    pay_now_text: typing.Optional[str] = pydantic.Field(
        alias="PayNowText", default=None
    )
    """
    The text displayed on the Pay Now button in Xero Online Invoicing. If this is not set it will default to Pay by credit card
    """
    payment_service_id: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceID", default=None
    )
    """
    Xero identifier
    """
    payment_service_name: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceName", default=None
    )
    """
    Name of payment service
    """
    payment_service_type: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceType", default=None
    )
    """
    This will always be CUSTOM for payment services created via the API.
    """
    payment_service_url: typing.Optional[str] = pydantic.Field(
        alias="PaymentServiceUrl", default=None
    )
    """
    The custom payment URL
    """
    validation_errors: typing.Optional[typing.List[ValidationError]] = pydantic.Field(
        alias="ValidationErrors", default=None
    )
    """
    Displays array of validation error messages from the API
    """
