import pydantic
import typing
import typing_extensions


class ExternalLink(typing_extensions.TypedDict):
    """
    ExternalLink
    """

    description: typing_extensions.NotRequired[str]

    link_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "Facebook", "GooglePlus", "LinkedIn", "Twitter", "Website"
        ]
    ]
    """
    See External link types
    """

    url: typing_extensions.NotRequired[str]
    """
    URL for service e.g. http://twitter.com/xeroapi
    """


class _SerializerExternalLink(pydantic.BaseModel):
    """
    Serializer for ExternalLink handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
