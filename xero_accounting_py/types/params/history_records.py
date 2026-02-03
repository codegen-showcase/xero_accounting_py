import pydantic
import typing
import typing_extensions

from .history_record import HistoryRecord, _SerializerHistoryRecord


class HistoryRecords(typing_extensions.TypedDict):
    """
    HistoryRecords
    """

    history_records: typing_extensions.NotRequired[typing.List[HistoryRecord]]


class _SerializerHistoryRecords(pydantic.BaseModel):
    """
    Serializer for HistoryRecords handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    history_records: typing.Optional[typing.List[_SerializerHistoryRecord]] = (
        pydantic.Field(alias="HistoryRecords", default=None)
    )
