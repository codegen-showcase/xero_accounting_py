import pydantic
import typing
import typing_extensions


class TaxBreakdownComponent(pydantic.BaseModel):
    """
    TaxBreakdownComponent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    exempt_amount: typing.Optional[float] = pydantic.Field(
        alias="ExemptAmount", default=None
    )
    """
    The amount that is exempt
    """
    jurisdiction_region: typing.Optional[str] = pydantic.Field(
        alias="JurisdictionRegion", default=None
    )
    """
    Name identifying the region within the country
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    The name of the jurisdiction
    """
    non_taxable_amount: typing.Optional[float] = pydantic.Field(
        alias="NonTaxableAmount", default=None
    )
    """
    The amount that is not taxable
    """
    state_assigned_no: typing.Optional[str] = pydantic.Field(
        alias="StateAssignedNo", default=None
    )
    """
    The state assigned number of the jurisdiction
    """
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    """
    The amount of the tax
    """
    tax_component_id: typing.Optional[str] = pydantic.Field(
        alias="TaxComponentId", default=None
    )
    """
    The unique ID number of this component
    """
    tax_percentage: typing.Optional[float] = pydantic.Field(
        alias="TaxPercentage", default=None
    )
    """
    The percentage of the tax
    """
    taxable_amount: typing.Optional[float] = pydantic.Field(
        alias="TaxableAmount", default=None
    )
    """
    The amount that is taxable
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "SYSGST/USCITY",
            "SYSGST/USCOUNTRY",
            "SYSGST/USCOUNTY",
            "SYSGST/USSPECIAL",
            "SYSGST/USSTATE",
        ]
    ] = pydantic.Field(alias="Type", default=None)
    """
    The type of the jurisdiction
    """
