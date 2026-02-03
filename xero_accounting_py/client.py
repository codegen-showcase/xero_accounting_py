import httpx
import typing

from make_api_request import (
    AsyncBaseClient,
    AuthBearer,
    OAuth2,
    OAuth2ClientCredentials,
    SyncBaseClient,
)
from xero_accounting_py.environment import Environment, _get_base_url
from xero_accounting_py.resources.accounts import AccountsClient, AsyncAccountsClient
from xero_accounting_py.resources.bank_transactions import (
    AsyncBankTransactionsClient,
    BankTransactionsClient,
)
from xero_accounting_py.resources.bank_transfers import (
    AsyncBankTransfersClient,
    BankTransfersClient,
)
from xero_accounting_py.resources.batch_payments import (
    AsyncBatchPaymentsClient,
    BatchPaymentsClient,
)
from xero_accounting_py.resources.branding_themes import (
    AsyncBrandingThemesClient,
    BrandingThemesClient,
)
from xero_accounting_py.resources.budgets import AsyncBudgetsClient, BudgetsClient
from xero_accounting_py.resources.contact_groups import (
    AsyncContactGroupsClient,
    ContactGroupsClient,
)
from xero_accounting_py.resources.contacts import AsyncContactsClient, ContactsClient
from xero_accounting_py.resources.credit_notes import (
    AsyncCreditNotesClient,
    CreditNotesClient,
)
from xero_accounting_py.resources.currencies import (
    AsyncCurrenciesClient,
    CurrenciesClient,
)
from xero_accounting_py.resources.employees import AsyncEmployeesClient, EmployeesClient
from xero_accounting_py.resources.expense_claims import (
    AsyncExpenseClaimsClient,
    ExpenseClaimsClient,
)
from xero_accounting_py.resources.invoice_reminders import (
    AsyncInvoiceRemindersClient,
    InvoiceRemindersClient,
)
from xero_accounting_py.resources.invoices import AsyncInvoicesClient, InvoicesClient
from xero_accounting_py.resources.items import AsyncItemsClient, ItemsClient
from xero_accounting_py.resources.journals import AsyncJournalsClient, JournalsClient
from xero_accounting_py.resources.linked_transactions import (
    AsyncLinkedTransactionsClient,
    LinkedTransactionsClient,
)
from xero_accounting_py.resources.manual_journals import (
    AsyncManualJournalsClient,
    ManualJournalsClient,
)
from xero_accounting_py.resources.organisation import (
    AsyncOrganisationClient,
    OrganisationClient,
)
from xero_accounting_py.resources.overpayments import (
    AsyncOverpaymentsClient,
    OverpaymentsClient,
)
from xero_accounting_py.resources.payment_services import (
    AsyncPaymentServicesClient,
    PaymentServicesClient,
)
from xero_accounting_py.resources.payments import AsyncPaymentsClient, PaymentsClient
from xero_accounting_py.resources.prepayments import (
    AsyncPrepaymentsClient,
    PrepaymentsClient,
)
from xero_accounting_py.resources.purchase_orders import (
    AsyncPurchaseOrdersClient,
    PurchaseOrdersClient,
)
from xero_accounting_py.resources.quotes import AsyncQuotesClient, QuotesClient
from xero_accounting_py.resources.receipts import AsyncReceiptsClient, ReceiptsClient
from xero_accounting_py.resources.repeating_invoices import (
    AsyncRepeatingInvoicesClient,
    RepeatingInvoicesClient,
)
from xero_accounting_py.resources.reports import AsyncReportsClient, ReportsClient
from xero_accounting_py.resources.setup import AsyncSetupClient, SetupClient
from xero_accounting_py.resources.tax_rates import AsyncTaxRatesClient, TaxRatesClient
from xero_accounting_py.resources.tracking_categories import (
    AsyncTrackingCategoriesClient,
    TrackingCategoriesClient,
)
from xero_accounting_py.resources.users import AsyncUsersClient, UsersClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        oauth: typing.Optional[OAuth2ClientCredentials] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={
                "OAuth2": OAuth2(
                    base_url=_get_base_url(base_url=base_url, environment=environment),
                    default_token_url="https://identity.xero.com/connect/token",
                    access_token_pointer="/access_token",
                    expires_in_pointer="/expires_in",
                    credentials_location="request_body",
                    body_content="form",
                    request_mutator=AuthBearer(token=None),
                    form=oauth,
                )
            },
        )
        self.accounts = AccountsClient(base_client=self._base_client)
        self.contact_groups = ContactGroupsClient(base_client=self._base_client)
        self.credit_notes = CreditNotesClient(base_client=self._base_client)
        self.items = ItemsClient(base_client=self._base_client)
        self.linked_transactions = LinkedTransactionsClient(
            base_client=self._base_client
        )
        self.overpayments = OverpaymentsClient(base_client=self._base_client)
        self.prepayments = PrepaymentsClient(base_client=self._base_client)
        self.tracking_categories = TrackingCategoriesClient(
            base_client=self._base_client
        )
        self.bank_transactions = BankTransactionsClient(base_client=self._base_client)
        self.bank_transfers = BankTransfersClient(base_client=self._base_client)
        self.batch_payments = BatchPaymentsClient(base_client=self._base_client)
        self.branding_themes = BrandingThemesClient(base_client=self._base_client)
        self.budgets = BudgetsClient(base_client=self._base_client)
        self.contacts = ContactsClient(base_client=self._base_client)
        self.currencies = CurrenciesClient(base_client=self._base_client)
        self.employees = EmployeesClient(base_client=self._base_client)
        self.expense_claims = ExpenseClaimsClient(base_client=self._base_client)
        self.invoice_reminders = InvoiceRemindersClient(base_client=self._base_client)
        self.invoices = InvoicesClient(base_client=self._base_client)
        self.journals = JournalsClient(base_client=self._base_client)
        self.manual_journals = ManualJournalsClient(base_client=self._base_client)
        self.organisation = OrganisationClient(base_client=self._base_client)
        self.payment_services = PaymentServicesClient(base_client=self._base_client)
        self.payments = PaymentsClient(base_client=self._base_client)
        self.purchase_orders = PurchaseOrdersClient(base_client=self._base_client)
        self.quotes = QuotesClient(base_client=self._base_client)
        self.receipts = ReceiptsClient(base_client=self._base_client)
        self.repeating_invoices = RepeatingInvoicesClient(base_client=self._base_client)
        self.reports = ReportsClient(base_client=self._base_client)
        self.tax_rates = TaxRatesClient(base_client=self._base_client)
        self.users = UsersClient(base_client=self._base_client)
        self.setup = SetupClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        oauth: typing.Optional[OAuth2ClientCredentials] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={
                "OAuth2": OAuth2(
                    base_url=_get_base_url(base_url=base_url, environment=environment),
                    default_token_url="https://identity.xero.com/connect/token",
                    access_token_pointer="/access_token",
                    expires_in_pointer="/expires_in",
                    credentials_location="request_body",
                    body_content="form",
                    request_mutator=AuthBearer(token=None),
                    form=oauth,
                )
            },
        )
        self.accounts = AsyncAccountsClient(base_client=self._base_client)
        self.contact_groups = AsyncContactGroupsClient(base_client=self._base_client)
        self.credit_notes = AsyncCreditNotesClient(base_client=self._base_client)
        self.items = AsyncItemsClient(base_client=self._base_client)
        self.linked_transactions = AsyncLinkedTransactionsClient(
            base_client=self._base_client
        )
        self.overpayments = AsyncOverpaymentsClient(base_client=self._base_client)
        self.prepayments = AsyncPrepaymentsClient(base_client=self._base_client)
        self.tracking_categories = AsyncTrackingCategoriesClient(
            base_client=self._base_client
        )
        self.bank_transactions = AsyncBankTransactionsClient(
            base_client=self._base_client
        )
        self.bank_transfers = AsyncBankTransfersClient(base_client=self._base_client)
        self.batch_payments = AsyncBatchPaymentsClient(base_client=self._base_client)
        self.branding_themes = AsyncBrandingThemesClient(base_client=self._base_client)
        self.budgets = AsyncBudgetsClient(base_client=self._base_client)
        self.contacts = AsyncContactsClient(base_client=self._base_client)
        self.currencies = AsyncCurrenciesClient(base_client=self._base_client)
        self.employees = AsyncEmployeesClient(base_client=self._base_client)
        self.expense_claims = AsyncExpenseClaimsClient(base_client=self._base_client)
        self.invoice_reminders = AsyncInvoiceRemindersClient(
            base_client=self._base_client
        )
        self.invoices = AsyncInvoicesClient(base_client=self._base_client)
        self.journals = AsyncJournalsClient(base_client=self._base_client)
        self.manual_journals = AsyncManualJournalsClient(base_client=self._base_client)
        self.organisation = AsyncOrganisationClient(base_client=self._base_client)
        self.payment_services = AsyncPaymentServicesClient(
            base_client=self._base_client
        )
        self.payments = AsyncPaymentsClient(base_client=self._base_client)
        self.purchase_orders = AsyncPurchaseOrdersClient(base_client=self._base_client)
        self.quotes = AsyncQuotesClient(base_client=self._base_client)
        self.receipts = AsyncReceiptsClient(base_client=self._base_client)
        self.repeating_invoices = AsyncRepeatingInvoicesClient(
            base_client=self._base_client
        )
        self.reports = AsyncReportsClient(base_client=self._base_client)
        self.tax_rates = AsyncTaxRatesClient(base_client=self._base_client)
        self.users = AsyncUsersClient(base_client=self._base_client)
        self.setup = AsyncSetupClient(base_client=self._base_client)
