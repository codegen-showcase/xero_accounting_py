import pydantic
import typing
import typing_extensions


class BrandingTheme(typing_extensions.TypedDict):
    """
    BrandingTheme
    """

    branding_theme_id: typing_extensions.NotRequired[str]
    """
    Xero identifier
    """

    created_date_utc: typing_extensions.NotRequired[str]
    """
    UTC timestamp of creation date of branding theme
    """

    logo_url: typing_extensions.NotRequired[str]
    """
    The location of the image file used as the logo on this branding theme
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of branding theme
    """

    sort_order: typing_extensions.NotRequired[int]
    """
    Integer – ranked order of branding theme. The default branding theme has a value of 0
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["INVOICE"]]
    """
    Always INVOICE
    """


class _SerializerBrandingTheme(pydantic.BaseModel):
    """
    Serializer for BrandingTheme handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    branding_theme_id: typing.Optional[str] = pydantic.Field(
        alias="BrandingThemeID", default=None
    )
    created_date_utc: typing.Optional[str] = pydantic.Field(
        alias="CreatedDateUTC", default=None
    )
    logo_url: typing.Optional[str] = pydantic.Field(alias="LogoUrl", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="Name", default=None)
    sort_order: typing.Optional[int] = pydantic.Field(alias="SortOrder", default=None)
    type_: typing.Optional[typing_extensions.Literal["INVOICE"]] = pydantic.Field(
        alias="Type", default=None
    )
