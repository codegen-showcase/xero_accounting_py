import pydantic
import typing
import typing_extensions


class TaxBreakdownComponent(typing_extensions.TypedDict):
    """
    TaxBreakdownComponent
    """

    exempt_amount: typing_extensions.NotRequired[float]
    """
    The amount that is exempt
    """

    jurisdiction_region: typing_extensions.NotRequired[str]
    """
    Name identifying the region within the country
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the jurisdiction
    """

    non_taxable_amount: typing_extensions.NotRequired[float]
    """
    The amount that is not taxable
    """

    state_assigned_no: typing_extensions.NotRequired[str]
    """
    The state assigned number of the jurisdiction
    """

    tax_amount: typing_extensions.NotRequired[float]
    """
    The amount of the tax
    """

    tax_component_id: typing_extensions.NotRequired[str]
    """
    The unique ID number of this component
    """

    tax_percentage: typing_extensions.NotRequired[float]
    """
    The percentage of the tax
    """

    taxable_amount: typing_extensions.NotRequired[float]
    """
    The amount that is taxable
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "SYSGST/USCITY",
            "SYSGST/USCOUNTRY",
            "SYSGST/USCOUNTY",
            "SYSGST/USSPECIAL",
            "SYSGST/USSTATE",
        ]
    ]
    """
    The type of the jurisdiction
    """


class _SerializerTaxBreakdownComponent(pydantic.BaseModel):
    """
    Serializer for TaxBreakdownComponent handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    exempt_amount: typing.Optional[float] = pydantic.Field(
        alias="ExemptAmount", default=None
    )
    jurisdiction_region: typing.Optional[str] = pydantic.Field(
        alias="JurisdictionRegion", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    non_taxable_amount: typing.Optional[float] = pydantic.Field(
        alias="NonTaxableAmount", default=None
    )
    state_assigned_no: typing.Optional[str] = pydantic.Field(
        alias="StateAssignedNo", default=None
    )
    tax_amount: typing.Optional[float] = pydantic.Field(alias="TaxAmount", default=None)
    tax_component_id: typing.Optional[str] = pydantic.Field(
        alias="TaxComponentId", default=None
    )
    tax_percentage: typing.Optional[float] = pydantic.Field(
        alias="TaxPercentage", default=None
    )
    taxable_amount: typing.Optional[float] = pydantic.Field(
        alias="TaxableAmount", default=None
    )
    type_: typing.Optional[
        typing_extensions.Literal[
            "SYSGST/USCITY",
            "SYSGST/USCOUNTRY",
            "SYSGST/USCOUNTY",
            "SYSGST/USSPECIAL",
            "SYSGST/USSTATE",
        ]
    ] = pydantic.Field(alias="Type", default=None)
