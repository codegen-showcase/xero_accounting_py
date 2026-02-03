import typing
import typing_extensions

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


class LinkedTransactionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific linked transactions (billable expenses)

        DELETE /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.linked_transactions.delete(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        self._base_client.request(
            method="DELETE",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        linked_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        target_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Retrieves linked transactions (billable expenses)

        GET /LinkedTransactions

        Args:
            contact_id: Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.
            linked_transaction_id: The Xero identifier for an Linked Transaction
            page: Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1.
            source_transaction_id: Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice
            status: Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status
            target_transaction_id: Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with all LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.linked_transactions.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_id="00000000-0000-0000-0000-000000000000",
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            page=1,
            source_transaction_id="00000000-0000-0000-0000-000000000000",
            status="APPROVED",
            target_transaction_id="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactID",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(linked_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "LinkedTransactionID",
                to_encodable(item=linked_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(source_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "SourceTransactionID",
                to_encodable(item=source_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(target_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "TargetTransactionID",
                to_encodable(item=target_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path="/LinkedTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id

        GET /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with a specified LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.linked_transactions.get(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return self._base_client.request(
            method="GET",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        linked_transactions: typing.Union[
            typing.Optional[typing.List[params.LinkedTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Updates a specific linked transactions (billable expenses)

        POST /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transactions: typing.List[LinkedTransaction]
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with updated LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.linked_transactions.update(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            linked_transactions=[
                {
                    "source_line_item_id": "00000000-0000-0000-0000-000000000000",
                    "source_transaction_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"linked_transactions": linked_transactions},
            dump_with=params._SerializerLinkedTransactions,
        )
        return self._base_client.request(
            method="POST",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        linked_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_line_item_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_type_code: typing.Union[
            typing.Optional[typing_extensions.Literal["ACCPAY", "SPEND"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "APPROVED", "BILLED", "DRAFT", "ONDRAFT", "VOIDED"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        target_line_item_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        target_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["BILLABLEEXPENSE"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Creates linked transactions (billable expenses)

        PUT /LinkedTransactions

        Args:
            contact_id: Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
            linked_transaction_id: The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9
            source_line_item_id: The line item identifier from the source transaction.
            source_transaction_id: Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice
            source_transaction_type_code: The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction.
            status: Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
            target_line_item_id: The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID.
            target_transaction_id: Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice
            type_: This will always be BILLABLEEXPENSE. More types may be added in future.
            updated_date_utc: The last modified date in UTC format
            validation_errors: Displays array of validation error messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with newly created LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.linked_transactions.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "linked_transaction_id": linked_transaction_id,
                "source_line_item_id": source_line_item_id,
                "source_transaction_id": source_transaction_id,
                "source_transaction_type_code": source_transaction_type_code,
                "status": status,
                "target_line_item_id": target_line_item_id,
                "target_transaction_id": target_transaction_id,
                "type_": type_,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
            },
            dump_with=params._SerializerLinkedTransaction,
        )
        return self._base_client.request(
            method="PUT",
            path="/LinkedTransactions",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )


class AsyncLinkedTransactionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific linked transactions (billable expenses)

        DELETE /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response 204 no content

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.linked_transactions.delete(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        await self._base_client.request(
            method="DELETE",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        linked_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        target_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Retrieves linked transactions (billable expenses)

        GET /LinkedTransactions

        Args:
            contact_id: Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.
            linked_transaction_id: The Xero identifier for an Linked Transaction
            page: Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1.
            source_transaction_id: Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice
            status: Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status
            target_transaction_id: Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with all LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.linked_transactions.list(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            contact_id="00000000-0000-0000-0000-000000000000",
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            page=1,
            source_transaction_id="00000000-0000-0000-0000-000000000000",
            status="APPROVED",
            target_transaction_id="00000000-0000-0000-0000-000000000000",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(contact_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ContactID",
                to_encodable(item=contact_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(linked_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "LinkedTransactionID",
                to_encodable(item=linked_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(source_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "SourceTransactionID",
                to_encodable(item=source_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "Status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(target_transaction_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "TargetTransactionID",
                to_encodable(item=target_transaction_id, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path="/LinkedTransactions",
            auth_names=["OAuth2"],
            query_params=_query,
            headers=_header,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id

        GET /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with a specified LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.linked_transactions.get(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        return await self._base_client.request(
            method="GET",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        linked_transaction_id: str,
        xero_tenant_id: str,
        linked_transactions: typing.Union[
            typing.Optional[typing.List[params.LinkedTransaction]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Updates a specific linked transactions (billable expenses)

        POST /LinkedTransactions/{LinkedTransactionID}

        Args:
            linked_transactions: typing.List[LinkedTransaction]
            linked_transaction_id: Unique identifier for a LinkedTransaction
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with updated LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.linked_transactions.update(
            linked_transaction_id="00000000-0000-0000-0000-000000000000",
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            linked_transactions=[
                {
                    "source_line_item_id": "00000000-0000-0000-0000-000000000000",
                    "source_transaction_id": "00000000-0000-0000-0000-000000000000",
                }
            ],
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={"linked_transactions": linked_transactions},
            dump_with=params._SerializerLinkedTransactions,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/LinkedTransactions/{linked_transaction_id}",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        xero_tenant_id: str,
        contact_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        linked_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_line_item_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        source_transaction_type_code: typing.Union[
            typing.Optional[typing_extensions.Literal["ACCPAY", "SPEND"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "APPROVED", "BILLED", "DRAFT", "ONDRAFT", "VOIDED"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        target_line_item_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        target_transaction_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["BILLABLEEXPENSE"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        updated_date_utc: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        validation_errors: typing.Union[
            typing.Optional[typing.List[params.ValidationError]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.LinkedTransactions:
        """
        Creates linked transactions (billable expenses)

        PUT /LinkedTransactions

        Args:
            contact_id: Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
            linked_transaction_id: The Xero identifier for an Linked Transaction e.g./LinkedTransactions/297c2dc5-cc47-4afd-8ec8-74990b8761e9
            source_line_item_id: The line item identifier from the source transaction.
            source_transaction_id: Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice
            source_transaction_type_code: The Type of the source tranasction. This will be ACCPAY if the linked transaction was created from an invoice and SPEND if it was created from a bank transaction.
            status: Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED.
            target_line_item_id: The line item identifier from the target transaction. It is possible  to link multiple billable expenses to the same TargetLineItemID.
            target_transaction_id: Filter by the TargetTransactionID. Get all the linked transactions  allocated to a particular ACCREC invoice
            type_: This will always be BILLABLEEXPENSE. More types may be added in future.
            updated_date_utc: The last modified date in UTC format
            validation_errors: Displays array of validation error messages from the API
            xero_tenant_id: Xero identifier for Tenant
            request_options: Additional options to customize the HTTP request

        Returns:
            Success - return response of type LinkedTransactions array with newly created LinkedTransaction

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.linked_transactions.create(
            xero_tenant_id="YOUR_XERO_TENANT_ID",
            updated_date_utc="/Date(1573755038314)/",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["xero-tenant-id"] = str(xero_tenant_id)
        _json = to_encodable(
            item={
                "contact_id": contact_id,
                "linked_transaction_id": linked_transaction_id,
                "source_line_item_id": source_line_item_id,
                "source_transaction_id": source_transaction_id,
                "source_transaction_type_code": source_transaction_type_code,
                "status": status,
                "target_line_item_id": target_line_item_id,
                "target_transaction_id": target_transaction_id,
                "type_": type_,
                "updated_date_utc": updated_date_utc,
                "validation_errors": validation_errors,
            },
            dump_with=params._SerializerLinkedTransaction,
        )
        return await self._base_client.request(
            method="PUT",
            path="/LinkedTransactions",
            auth_names=["OAuth2"],
            headers=_header,
            json=_json,
            cast_to=models.LinkedTransactions,
            request_options=request_options or default_request_options(),
        )
