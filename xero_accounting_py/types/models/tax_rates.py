import pydantic
import typing

from .tax_rate import TaxRate


class TaxRates(pydantic.BaseModel):
    """
    TaxRates
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="TaxRates", default=None
    )
