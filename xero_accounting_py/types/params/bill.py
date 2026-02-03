import pydantic
import typing
import typing_extensions


class Bill(typing_extensions.TypedDict):
    """
    Bill
    """

    day: typing_extensions.NotRequired[int]
    """
    Day of Month (0-31)
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
        ]
    ]


class _SerializerBill(pydantic.BaseModel):
    """
    Serializer for Bill handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: typing.Optional[int] = pydantic.Field(alias="Day", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
        ]
    ] = pydantic.Field(alias="Type", default=None)
