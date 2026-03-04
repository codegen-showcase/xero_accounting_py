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
    """
    Number of items returned
    """
    page: typing.Optional[int] = pydantic.Field(alias="page", default=None)
    """
    Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0.
    """
    page_count: typing.Optional[int] = pydantic.Field(alias="pageCount", default=None)
    """
    Number of pages available
    """
    page_size: typing.Optional[int] = pydantic.Field(alias="pageSize", default=None)
    """
    Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500.
    """
