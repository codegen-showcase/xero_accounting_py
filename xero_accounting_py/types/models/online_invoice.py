import pydantic
import typing


class OnlineInvoice(pydantic.BaseModel):
    """
    OnlineInvoice
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    online_invoice_url: typing.Optional[str] = pydantic.Field(
        alias="OnlineInvoiceUrl", default=None
    )
    """
    the URL to an online invoice
    """
