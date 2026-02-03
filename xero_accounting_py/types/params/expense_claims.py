import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .expense_claim import ExpenseClaim, _SerializerExpenseClaim


class ExpenseClaims(typing_extensions.TypedDict):
    """
    ExpenseClaims
    """

    expense_claims: typing_extensions.NotRequired[typing.List["ExpenseClaim"]]


class _SerializerExpenseClaims(pydantic.BaseModel):
    """
    Serializer for ExpenseClaims handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expense_claims: typing.Optional[typing.List["_SerializerExpenseClaim"]] = (
        pydantic.Field(alias="ExpenseClaims", default=None)
    )
