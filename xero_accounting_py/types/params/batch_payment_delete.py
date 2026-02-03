import pydantic
import typing_extensions


class BatchPaymentDelete(typing_extensions.TypedDict):
    """
    BatchPaymentDelete
    """

    batch_payment_id: typing_extensions.Required[str]
    """
    The Xero generated unique identifier for the bank transaction (read-only)
    """

    status: typing_extensions.Required[str]
    """
    The status of the batch payment.
    """


class _SerializerBatchPaymentDelete(pydantic.BaseModel):
    """
    Serializer for BatchPaymentDelete handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    batch_payment_id: str = pydantic.Field(
        alias="BatchPaymentID",
    )
    status: str = pydantic.Field(
        alias="Status",
    )
