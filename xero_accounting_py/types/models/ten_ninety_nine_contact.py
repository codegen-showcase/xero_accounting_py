import pydantic
import typing
import typing_extensions


class TenNinetyNineContact(pydantic.BaseModel):
    """
    TenNinetyNineContact
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    box1: typing.Optional[float] = pydantic.Field(alias="Box1", default=None)
    """
    Box 1 on 1099 Form
    """
    box10: typing.Optional[float] = pydantic.Field(alias="Box10", default=None)
    """
    Box 10 on 1099 Form
    """
    box11: typing.Optional[float] = pydantic.Field(alias="Box11", default=None)
    """
    Box 11 on 1099 Form
    """
    box13: typing.Optional[float] = pydantic.Field(alias="Box13", default=None)
    """
    Box 13 on 1099 Form
    """
    box14: typing.Optional[float] = pydantic.Field(alias="Box14", default=None)
    """
    Box 14 on 1099 Form
    """
    box2: typing.Optional[float] = pydantic.Field(alias="Box2", default=None)
    """
    Box 2 on 1099 Form
    """
    box3: typing.Optional[float] = pydantic.Field(alias="Box3", default=None)
    """
    Box 3 on 1099 Form
    """
    box4: typing.Optional[float] = pydantic.Field(alias="Box4", default=None)
    """
    Box 4 on 1099 Form
    """
    box5: typing.Optional[float] = pydantic.Field(alias="Box5", default=None)
    """
    Box 5 on 1099 Form
    """
    box6: typing.Optional[float] = pydantic.Field(alias="Box6", default=None)
    """
    Box 6 on 1099 Form
    """
    box7: typing.Optional[float] = pydantic.Field(alias="Box7", default=None)
    """
    Box 7 on 1099 Form
    """
    box8: typing.Optional[float] = pydantic.Field(alias="Box8", default=None)
    """
    Box 8 on 1099 Form
    """
    box9: typing.Optional[float] = pydantic.Field(alias="Box9", default=None)
    """
    Box 9 on 1099 Form
    """
    business_name: typing.Optional[str] = pydantic.Field(
        alias="BusinessName", default=None
    )
    """
    Contact business name
    """
    city: typing.Optional[str] = pydantic.Field(alias="City", default=None)
    """
    Contact city on 1099 Form
    """
    contact_id: typing.Optional[str] = pydantic.Field(alias="ContactId", default=None)
    """
    Contact contact id
    """
    email: typing.Optional[str] = pydantic.Field(alias="Email", default=None)
    """
    Contact email on 1099 Form
    """
    federal_tax_classification: typing.Optional[
        typing_extensions.Literal[
            "C_CORP",
            "NONPROFIT",
            "OTHER",
            "PARTNERSHIP",
            "SOLE_PROPRIETOR",
            "S_CORP",
            "TRUST_OR_ESTATE",
        ]
    ] = pydantic.Field(alias="FederalTaxClassification", default=None)
    """
    Contact federal tax classification
    """
    federal_tax_id_type: typing.Optional[str] = pydantic.Field(
        alias="FederalTaxIDType", default=None
    )
    """
    Contact Fed Tax ID type
    """
    legal_name: typing.Optional[str] = pydantic.Field(alias="LegalName", default=None)
    """
    Contact legal name
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Contact name on 1099 Form
    """
    state: typing.Optional[str] = pydantic.Field(alias="State", default=None)
    """
    Contact State on 1099 Form
    """
    street_address: typing.Optional[str] = pydantic.Field(
        alias="StreetAddress", default=None
    )
    """
    Contact address on 1099 Form
    """
    tax_id: typing.Optional[str] = pydantic.Field(alias="TaxID", default=None)
    """
    Contact tax id on 1099 Form
    """
    zip: typing.Optional[str] = pydantic.Field(alias="Zip", default=None)
    """
    Contact zip on 1099 Form
    """
