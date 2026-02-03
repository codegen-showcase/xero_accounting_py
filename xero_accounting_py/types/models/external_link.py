import pydantic
import typing
import typing_extensions


class ExternalLink(pydantic.BaseModel):
    """
    ExternalLink
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    link_type: typing.Optional[
        typing_extensions.Literal[
            "Facebook", "GooglePlus", "LinkedIn", "Twitter", "Website"
        ]
    ] = pydantic.Field(alias="LinkType", default=None)
    """
    See External link types
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    URL for service e.g. http://twitter.com/xeroapi
    """
