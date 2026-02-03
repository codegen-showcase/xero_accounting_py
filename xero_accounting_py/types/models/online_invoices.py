import pydantic
import typing

from .online_invoice import OnlineInvoice


class OnlineInvoices(pydantic.BaseModel):
    """
    OnlineInvoices
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    online_invoices: typing.Optional[typing.List[OnlineInvoice]] = pydantic.Field(
        alias="OnlineInvoices", default=None
    )
