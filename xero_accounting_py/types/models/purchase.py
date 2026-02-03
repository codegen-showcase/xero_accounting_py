import pydantic
import typing


class Purchase(pydantic.BaseModel):
    """
    Purchase
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    """
    Default account code to be used for purchased/sale. Not applicable to the purchase details of tracked items
    """
    cogs_account_code: typing.Optional[str] = pydantic.Field(
        alias="COGSAccountCode", default=None
    )
    """
    Cost of goods sold account. Only applicable to the purchase details of tracked items.
    """
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    """
    The tax type from TaxRates
    """
    unit_price: typing.Optional[float] = pydantic.Field(alias="UnitPrice", default=None)
    """
    Unit Price of the item. By default UnitPrice is rounded to two decimal places. You can use 4 decimal places by adding the unitdp=4 querystring parameter to your request.
    """
