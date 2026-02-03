import pydantic
import typing

from .currency import Currency


class Currencies(pydantic.BaseModel):
    """
    Currencies
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currencies: typing.Optional[typing.List[Currency]] = pydantic.Field(
        alias="Currencies", default=None
    )
