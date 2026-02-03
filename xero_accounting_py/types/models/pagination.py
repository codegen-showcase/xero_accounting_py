import pydantic
import typing


class Pagination(pydantic.BaseModel):
    """
    Pagination
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    item_count: typing.Optional[int] = pydantic.Field(alias="itemCount", default=None)
    page: typing.Optional[int] = pydantic.Field(alias="page", default=None)
    page_count: typing.Optional[int] = pydantic.Field(alias="pageCount", default=None)
    page_size: typing.Optional[int] = pydantic.Field(alias="pageSize", default=None)
