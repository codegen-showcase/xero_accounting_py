import pydantic
import typing
import typing_extensions


class Purchase(typing_extensions.TypedDict):
    """
    Purchase
    """

    account_code: typing_extensions.NotRequired[str]
    """
    Default account code to be used for purchased/sale. Not applicable to the purchase details of tracked items
    """

    cogs_account_code: typing_extensions.NotRequired[str]
    """
    Cost of goods sold account. Only applicable to the purchase details of tracked items.
    """

    tax_type: typing_extensions.NotRequired[str]
    """
    The tax type from TaxRates
    """

    unit_price: typing_extensions.NotRequired[float]
    """
    Unit Price of the item. By default UnitPrice is rounded to two decimal places. You can use 4 decimal places by adding the unitdp=4 querystring parameter to your request.
    """


class _SerializerPurchase(pydantic.BaseModel):
    """
    Serializer for Purchase handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_code: typing.Optional[str] = pydantic.Field(
        alias="AccountCode", default=None
    )
    cogs_account_code: typing.Optional[str] = pydantic.Field(
        alias="COGSAccountCode", default=None
    )
    tax_type: typing.Optional[str] = pydantic.Field(alias="TaxType", default=None)
    unit_price: typing.Optional[float] = pydantic.Field(alias="UnitPrice", default=None)
