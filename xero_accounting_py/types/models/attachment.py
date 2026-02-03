import pydantic
import typing


class Attachment(pydantic.BaseModel):
    """
    Attachment
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attachment_id: typing.Optional[str] = pydantic.Field(
        alias="AttachmentID", default=None
    )
    """
    Unique ID for the file
    """
    content_length: typing.Optional[int] = pydantic.Field(
        alias="ContentLength", default=None
    )
    """
    Length of the file content
    """
    file_name: typing.Optional[str] = pydantic.Field(alias="FileName", default=None)
    """
    Name of the file
    """
    include_online: typing.Optional[bool] = pydantic.Field(
        alias="IncludeOnline", default=None
    )
    """
    Include the file with the online invoice
    """
    mime_type: typing.Optional[str] = pydantic.Field(alias="MimeType", default=None)
    """
    Type of file
    """
    url: typing.Optional[str] = pydantic.Field(alias="Url", default=None)
    """
    URL to the file on xero.com
    """
