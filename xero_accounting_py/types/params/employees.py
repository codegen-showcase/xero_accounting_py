import pydantic
import typing
import typing_extensions

from .employee import Employee, _SerializerEmployee


class Employees(typing_extensions.TypedDict):
    """
    Employees
    """

    employees: typing_extensions.NotRequired[typing.List[Employee]]


class _SerializerEmployees(pydantic.BaseModel):
    """
    Serializer for Employees handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    employees: typing.Optional[typing.List[_SerializerEmployee]] = pydantic.Field(
        alias="Employees", default=None
    )
