import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .expense_claim import ExpenseClaim


class ExpenseClaims(pydantic.BaseModel):
    """
    ExpenseClaims
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expense_claims: typing.Optional[typing.List["ExpenseClaim"]] = pydantic.Field(
        alias="ExpenseClaims", default=None
    )
