import pydantic
import typing
import typing_extensions


class SalesTrackingCategory(typing_extensions.TypedDict):
    """
    SalesTrackingCategory
    """

    tracking_category_name: typing_extensions.NotRequired[str]
    """
    The default sales tracking category name for contacts
    """

    tracking_option_name: typing_extensions.NotRequired[str]
    """
    The default purchase tracking category name for contacts
    """


class _SerializerSalesTrackingCategory(pydantic.BaseModel):
    """
    Serializer for SalesTrackingCategory handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tracking_category_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingCategoryName", default=None
    )
    tracking_option_name: typing.Optional[str] = pydantic.Field(
        alias="TrackingOptionName", default=None
    )
