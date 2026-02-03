import pydantic
import typing

from .cis_setting import CisSetting


class CisSettings(pydantic.BaseModel):
    """
    CisSettings
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cis_settings: typing.Optional[typing.List[CisSetting]] = pydantic.Field(
        alias="CISSettings", default=None
    )
