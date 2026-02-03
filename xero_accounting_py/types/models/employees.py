import pydantic
import typing

from .employee import Employee


class Employees(pydantic.BaseModel):
    """
    Employees
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    employees: typing.Optional[typing.List[Employee]] = pydantic.Field(
        alias="Employees", default=None
    )
