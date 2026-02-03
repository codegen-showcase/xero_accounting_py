import pydantic
import typing
import typing_extensions


class BrandingTheme(pydantic.BaseModel):
    """
    BrandingTheme
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
    )
    """
    Xero identifier
    """
    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    """
    UTC timestamp of creation date of branding theme
    """
    logo_url: typing.Optional[str] = pydantic.Field(alias="LogoUrl", default=None)
    """
    The location of the image file used as the logo on this branding theme
    """
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    """
    Name of branding theme
    """
    sort_order: typing.Optional[int] = pydantic.Field(alias="SortOrder", default=None)
    """
    Integer – ranked order of branding theme. The default branding theme has a value of 0
    """
    type_: typing.Optional[typing_extensions.Literal["INVOICE"]] = pydantic.Field(
        alias="Type", default=None
    )
    """
    Always INVOICE
    """
