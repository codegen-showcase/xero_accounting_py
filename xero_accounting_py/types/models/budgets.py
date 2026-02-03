import pydantic
import typing

from .budget import Budget


class Budgets(pydantic.BaseModel):
    """
    Budgets
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    budgets: typing.Optional[typing.List[Budget]] = pydantic.Field(
        alias="Budgets", default=None
    )
