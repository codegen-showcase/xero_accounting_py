import pydantic
import typing
import typing_extensions


class Pagination(typing_extensions.TypedDict):
    """
    Pagination
    """

    item_count: typing_extensions.NotRequired[int]
    """
    Number of items returned
    """

    page: typing_extensions.NotRequired[int]
    """
    Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
    """

    page_count: typing_extensions.NotRequired[int]
    """
    Number of pages available
    """

    page_size: typing_extensions.NotRequired[int]
    """
    Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
    """


class _SerializerPagination(pydantic.BaseModel):
    """
    Serializer for Pagination handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    item_count: typing.Optional[int] = pydantic.Field(alias="itemCount", default=None)
    page: typing.Optional[int] = pydantic.Field(alias="page", default=None)
    page_count: typing.Optional[int] = pydantic.Field(alias="pageCount", default=None)
    page_size: typing.Optional[int] = pydantic.Field(alias="pageSize", default=None)
