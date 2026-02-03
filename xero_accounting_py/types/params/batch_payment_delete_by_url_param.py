import pydantic
import typing_extensions


class BatchPaymentDeleteByUrlParam(typing_extensions.TypedDict):
    """
    BatchPaymentDeleteByUrlParam
    """

    status: typing_extensions.Required[str]
    """
    The status of the batch payment.
    """


class _SerializerBatchPaymentDeleteByUrlParam(pydantic.BaseModel):
    """
    Serializer for BatchPaymentDeleteByUrlParam handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    status: str = pydantic.Field(
        alias="Status",
    )
