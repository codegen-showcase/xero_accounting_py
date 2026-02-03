from make_api_request import AsyncBaseClient, SyncBaseClient
from xero_accounting_py.resources.invoice_reminders.settings import (
    AsyncSettingsClient,
    SettingsClient,
)


class InvoiceRemindersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.settings = SettingsClient(base_client=self._base_client)


class AsyncInvoiceRemindersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.settings = AsyncSettingsClient(base_client=self._base_client)
