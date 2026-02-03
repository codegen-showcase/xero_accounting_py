import pydantic
import typing
import typing_extensions


class Pagination(typing_extensions.TypedDict):
    """
    Pagination
    """

    item_count: typing_extensions.NotRequired[int]

    page: typing_extensions.NotRequired[int]

    page_count: typing_extensions.NotRequired[int]

    page_size: typing_extensions.NotRequired[int]


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
