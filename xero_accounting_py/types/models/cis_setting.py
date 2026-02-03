import pydantic
import typing


class CisSetting(pydantic.BaseModel):
    """
    CisSetting
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cis_enabled: typing.Optional[bool] = pydantic.Field(
        alias="CISEnabled", default=None
    )
    """
    Boolean that describes if the contact is a CIS Subcontractor
    """
    rate: typing.Optional[float] = pydantic.Field(alias="Rate", default=None)
    """
    CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned
    """
