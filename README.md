# Xero: Accounting + Projects APIs - Python

This README can be edited between codegens. The "Module Documentation and Snippets" section stays up to date automatically even when you edit this file.

## Getting Started

#### Synchronous Client

```python
from os import getenv
from xero_accounting_py import Client

client = Client(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
```

#### Asynchronous Client

```python
from os import getenv
from xero_accounting_py import AsyncClient

client = AsyncClient(
    oauth={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
```

## Local Development

1. Install

```bash
poetry install
```

2. Run Tests

```bash
poetry run pytests
```

## Module Documentation and Snippets

### [accounting.accounts](xero_accounting_py/resources/accounting/accounts/README.md)

- [create](xero_accounting_py/resources/accounting/accounts/README.md#create) - Creates a new chart of accounts
- [delete](xero_accounting_py/resources/accounting/accounts/README.md#delete) - Deletes a chart of accounts
- [get](xero_accounting_py/resources/accounting/accounts/README.md#get) - Retrieves a single chart of accounts by using a unique account Id
- [list](xero_accounting_py/resources/accounting/accounts/README.md#list) - Retrieves the full chart of accounts
- [update](xero_accounting_py/resources/accounting/accounts/README.md#update) - Updates a chart of accounts

### [accounting.accounts.attachments](xero_accounting_py/resources/accounting/accounts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/accounts/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific account using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/accounts/attachments/README.md#list) - Retrieves attachments for a specific accounts by using a unique account Id

### [accounting.bank_transactions](xero_accounting_py/resources/accounting/bank_transactions/README.md)

- [create](xero_accounting_py/resources/accounting/bank_transactions/README.md#create) - Creates one or more spent or received money transaction
- [get](xero_accounting_py/resources/accounting/bank_transactions/README.md#get) - Retrieves a single spent or received money transaction by using a unique bank transaction Id
- [list](xero_accounting_py/resources/accounting/bank_transactions/README.md#list) - Retrieves any spent or received money transactions
- [update](xero_accounting_py/resources/accounting/bank_transactions/README.md#update) - Updates a single spent or received money transaction
- [update_or_create](xero_accounting_py/resources/accounting/bank_transactions/README.md#update_or_create) - Updates or creates one or more spent or received money transaction

### [accounting.bank_transactions.attachments](xero_accounting_py/resources/accounting/bank_transactions/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/bank_transactions/attachments/README.md#get_by_id) - Retrieves specific attachments from a specific BankTransaction using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/bank_transactions/attachments/README.md#list) - Retrieves any attachments from a specific bank transactions

### [accounting.bank_transactions.history](xero_accounting_py/resources/accounting/bank_transactions/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/bank_transactions/history/README.md#create_record) - Creates a history record for a specific bank transactions
- [list](xero_accounting_py/resources/accounting/bank_transactions/history/README.md#list) - Retrieves history from a specific bank transaction using a unique bank transaction Id

### [accounting.bank_transfers](xero_accounting_py/resources/accounting/bank_transfers/README.md)

- [create](xero_accounting_py/resources/accounting/bank_transfers/README.md#create) - Creates a bank transfer
- [get](xero_accounting_py/resources/accounting/bank_transfers/README.md#get) - Retrieves specific bank transfers by using a unique bank transfer Id
- [list](xero_accounting_py/resources/accounting/bank_transfers/README.md#list) - Retrieves all bank transfers

### [accounting.bank_transfers.attachments](xero_accounting_py/resources/accounting/bank_transfers/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/bank_transfers/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific bank transfer using a unique attachment ID
- [list](xero_accounting_py/resources/accounting/bank_transfers/attachments/README.md#list) - Retrieves attachments from a specific bank transfer

### [accounting.bank_transfers.history](xero_accounting_py/resources/accounting/bank_transfers/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/bank_transfers/history/README.md#create_record) - Creates a history record for a specific bank transfer
- [list](xero_accounting_py/resources/accounting/bank_transfers/history/README.md#list) - Retrieves history from a specific bank transfer using a unique bank transfer Id

### [accounting.batch_payments](xero_accounting_py/resources/accounting/batch_payments/README.md)

- [create](xero_accounting_py/resources/accounting/batch_payments/README.md#create) - Creates one or many batch payments for invoices
- [delete](xero_accounting_py/resources/accounting/batch_payments/README.md#delete) - Updates a specific batch payment for invoices and credit notes
- [get](xero_accounting_py/resources/accounting/batch_payments/README.md#get) - Retrieves a specific batch payment using a unique batch payment Id
- [list](xero_accounting_py/resources/accounting/batch_payments/README.md#list) - Retrieves either one or many batch payments for invoices
- [update](xero_accounting_py/resources/accounting/batch_payments/README.md#update) - Updates a specific batch payment for invoices and credit notes

### [accounting.batch_payments.history](xero_accounting_py/resources/accounting/batch_payments/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/batch_payments/history/README.md#create_record) - Creates a history record for a specific batch payment
- [list](xero_accounting_py/resources/accounting/batch_payments/history/README.md#list) - Retrieves history from a specific batch payment

### [accounting.branding_themes](xero_accounting_py/resources/accounting/branding_themes/README.md)

- [get](xero_accounting_py/resources/accounting/branding_themes/README.md#get) - Retrieves a specific branding theme using a unique branding theme Id
- [list](xero_accounting_py/resources/accounting/branding_themes/README.md#list) - Retrieves all the branding themes

### [accounting.branding_themes.payment_services](xero_accounting_py/resources/accounting/branding_themes/payment_services/README.md)

- [create](xero_accounting_py/resources/accounting/branding_themes/payment_services/README.md#create) - Creates a new custom payment service for a specific branding theme
- [list](xero_accounting_py/resources/accounting/branding_themes/payment_services/README.md#list) - Retrieves the payment services for a specific branding theme

### [accounting.budgets](xero_accounting_py/resources/accounting/budgets/README.md)

- [get](xero_accounting_py/resources/accounting/budgets/README.md#get) - Retrieves a specific budget, which includes budget lines
- [list](xero_accounting_py/resources/accounting/budgets/README.md#list) - Retrieve a list of budgets

### [accounting.contact_groups](xero_accounting_py/resources/accounting/contact_groups/README.md)

- [create](xero_accounting_py/resources/accounting/contact_groups/README.md#create) - Creates a contact group
- [get](xero_accounting_py/resources/accounting/contact_groups/README.md#get) - Retrieves a specific contact group by using a unique contact group Id
- [list](xero_accounting_py/resources/accounting/contact_groups/README.md#list) - Retrieves the contact Id and name of each contact group
- [update](xero_accounting_py/resources/accounting/contact_groups/README.md#update) - Updates a specific contact group

### [accounting.contact_groups.contacts](xero_accounting_py/resources/accounting/contact_groups/contacts/README.md)

- [create](xero_accounting_py/resources/accounting/contact_groups/contacts/README.md#create) - Creates contacts to a specific contact group
- [delete](xero_accounting_py/resources/accounting/contact_groups/contacts/README.md#delete) - Deletes a specific contact from a contact group using a unique contact Id
- [delete_all](xero_accounting_py/resources/accounting/contact_groups/contacts/README.md#delete_all) - Deletes all contacts from a specific contact group

### [accounting.contacts](xero_accounting_py/resources/accounting/contacts/README.md)

- [create](xero_accounting_py/resources/accounting/contacts/README.md#create) - Creates multiple contacts (bulk) in a Xero organisation
- [get](xero_accounting_py/resources/accounting/contacts/README.md#get) - Retrieves a specific contacts in a Xero organisation using a unique contact Id
- [list](xero_accounting_py/resources/accounting/contacts/README.md#list) - Retrieves all contacts in a Xero organisation
- [update](xero_accounting_py/resources/accounting/contacts/README.md#update) - Updates a specific contact in a Xero organisation
- [update_or_create](xero_accounting_py/resources/accounting/contacts/README.md#update_or_create) - Updates or creates one or more contacts in a Xero organisation

### [accounting.contacts.attachments](xero_accounting_py/resources/accounting/contacts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/contacts/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific contact using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/contacts/attachments/README.md#list) - Retrieves attachments for a specific contact in a Xero organisation

### [accounting.contacts.cis_settings](xero_accounting_py/resources/accounting/contacts/cis_settings/README.md)

- [list](xero_accounting_py/resources/accounting/contacts/cis_settings/README.md#list) - Retrieves CIS settings for a specific contact in a Xero organisation

### [accounting.contacts.history](xero_accounting_py/resources/accounting/contacts/history/README.md)

- [create](xero_accounting_py/resources/accounting/contacts/history/README.md#create) - Creates a new history record for a specific contact
- [list](xero_accounting_py/resources/accounting/contacts/history/README.md#list) - Retrieves history records for a specific contact

### [accounting.credit_notes](xero_accounting_py/resources/accounting/credit_notes/README.md)

- [create](xero_accounting_py/resources/accounting/credit_notes/README.md#create) - Creates a new credit note
- [get](xero_accounting_py/resources/accounting/credit_notes/README.md#get) - Retrieves a specific credit note using a unique credit note Id
- [list](xero_accounting_py/resources/accounting/credit_notes/README.md#list) - Retrieves any credit notes
- [update](xero_accounting_py/resources/accounting/credit_notes/README.md#update) - Updates a specific credit note
- [update_or_create](xero_accounting_py/resources/accounting/credit_notes/README.md#update_or_create) - Updates or creates one or more credit notes

### [accounting.credit_notes.allocations](xero_accounting_py/resources/accounting/credit_notes/allocations/README.md)

- [create](xero_accounting_py/resources/accounting/credit_notes/allocations/README.md#create) - Creates allocation for a specific credit note
- [delete](xero_accounting_py/resources/accounting/credit_notes/allocations/README.md#delete) - Deletes an Allocation from a Credit Note

### [accounting.credit_notes.attachments](xero_accounting_py/resources/accounting/credit_notes/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/credit_notes/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific credit note using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/credit_notes/attachments/README.md#list) - Retrieves attachments for a specific credit notes

### [accounting.credit_notes.history](xero_accounting_py/resources/accounting/credit_notes/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/credit_notes/history/README.md#create_record) - Retrieves history records of a specific credit note
- [list](xero_accounting_py/resources/accounting/credit_notes/history/README.md#list) - Retrieves history records of a specific credit note

### [accounting.credit_notes.pdf](xero_accounting_py/resources/accounting/credit_notes/pdf/README.md)

- [get](xero_accounting_py/resources/accounting/credit_notes/pdf/README.md#get) - Retrieves credit notes as PDF files

### [accounting.currencies](xero_accounting_py/resources/accounting/currencies/README.md)

- [create](xero_accounting_py/resources/accounting/currencies/README.md#create) - Create a new currency for a Xero organisation
- [list](xero_accounting_py/resources/accounting/currencies/README.md#list) - Retrieves currencies for your Xero organisation

### [accounting.employees](xero_accounting_py/resources/accounting/employees/README.md)

- [create](xero_accounting_py/resources/accounting/employees/README.md#create) - Creates new employees used in Xero payrun
- [get](xero_accounting_py/resources/accounting/employees/README.md#get) - Retrieves a specific employee used in Xero payrun using a unique employee Id
- [list](xero_accounting_py/resources/accounting/employees/README.md#list) - Retrieves employees used in Xero payrun
- [update_or_create](xero_accounting_py/resources/accounting/employees/README.md#update_or_create) - Creates a single new employees used in Xero payrun

### [accounting.expense_claims](xero_accounting_py/resources/accounting/expense_claims/README.md)

- [create](xero_accounting_py/resources/accounting/expense_claims/README.md#create) - Creates expense claims
- [get](xero_accounting_py/resources/accounting/expense_claims/README.md#get) - Retrieves a specific expense claim using a unique expense claim Id
- [list](xero_accounting_py/resources/accounting/expense_claims/README.md#list) - Retrieves expense claims
- [update](xero_accounting_py/resources/accounting/expense_claims/README.md#update) - Updates a specific expense claims

### [accounting.expense_claims.history](xero_accounting_py/resources/accounting/expense_claims/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/expense_claims/history/README.md#create_record) - Creates a history record for a specific expense claim
- [list](xero_accounting_py/resources/accounting/expense_claims/history/README.md#list) - Retrieves history records of a specific expense claim

### [accounting.invoice_reminders.settings](xero_accounting_py/resources/accounting/invoice_reminders/settings/README.md)

- [list](xero_accounting_py/resources/accounting/invoice_reminders/settings/README.md#list) - Retrieves invoice reminder settings

### [accounting.invoices](xero_accounting_py/resources/accounting/invoices/README.md)

- [create](xero_accounting_py/resources/accounting/invoices/README.md#create) - Creates one or more sales invoices or purchase bills
- [get](xero_accounting_py/resources/accounting/invoices/README.md#get) - Retrieves a specific sales invoice or purchase bill using a unique invoice Id
- [list](xero_accounting_py/resources/accounting/invoices/README.md#list) - Retrieves sales invoices or purchase bills
- [update](xero_accounting_py/resources/accounting/invoices/README.md#update) - Updates a specific sales invoices or purchase bills
- [update_or_create](xero_accounting_py/resources/accounting/invoices/README.md#update_or_create) - Updates or creates one or more sales invoices or purchase bills

### [accounting.invoices.attachments](xero_accounting_py/resources/accounting/invoices/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/invoices/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/invoices/attachments/README.md#list) - Retrieves attachments for a specific invoice or purchase bill

### [accounting.invoices.email](xero_accounting_py/resources/accounting/invoices/email/README.md)

- [send](xero_accounting_py/resources/accounting/invoices/email/README.md#send) - Sends a copy of a specific invoice to related contact via email

### [accounting.invoices.history](xero_accounting_py/resources/accounting/invoices/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/invoices/history/README.md#create_record) - Creates a history record for a specific invoice
- [list](xero_accounting_py/resources/accounting/invoices/history/README.md#list) - Retrieves history records for a specific invoice

### [accounting.invoices.online_invoice](xero_accounting_py/resources/accounting/invoices/online_invoice/README.md)

- [get](xero_accounting_py/resources/accounting/invoices/online_invoice/README.md#get) - Retrieves a URL to an online invoice

### [accounting.invoices.pdf](xero_accounting_py/resources/accounting/invoices/pdf/README.md)

- [get](xero_accounting_py/resources/accounting/invoices/pdf/README.md#get) - Retrieves invoices or purchase bills as PDF files

### [accounting.items](xero_accounting_py/resources/accounting/items/README.md)

- [create](xero_accounting_py/resources/accounting/items/README.md#create) - Creates one or more items
- [delete](xero_accounting_py/resources/accounting/items/README.md#delete) - Deletes a specific item
- [get](xero_accounting_py/resources/accounting/items/README.md#get) - Retrieves a specific item using a unique item Id
- [list](xero_accounting_py/resources/accounting/items/README.md#list) - Retrieves items
- [update](xero_accounting_py/resources/accounting/items/README.md#update) - Updates a specific item
- [update_or_create](xero_accounting_py/resources/accounting/items/README.md#update_or_create) - Updates or creates one or more items

### [accounting.items.history](xero_accounting_py/resources/accounting/items/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/items/history/README.md#create_record) - Creates a history record for a specific item
- [list](xero_accounting_py/resources/accounting/items/history/README.md#list) - Retrieves history for a specific item

### [accounting.journals](xero_accounting_py/resources/accounting/journals/README.md)

- [get](xero_accounting_py/resources/accounting/journals/README.md#get) - Retrieves a specific journal using a unique journal Id.
- [list](xero_accounting_py/resources/accounting/journals/README.md#list) - Retrieves journals

### [accounting.linked_transactions](xero_accounting_py/resources/accounting/linked_transactions/README.md)

- [create](xero_accounting_py/resources/accounting/linked_transactions/README.md#create) - Creates linked transactions (billable expenses)
- [delete](xero_accounting_py/resources/accounting/linked_transactions/README.md#delete) - Deletes a specific linked transactions (billable expenses)
- [get](xero_accounting_py/resources/accounting/linked_transactions/README.md#get) - Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id
- [list](xero_accounting_py/resources/accounting/linked_transactions/README.md#list) - Retrieves linked transactions (billable expenses)
- [update](xero_accounting_py/resources/accounting/linked_transactions/README.md#update) - Updates a specific linked transactions (billable expenses)

### [accounting.manual_journals](xero_accounting_py/resources/accounting/manual_journals/README.md)

- [create](xero_accounting_py/resources/accounting/manual_journals/README.md#create) - Creates one or more manual journals
- [get](xero_accounting_py/resources/accounting/manual_journals/README.md#get) - Retrieves a specific manual journal
- [list](xero_accounting_py/resources/accounting/manual_journals/README.md#list) - Retrieves manual journals
- [update](xero_accounting_py/resources/accounting/manual_journals/README.md#update) - Updates a specific manual journal
- [update_or_create](xero_accounting_py/resources/accounting/manual_journals/README.md#update_or_create) - Updates or creates a single manual journal

### [accounting.manual_journals.attachments](xero_accounting_py/resources/accounting/manual_journals/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/manual_journals/attachments/README.md#get_by_id) - Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/manual_journals/attachments/README.md#list) - Retrieves attachment for a specific manual journal

### [accounting.manual_journals.history](xero_accounting_py/resources/accounting/manual_journals/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/manual_journals/history/README.md#create_record) - Creates a history record for a specific manual journal
- [list](xero_accounting_py/resources/accounting/manual_journals/history/README.md#list) - Retrieves history for a specific manual journal

### [accounting.organisation](xero_accounting_py/resources/accounting/organisation/README.md)

- [list](xero_accounting_py/resources/accounting/organisation/README.md#list) - Retrieves Xero organisation details

### [accounting.organisation.actions](xero_accounting_py/resources/accounting/organisation/actions/README.md)

- [list](xero_accounting_py/resources/accounting/organisation/actions/README.md#list) - Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

### [accounting.organisation.cis_settings](xero_accounting_py/resources/accounting/organisation/cis_settings/README.md)

- [list](xero_accounting_py/resources/accounting/organisation/cis_settings/README.md#list) - Retrieves the CIS settings for the Xero organistaion.

### [accounting.overpayments](xero_accounting_py/resources/accounting/overpayments/README.md)

- [get](xero_accounting_py/resources/accounting/overpayments/README.md#get) - Retrieves a specific overpayment using a unique overpayment Id
- [list](xero_accounting_py/resources/accounting/overpayments/README.md#list) - Retrieves overpayments

### [accounting.overpayments.allocations](xero_accounting_py/resources/accounting/overpayments/allocations/README.md)

- [create](xero_accounting_py/resources/accounting/overpayments/allocations/README.md#create) - Creates a single allocation for a specific overpayment
- [delete](xero_accounting_py/resources/accounting/overpayments/allocations/README.md#delete) - Deletes an Allocation from an overpayment

### [accounting.overpayments.history](xero_accounting_py/resources/accounting/overpayments/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/overpayments/history/README.md#create_record) - Creates a history record for a specific overpayment
- [list](xero_accounting_py/resources/accounting/overpayments/history/README.md#list) - Retrieves history records of a specific overpayment

### [accounting.payment_services](xero_accounting_py/resources/accounting/payment_services/README.md)

- [create](xero_accounting_py/resources/accounting/payment_services/README.md#create) - Creates a payment service
- [list](xero_accounting_py/resources/accounting/payment_services/README.md#list) - Retrieves payment services

### [accounting.payments](xero_accounting_py/resources/accounting/payments/README.md)

- [create](xero_accounting_py/resources/accounting/payments/README.md#create) - Creates multiple payments for invoices or credit notes
- [create_1](xero_accounting_py/resources/accounting/payments/README.md#create_1) - Creates a single payment for invoice or credit notes
- [delete](xero_accounting_py/resources/accounting/payments/README.md#delete) - Updates a specific payment for invoices and credit notes
- [get](xero_accounting_py/resources/accounting/payments/README.md#get) - Retrieves a specific payment for invoices and credit notes using a unique payment Id
- [list](xero_accounting_py/resources/accounting/payments/README.md#list) - Retrieves payments for invoices and credit notes

### [accounting.payments.history](xero_accounting_py/resources/accounting/payments/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/payments/history/README.md#create_record) - Creates a history record for a specific payment
- [list](xero_accounting_py/resources/accounting/payments/history/README.md#list) - Retrieves history records of a specific payment

### [accounting.prepayments](xero_accounting_py/resources/accounting/prepayments/README.md)

- [get](xero_accounting_py/resources/accounting/prepayments/README.md#get) - Allows you to retrieve a specified prepayments
- [list](xero_accounting_py/resources/accounting/prepayments/README.md#list) - Retrieves prepayments

### [accounting.prepayments.allocations](xero_accounting_py/resources/accounting/prepayments/allocations/README.md)

- [create](xero_accounting_py/resources/accounting/prepayments/allocations/README.md#create) - Allows you to create an Allocation for prepayments
- [delete](xero_accounting_py/resources/accounting/prepayments/allocations/README.md#delete) - Deletes an Allocation from a Prepayment

### [accounting.prepayments.history](xero_accounting_py/resources/accounting/prepayments/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/prepayments/history/README.md#create_record) - Creates a history record for a specific prepayment
- [list](xero_accounting_py/resources/accounting/prepayments/history/README.md#list) - Retrieves history record for a specific prepayment

### [accounting.purchase_orders](xero_accounting_py/resources/accounting/purchase_orders/README.md)

- [create](xero_accounting_py/resources/accounting/purchase_orders/README.md#create) - Creates one or more purchase orders
- [get](xero_accounting_py/resources/accounting/purchase_orders/README.md#get) - Retrieves a specific purchase order using a unique purchase order Id
- [list](xero_accounting_py/resources/accounting/purchase_orders/README.md#list) - Retrieves purchase orders
- [update](xero_accounting_py/resources/accounting/purchase_orders/README.md#update) - Updates a specific purchase order
- [update_or_create](xero_accounting_py/resources/accounting/purchase_orders/README.md#update_or_create) - Updates or creates one or more purchase orders

### [accounting.purchase_orders.attachments](xero_accounting_py/resources/accounting/purchase_orders/attachments/README.md)

- [get_as_pdf](xero_accounting_py/resources/accounting/purchase_orders/attachments/README.md#get_as_pdf) - Retrieves specific purchase order as PDF files using a unique purchase order Id
- [get_by_id](xero_accounting_py/resources/accounting/purchase_orders/attachments/README.md#get_by_id) - Retrieves specific attachment for a specific purchase order using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/purchase_orders/attachments/README.md#list) - Retrieves attachments for a specific purchase order

### [accounting.purchase_orders.history](xero_accounting_py/resources/accounting/purchase_orders/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/purchase_orders/history/README.md#create_record) - Creates a history record for a specific purchase orders
- [list](xero_accounting_py/resources/accounting/purchase_orders/history/README.md#list) - Retrieves history for a specific purchase order

### [accounting.quotes](xero_accounting_py/resources/accounting/quotes/README.md)

- [create](xero_accounting_py/resources/accounting/quotes/README.md#create) - Create one or more quotes
- [get](xero_accounting_py/resources/accounting/quotes/README.md#get) - Retrieves a specific quote using a unique quote Id
- [get_as_pdf](xero_accounting_py/resources/accounting/quotes/README.md#get_as_pdf) - Retrieves a specific quote as a PDF file using a unique quote Id
- [list](xero_accounting_py/resources/accounting/quotes/README.md#list) - Retrieves sales quotes
- [update](xero_accounting_py/resources/accounting/quotes/README.md#update) - Updates a specific quote
- [update_or_create](xero_accounting_py/resources/accounting/quotes/README.md#update_or_create) - Updates or creates one or more quotes

### [accounting.quotes.attachments](xero_accounting_py/resources/accounting/quotes/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/quotes/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific quote using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/quotes/attachments/README.md#list) - Retrieves attachments for a specific quote

### [accounting.quotes.history](xero_accounting_py/resources/accounting/quotes/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/quotes/history/README.md#create_record) - Creates a history record for a specific quote
- [list](xero_accounting_py/resources/accounting/quotes/history/README.md#list) - Retrieves history records of a specific quote

### [accounting.receipts](xero_accounting_py/resources/accounting/receipts/README.md)

- [create](xero_accounting_py/resources/accounting/receipts/README.md#create) - Creates draft expense claim receipts for any user
- [get](xero_accounting_py/resources/accounting/receipts/README.md#get) - Retrieves a specific draft expense claim receipt by using a unique receipt Id
- [list](xero_accounting_py/resources/accounting/receipts/README.md#list) - Retrieves draft expense claim receipts for any user
- [update](xero_accounting_py/resources/accounting/receipts/README.md#update) - Updates a specific draft expense claim receipts

### [accounting.receipts.attachments](xero_accounting_py/resources/accounting/receipts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/receipts/attachments/README.md#get_by_id) - Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id
- [list](xero_accounting_py/resources/accounting/receipts/attachments/README.md#list) - Retrieves attachments for a specific expense claim receipt

### [accounting.receipts.history](xero_accounting_py/resources/accounting/receipts/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/receipts/history/README.md#create_record) - Creates a history record for a specific receipt
- [list](xero_accounting_py/resources/accounting/receipts/history/README.md#list) - Retrieves a history record for a specific receipt

### [accounting.repeating_invoices](xero_accounting_py/resources/accounting/repeating_invoices/README.md)

- [create](xero_accounting_py/resources/accounting/repeating_invoices/README.md#create) - Creates one or more repeating invoice templates
- [get](xero_accounting_py/resources/accounting/repeating_invoices/README.md#get) - Retrieves a specific repeating invoice by using a unique repeating invoice Id
- [list](xero_accounting_py/resources/accounting/repeating_invoices/README.md#list) - Retrieves repeating invoices
- [update](xero_accounting_py/resources/accounting/repeating_invoices/README.md#update) - Deletes a specific repeating invoice template
- [update_or_create](xero_accounting_py/resources/accounting/repeating_invoices/README.md#update_or_create) - Creates or deletes one or more repeating invoice templates

### [accounting.repeating_invoices.attachments](xero_accounting_py/resources/accounting/repeating_invoices/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounting/repeating_invoices/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific repeating invoice
- [list](xero_accounting_py/resources/accounting/repeating_invoices/attachments/README.md#list) - Retrieves attachments from a specific repeating invoice

### [accounting.repeating_invoices.history](xero_accounting_py/resources/accounting/repeating_invoices/history/README.md)

- [create_record](xero_accounting_py/resources/accounting/repeating_invoices/history/README.md#create_record) - Creates a history record for a specific repeating invoice
- [list](xero_accounting_py/resources/accounting/repeating_invoices/history/README.md#list) - Retrieves history record for a specific repeating invoice

### [accounting.reports](xero_accounting_py/resources/accounting/reports/README.md)

- [get](xero_accounting_py/resources/accounting/reports/README.md#get) - Retrieves a specific report using a unique ReportID
- [get_aged_payables_by_contact](xero_accounting_py/resources/accounting/reports/README.md#get_aged_payables_by_contact) - Retrieves report for aged payables by contact
- [get_aged_receivables_by_contact](xero_accounting_py/resources/accounting/reports/README.md#get_aged_receivables_by_contact) - Retrieves report for aged receivables by contact
- [get_balance_sheet](xero_accounting_py/resources/accounting/reports/README.md#get_balance_sheet) - Retrieves report for balancesheet
- [get_bank_summary](xero_accounting_py/resources/accounting/reports/README.md#get_bank_summary) - Retrieves report for bank summary
- [get_budget_summary](xero_accounting_py/resources/accounting/reports/README.md#get_budget_summary) - Retrieves report for budget summary
- [get_executive_summary](xero_accounting_py/resources/accounting/reports/README.md#get_executive_summary) - Retrieves report for executive summary
- [get_profit_and_loss](xero_accounting_py/resources/accounting/reports/README.md#get_profit_and_loss) - Retrieves report for profit and loss
- [get_ten_ninety_nine](xero_accounting_py/resources/accounting/reports/README.md#get_ten_ninety_nine) - Retrieve reports for 1099
- [get_trial_balance](xero_accounting_py/resources/accounting/reports/README.md#get_trial_balance) - Retrieves report for trial balance
- [list](xero_accounting_py/resources/accounting/reports/README.md#list) - Retrieves a list of the organistaions unique reports that require a uuid to fetch

### [accounting.setup](xero_accounting_py/resources/accounting/setup/README.md)

- [create](xero_accounting_py/resources/accounting/setup/README.md#create) - Sets the chart of accounts, the conversion date and conversion balances

### [accounting.tax_rates](xero_accounting_py/resources/accounting/tax_rates/README.md)

- [create](xero_accounting_py/resources/accounting/tax_rates/README.md#create) - Creates one or more tax rates
- [get](xero_accounting_py/resources/accounting/tax_rates/README.md#get) - Retrieves a specific tax rate according to given TaxType code
- [list](xero_accounting_py/resources/accounting/tax_rates/README.md#list) - Retrieves tax rates
- [update](xero_accounting_py/resources/accounting/tax_rates/README.md#update) - Updates tax rates

### [accounting.tracking_categories](xero_accounting_py/resources/accounting/tracking_categories/README.md)

- [create](xero_accounting_py/resources/accounting/tracking_categories/README.md#create) - Create tracking categories
- [delete](xero_accounting_py/resources/accounting/tracking_categories/README.md#delete) - Deletes a specific tracking category
- [get](xero_accounting_py/resources/accounting/tracking_categories/README.md#get) - Retrieves specific tracking categories and options using a unique tracking category Id
- [list](xero_accounting_py/resources/accounting/tracking_categories/README.md#list) - Retrieves tracking categories and options
- [update](xero_accounting_py/resources/accounting/tracking_categories/README.md#update) - Updates a specific tracking category

### [accounting.tracking_categories.options](xero_accounting_py/resources/accounting/tracking_categories/options/README.md)

- [create](xero_accounting_py/resources/accounting/tracking_categories/options/README.md#create) - Creates options for a specific tracking category
- [delete](xero_accounting_py/resources/accounting/tracking_categories/options/README.md#delete) - Deletes a specific option for a specific tracking category
- [update](xero_accounting_py/resources/accounting/tracking_categories/options/README.md#update) - Updates a specific option for a specific tracking category

### [accounting.users](xero_accounting_py/resources/accounting/users/README.md)

- [get](xero_accounting_py/resources/accounting/users/README.md#get) - Retrieves a specific user
- [list](xero_accounting_py/resources/accounting/users/README.md#list) - Retrieves users

### [projects](xero_accounting_py/resources/projects/README.md)

- [create](xero_accounting_py/resources/projects/README.md#create) - Create one or more new projects
- [get](xero_accounting_py/resources/projects/README.md#get) - Retrieves a single project
- [list](xero_accounting_py/resources/projects/README.md#list) - Retrieves all projects
- [patch](xero_accounting_py/resources/projects/README.md#patch) - creates a project for the specified contact
- [update](xero_accounting_py/resources/projects/README.md#update) - Updates a specific project

### [projects.projects_users](xero_accounting_py/resources/projects/projects_users/README.md)

- [list](xero_accounting_py/resources/projects/projects_users/README.md#list) - Retrieves a list of all project users

### [projects.tasks](xero_accounting_py/resources/projects/tasks/README.md)

- [create](xero_accounting_py/resources/projects/tasks/README.md#create) - Allows you to create a task
- [delete](xero_accounting_py/resources/projects/tasks/README.md#delete) - Allows you to delete a task
- [get](xero_accounting_py/resources/projects/tasks/README.md#get) - Retrieves a single project task
- [list](xero_accounting_py/resources/projects/tasks/README.md#list) - Retrieves all project tasks
- [update](xero_accounting_py/resources/projects/tasks/README.md#update) - Allows you to update a task

### [projects.time](xero_accounting_py/resources/projects/time/README.md)

- [create](xero_accounting_py/resources/projects/time/README.md#create) - Creates a time entry for a specific project
- [delete](xero_accounting_py/resources/projects/time/README.md#delete) - Deletes a time entry for a specific project
- [get](xero_accounting_py/resources/projects/time/README.md#get) - Retrieves a single time entry for a specific project
- [list](xero_accounting_py/resources/projects/time/README.md#list) - Retrieves all time entries associated with a specific project
- [update](xero_accounting_py/resources/projects/time/README.md#update) - Updates a time entry for a specific project

<!-- MODULE DOCS END -->
