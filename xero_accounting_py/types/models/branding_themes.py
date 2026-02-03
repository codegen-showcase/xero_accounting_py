import pydantic
import typing

from .branding_theme import BrandingTheme


class BrandingThemes(pydantic.BaseModel):
    """
    BrandingThemes
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branding_themes: typing.Optional[typing.List[BrandingTheme]] = pydantic.Field(
        alias="BrandingThemes", default=None
    )
