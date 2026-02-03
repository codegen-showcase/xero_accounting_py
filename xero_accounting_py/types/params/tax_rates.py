import pydantic
import typing
import typing_extensions

from .tax_rate import TaxRate, _SerializerTaxRate


class TaxRates(typing_extensions.TypedDict):
    """
    TaxRates
    """

    tax_rates: typing_extensions.NotRequired[typing.List[TaxRate]]


class _SerializerTaxRates(pydantic.BaseModel):
    """
    Serializer for TaxRates handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_rates: typing.Optional[typing.List[_SerializerTaxRate]] = pydantic.Field(
        alias="TaxRates", default=None
    )
