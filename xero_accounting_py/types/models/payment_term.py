import pydantic
import typing

from .bill import Bill


class PaymentTerm(pydantic.BaseModel):
    """
    PaymentTerm
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bills: typing.Optional[Bill] = pydantic.Field(alias="Bills", default=None)
    sales: typing.Optional[Bill] = pydantic.Field(alias="Sales", default=None)
