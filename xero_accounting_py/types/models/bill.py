import pydantic
import typing
import typing_extensions


class Bill(pydantic.BaseModel):
    """
    Bill
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    day: typing.Optional[int] = pydantic.Field(alias="Day", default=None)
    """
    Day of Month (0-31)
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
        ]
    ] = pydantic.Field(alias="Type", default=None)
