import pydantic
import typing


class CisOrgSetting(pydantic.BaseModel):
    """
    CisOrgSetting
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cis_contractor_enabled: typing.Optional[bool] = pydantic.Field(
        alias="CISContractorEnabled", default=None
    )
    """
    true or false - Boolean that describes if the organisation is a CIS Contractor
    """
    cis_sub_contractor_enabled: typing.Optional[bool] = pydantic.Field(
        alias="CISSubContractorEnabled", default=None
    )
    """
    true or false - Boolean that describes if the organisation is a CIS SubContractor
    """
    rate: typing.Optional[float] = pydantic.Field(alias="Rate", default=None)
    """
    CIS Deduction rate for the organisation
    """
