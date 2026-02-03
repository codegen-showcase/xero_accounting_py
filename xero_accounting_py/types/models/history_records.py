import pydantic
import typing

from .history_record import HistoryRecord


class HistoryRecords(pydantic.BaseModel):
    """
    HistoryRecords
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    history_records: typing.Optional[typing.List[HistoryRecord]] = pydantic.Field(
        alias="HistoryRecords", default=None
    )
