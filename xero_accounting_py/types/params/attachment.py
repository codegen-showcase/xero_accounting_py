import pydantic
import typing
import typing_extensions


class Attachment(typing_extensions.TypedDict):
    """
    Attachment
    """

    attachment_id: typing_extensions.NotRequired[str]
    """
    Unique ID for the file
    """

    content_length: typing_extensions.NotRequired[int]
    """
    Length of the file content
    """

    file_name: typing_extensions.NotRequired[str]
    """
    Name of the file
    """

    include_online: typing_extensions.NotRequired[bool]
    """
    Include the file with the online invoice
    """

    mime_type: typing_extensions.NotRequired[str]
    """
    Type of file
    """

    url: typing_extensions.NotRequired[str]
    """
    URL to the file on xero.com
    """


class _SerializerAttachment(pydantic.BaseModel):
    """
    Serializer for Attachment handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attachment_id: typing.Optional[str] = pydantic.Field(
        alias="AttachmentID", default=None
    )
    content_length: typing.Optional[int] = pydantic.Field(
        alias="ContentLength", default=None
    )
    file_name: typing.Optional[str] = pydantic.Field(alias="FileName", default=None)
    include_online: typing.Optional[bool] = pydantic.Field(
        alias="IncludeOnline", default=None
    )
    mime_type: typing.Optional[str] = pydantic.Field(alias="MimeType", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
