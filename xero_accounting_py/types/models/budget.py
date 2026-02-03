import pydantic
import typing
import typing_extensions

from .budget_line import BudgetLine
from .tracking_category import TrackingCategory


class Budget(pydantic.BaseModel):
    """
    Budget
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    budget_id: typing.Optional[str] = pydantic.Field(alias="BudgetID", default=None)
    """
    Xero identifier
    """
    budget_lines: typing.Optional[typing.List[BudgetLine]] = pydantic.Field(
        alias="BudgetLines", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="Description", default=None
    )
    """
    The Budget description
    """
    tracking: typing.Optional[typing.List[TrackingCategory]] = pydantic.Field(
        alias="Tracking", default=None
    )
    type_: typing.Optional[typing_extensions.Literal["OVERALL", "TRACKING"]] = (
        pydantic.Field(alias="Type", default=None)
    )
    """
    Type of Budget. OVERALL or TRACKING
    """
    updated_date_utc: typing.Optional[str] = pydantic.Field(
        alias="UpdatedDateUTC", default=None
    )
    """
    UTC timestamp of last update to budget
    """
