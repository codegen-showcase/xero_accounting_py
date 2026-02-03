import pydantic
import typing

from .cis_org_setting import CisOrgSetting


class CisOrgSettings(pydantic.BaseModel):
    """
    CisOrgSettings
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cis_settings: typing.Optional[typing.List[CisOrgSetting]] = pydantic.Field(
        alias="CISSettings", default=None
    )
