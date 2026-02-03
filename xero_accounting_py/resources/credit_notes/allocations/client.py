import typing

from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from xero_accounting_py.types import models, params


class AllocationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        allocation_id: str,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Allocation:
        """
        Deletes an Allocation from a Credit Note

        DELETE /CreditNotes/{CreditNoteID}/Allocations/{AllocationID}

        Args:
            allocation_id: Unique identifier for Allocation object
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Allocation with the isDeleted flag as true

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.allocations.delete(
            allocation_id="00000000-0000-0000-0000-000000000000",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Allocation.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="DELETE",
            path=f"/CreditNotes/{credit_note_id}/Allocations/{allocation_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Allocation,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        allocations: typing.Union[
            typing.Optional[typing.List[params.Allocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Allocations:
        """
        Creates allocation for a specific credit note

        PUT /CreditNotes/{CreditNoteID}/Allocations

        Args:
            allocations: typing.List[Allocation]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Allocations array with newly created Allocation for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.credit_notes.allocations.create(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            allocations=[
                {
                    "amount": 1.0,
                    "date": "2019-03-05",
                    "invoice": {
                        "invoice_id": "c45720a1-ade3-4a38-a064-d15489be6841",
                        "line_items": [
                            {
                                "account_id": "00000000-0000-0000-0000-000000000000",
                                "line_item_id": "00000000-0000-0000-0000-000000000000",
                                "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                            }
                        ],
                    },
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerAllocations.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Allocations.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"allocations": allocations}, dump_with=params._SerializerAllocations
        )
        return self._base_client.request(
            method="PUT",
            path=f"/CreditNotes/{credit_note_id}/Allocations",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Allocations,
            request_options=request_options or default_request_options(),
        )


class AsyncAllocationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        allocation_id: str,
        credit_note_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Allocation:
        """
        Deletes an Allocation from a Credit Note

        DELETE /CreditNotes/{CreditNoteID}/Allocations/{AllocationID}

        Args:
            allocation_id: Unique identifier for Allocation object
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Allocation with the isDeleted flag as true

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.allocations.delete(
            allocation_id="00000000-0000-0000-0000-000000000000",
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        models.Allocation.model_rebuild(_types_namespace=models._types_namespace)
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="DELETE",
            path=f"/CreditNotes/{credit_note_id}/Allocations/{allocation_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.Allocation,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        credit_note_id: str,
        xero_tenant_id: str,
        allocations: typing.Union[
            typing.Optional[typing.List[params.Allocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summarize_errors: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Allocations:
        """
        Creates allocation for a specific credit note

        PUT /CreditNotes/{CreditNoteID}/Allocations

        Args:
            allocations: typing.List[Allocation]
            summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
            credit_note_id: Unique identifier for a Credit Note
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type Allocations array with newly created Allocation for specific Credit Note

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.credit_notes.allocations.create(
            credit_note_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            allocations=[
                {
                    "amount": 1.0,
                    "date": "2019-03-05",
                    "invoice": {
                        "invoice_id": "c45720a1-ade3-4a38-a064-d15489be6841",
                        "line_items": [
                            {
                                "account_id": "00000000-0000-0000-0000-000000000000",
                                "line_item_id": "00000000-0000-0000-0000-000000000000",
                                "repeating_invoice_id": "00000000-0000-0000-0000-000000000000",
                            }
                        ],
                    },
                }
            ],
            summarize_errors=True,
        )
        ```
        """
        params._SerializerAllocations.model_rebuild(
            _types_namespace=params._types_namespace
        )
        models.Allocations.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(summarize_errors, type_utils.NotGiven):
            encode_query_param(
                _query,
                "summarizeErrors",
                to_encodable(item=summarize_errors, dump_with=bool),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"allocations": allocations}, dump_with=params._SerializerAllocations
        )
        return await self._base_client.request(
            method="PUT",
            path=f"/CreditNotes/{credit_note_id}/Allocations",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            json=_json,
            cast_to=models.Allocations,
            request_options=request_options or default_request_options(),
        )
