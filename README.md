# Xero Accounting API - Python

xero-accounting (10.0.0)

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

> A number of tests are failing due to invalid examples in `accounting.yml` see the lint report (`accounting-lint-report.csv`) for details.

```bash
poetry run pytests
```

## Module Documentation and Snippets

### [accounts](xero_accounting_py/resources/accounts/README.md)

- [create](xero_accounting_py/resources/accounts/README.md#create) - Creates a new chart of accounts
- [delete](xero_accounting_py/resources/accounts/README.md#delete) - Deletes a chart of accounts
- [get](xero_accounting_py/resources/accounts/README.md#get) - Retrieves a single chart of accounts by using a unique account Id
- [list](xero_accounting_py/resources/accounts/README.md#list) - Retrieves the full chart of accounts
- [update](xero_accounting_py/resources/accounts/README.md#update) - Updates a chart of accounts

### [accounts.attachments](xero_accounting_py/resources/accounts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/accounts/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific account using a unique attachment Id
- [list](xero_accounting_py/resources/accounts/attachments/README.md#list) - Retrieves attachments for a specific accounts by using a unique account Id

### [bank_transactions](xero_accounting_py/resources/bank_transactions/README.md)

- [create](xero_accounting_py/resources/bank_transactions/README.md#create) - Creates one or more spent or received money transaction
- [get](xero_accounting_py/resources/bank_transactions/README.md#get) - Retrieves a single spent or received money transaction by using a unique bank transaction Id
- [list](xero_accounting_py/resources/bank_transactions/README.md#list) - Retrieves any spent or received money transactions
- [update](xero_accounting_py/resources/bank_transactions/README.md#update) - Updates a single spent or received money transaction
- [update_or_create](xero_accounting_py/resources/bank_transactions/README.md#update_or_create) - Updates or creates one or more spent or received money transaction

### [bank_transactions.attachments](xero_accounting_py/resources/bank_transactions/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/bank_transactions/attachments/README.md#get_by_id) - Retrieves specific attachments from a specific BankTransaction using a unique attachment Id
- [list](xero_accounting_py/resources/bank_transactions/attachments/README.md#list) - Retrieves any attachments from a specific bank transactions

### [bank_transactions.history](xero_accounting_py/resources/bank_transactions/history/README.md)

- [create_record](xero_accounting_py/resources/bank_transactions/history/README.md#create_record) - Creates a history record for a specific bank transactions
- [list](xero_accounting_py/resources/bank_transactions/history/README.md#list) - Retrieves history from a specific bank transaction using a unique bank transaction Id

### [bank_transfers](xero_accounting_py/resources/bank_transfers/README.md)

- [create](xero_accounting_py/resources/bank_transfers/README.md#create) - Creates a bank transfer
- [get](xero_accounting_py/resources/bank_transfers/README.md#get) - Retrieves specific bank transfers by using a unique bank transfer Id
- [list](xero_accounting_py/resources/bank_transfers/README.md#list) - Retrieves all bank transfers

### [bank_transfers.attachments](xero_accounting_py/resources/bank_transfers/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/bank_transfers/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific bank transfer using a unique attachment ID
- [list](xero_accounting_py/resources/bank_transfers/attachments/README.md#list) - Retrieves attachments from a specific bank transfer

### [bank_transfers.history](xero_accounting_py/resources/bank_transfers/history/README.md)

- [create_record](xero_accounting_py/resources/bank_transfers/history/README.md#create_record) - Creates a history record for a specific bank transfer
- [list](xero_accounting_py/resources/bank_transfers/history/README.md#list) - Retrieves history from a specific bank transfer using a unique bank transfer Id

### [batch_payments](xero_accounting_py/resources/batch_payments/README.md)

- [create](xero_accounting_py/resources/batch_payments/README.md#create) - Creates one or many batch payments for invoices
- [delete](xero_accounting_py/resources/batch_payments/README.md#delete) - Updates a specific batch payment for invoices and credit notes
- [get](xero_accounting_py/resources/batch_payments/README.md#get) - Retrieves a specific batch payment using a unique batch payment Id
- [list](xero_accounting_py/resources/batch_payments/README.md#list) - Retrieves either one or many batch payments for invoices
- [update](xero_accounting_py/resources/batch_payments/README.md#update) - Updates a specific batch payment for invoices and credit notes

### [batch_payments.history](xero_accounting_py/resources/batch_payments/history/README.md)

- [create_record](xero_accounting_py/resources/batch_payments/history/README.md#create_record) - Creates a history record for a specific batch payment
- [list](xero_accounting_py/resources/batch_payments/history/README.md#list) - Retrieves history from a specific batch payment

### [branding_themes](xero_accounting_py/resources/branding_themes/README.md)

- [get](xero_accounting_py/resources/branding_themes/README.md#get) - Retrieves a specific branding theme using a unique branding theme Id
- [list](xero_accounting_py/resources/branding_themes/README.md#list) - Retrieves all the branding themes

### [branding_themes.payment_services](xero_accounting_py/resources/branding_themes/payment_services/README.md)

- [create](xero_accounting_py/resources/branding_themes/payment_services/README.md#create) - Creates a new custom payment service for a specific branding theme
- [list](xero_accounting_py/resources/branding_themes/payment_services/README.md#list) - Retrieves the payment services for a specific branding theme

### [budgets](xero_accounting_py/resources/budgets/README.md)

- [get](xero_accounting_py/resources/budgets/README.md#get) - Retrieves a specific budget, which includes budget lines
- [list](xero_accounting_py/resources/budgets/README.md#list) - Retrieve a list of budgets

### [contact_groups](xero_accounting_py/resources/contact_groups/README.md)

- [create](xero_accounting_py/resources/contact_groups/README.md#create) - Creates a contact group
- [get](xero_accounting_py/resources/contact_groups/README.md#get) - Retrieves a specific contact group by using a unique contact group Id
- [list](xero_accounting_py/resources/contact_groups/README.md#list) - Retrieves the contact Id and name of each contact group
- [update](xero_accounting_py/resources/contact_groups/README.md#update) - Updates a specific contact group

### [contact_groups.contacts](xero_accounting_py/resources/contact_groups/contacts/README.md)

- [create](xero_accounting_py/resources/contact_groups/contacts/README.md#create) - Creates contacts to a specific contact group
- [delete](xero_accounting_py/resources/contact_groups/contacts/README.md#delete) - Deletes a specific contact from a contact group using a unique contact Id
- [delete_all](xero_accounting_py/resources/contact_groups/contacts/README.md#delete_all) - Deletes all contacts from a specific contact group

### [contacts](xero_accounting_py/resources/contacts/README.md)

- [create](xero_accounting_py/resources/contacts/README.md#create) - Creates multiple contacts (bulk) in a Xero organisation
- [get](xero_accounting_py/resources/contacts/README.md#get) - Retrieves a specific contacts in a Xero organisation using a unique contact Id
- [list](xero_accounting_py/resources/contacts/README.md#list) - Retrieves all contacts in a Xero organisation
- [update](xero_accounting_py/resources/contacts/README.md#update) - Updates a specific contact in a Xero organisation
- [update_or_create](xero_accounting_py/resources/contacts/README.md#update_or_create) - Updates or creates one or more contacts in a Xero organisation

### [contacts.attachments](xero_accounting_py/resources/contacts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/contacts/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific contact using a unique attachment Id
- [list](xero_accounting_py/resources/contacts/attachments/README.md#list) - Retrieves attachments for a specific contact in a Xero organisation

### [contacts.cis_settings](xero_accounting_py/resources/contacts/cis_settings/README.md)

- [list](xero_accounting_py/resources/contacts/cis_settings/README.md#list) - Retrieves CIS settings for a specific contact in a Xero organisation

### [contacts.history](xero_accounting_py/resources/contacts/history/README.md)

- [create](xero_accounting_py/resources/contacts/history/README.md#create) - Creates a new history record for a specific contact
- [list](xero_accounting_py/resources/contacts/history/README.md#list) - Retrieves history records for a specific contact

### [credit_notes](xero_accounting_py/resources/credit_notes/README.md)

- [create](xero_accounting_py/resources/credit_notes/README.md#create) - Creates a new credit note
- [get](xero_accounting_py/resources/credit_notes/README.md#get) - Retrieves a specific credit note using a unique credit note Id
- [list](xero_accounting_py/resources/credit_notes/README.md#list) - Retrieves any credit notes
- [update](xero_accounting_py/resources/credit_notes/README.md#update) - Updates a specific credit note
- [update_or_create](xero_accounting_py/resources/credit_notes/README.md#update_or_create) - Updates or creates one or more credit notes

### [credit_notes.allocations](xero_accounting_py/resources/credit_notes/allocations/README.md)

- [create](xero_accounting_py/resources/credit_notes/allocations/README.md#create) - Creates allocation for a specific credit note
- [delete](xero_accounting_py/resources/credit_notes/allocations/README.md#delete) - Deletes an Allocation from a Credit Note

### [credit_notes.attachments](xero_accounting_py/resources/credit_notes/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/credit_notes/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific credit note using a unique attachment Id
- [list](xero_accounting_py/resources/credit_notes/attachments/README.md#list) - Retrieves attachments for a specific credit notes

### [credit_notes.history](xero_accounting_py/resources/credit_notes/history/README.md)

- [create_record](xero_accounting_py/resources/credit_notes/history/README.md#create_record) - Retrieves history records of a specific credit note
- [list](xero_accounting_py/resources/credit_notes/history/README.md#list) - Retrieves history records of a specific credit note

### [credit_notes.pdf](xero_accounting_py/resources/credit_notes/pdf/README.md)

- [get](xero_accounting_py/resources/credit_notes/pdf/README.md#get) - Retrieves credit notes as PDF files

### [currencies](xero_accounting_py/resources/currencies/README.md)

- [create](xero_accounting_py/resources/currencies/README.md#create) - Create a new currency for a Xero organisation
- [list](xero_accounting_py/resources/currencies/README.md#list) - Retrieves currencies for your Xero organisation

### [employees](xero_accounting_py/resources/employees/README.md)

- [create](xero_accounting_py/resources/employees/README.md#create) - Creates new employees used in Xero payrun
- [get](xero_accounting_py/resources/employees/README.md#get) - Retrieves a specific employee used in Xero payrun using a unique employee Id
- [list](xero_accounting_py/resources/employees/README.md#list) - Retrieves employees used in Xero payrun
- [update_or_create](xero_accounting_py/resources/employees/README.md#update_or_create) - Creates a single new employees used in Xero payrun

### [expense_claims](xero_accounting_py/resources/expense_claims/README.md)

- [create](xero_accounting_py/resources/expense_claims/README.md#create) - Creates expense claims
- [get](xero_accounting_py/resources/expense_claims/README.md#get) - Retrieves a specific expense claim using a unique expense claim Id
- [list](xero_accounting_py/resources/expense_claims/README.md#list) - Retrieves expense claims
- [update](xero_accounting_py/resources/expense_claims/README.md#update) - Updates a specific expense claims

### [expense_claims.history](xero_accounting_py/resources/expense_claims/history/README.md)

- [create_record](xero_accounting_py/resources/expense_claims/history/README.md#create_record) - Creates a history record for a specific expense claim
- [list](xero_accounting_py/resources/expense_claims/history/README.md#list) - Retrieves history records of a specific expense claim

### [invoice_reminders.settings](xero_accounting_py/resources/invoice_reminders/settings/README.md)

- [list](xero_accounting_py/resources/invoice_reminders/settings/README.md#list) - Retrieves invoice reminder settings

### [invoices](xero_accounting_py/resources/invoices/README.md)

- [create](xero_accounting_py/resources/invoices/README.md#create) - Creates one or more sales invoices or purchase bills
- [get](xero_accounting_py/resources/invoices/README.md#get) - Retrieves a specific sales invoice or purchase bill using a unique invoice Id
- [list](xero_accounting_py/resources/invoices/README.md#list) - Retrieves sales invoices or purchase bills
- [update](xero_accounting_py/resources/invoices/README.md#update) - Updates a specific sales invoices or purchase bills
- [update_or_create](xero_accounting_py/resources/invoices/README.md#update_or_create) - Updates or creates one or more sales invoices or purchase bills

### [invoices.attachments](xero_accounting_py/resources/invoices/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/invoices/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id
- [list](xero_accounting_py/resources/invoices/attachments/README.md#list) - Retrieves attachments for a specific invoice or purchase bill

### [invoices.email](xero_accounting_py/resources/invoices/email/README.md)

- [send](xero_accounting_py/resources/invoices/email/README.md#send) - Sends a copy of a specific invoice to related contact via email

### [invoices.history](xero_accounting_py/resources/invoices/history/README.md)

- [create_record](xero_accounting_py/resources/invoices/history/README.md#create_record) - Creates a history record for a specific invoice
- [list](xero_accounting_py/resources/invoices/history/README.md#list) - Retrieves history records for a specific invoice

### [invoices.online_invoice](xero_accounting_py/resources/invoices/online_invoice/README.md)

- [get](xero_accounting_py/resources/invoices/online_invoice/README.md#get) - Retrieves a URL to an online invoice

### [invoices.pdf](xero_accounting_py/resources/invoices/pdf/README.md)

- [get](xero_accounting_py/resources/invoices/pdf/README.md#get) - Retrieves invoices or purchase bills as PDF files

### [items](xero_accounting_py/resources/items/README.md)

- [create](xero_accounting_py/resources/items/README.md#create) - Creates one or more items
- [delete](xero_accounting_py/resources/items/README.md#delete) - Deletes a specific item
- [get](xero_accounting_py/resources/items/README.md#get) - Retrieves a specific item using a unique item Id
- [list](xero_accounting_py/resources/items/README.md#list) - Retrieves items
- [update](xero_accounting_py/resources/items/README.md#update) - Updates a specific item
- [update_or_create](xero_accounting_py/resources/items/README.md#update_or_create) - Updates or creates one or more items

### [items.history](xero_accounting_py/resources/items/history/README.md)

- [create_record](xero_accounting_py/resources/items/history/README.md#create_record) - Creates a history record for a specific item
- [list](xero_accounting_py/resources/items/history/README.md#list) - Retrieves history for a specific item

### [journals](xero_accounting_py/resources/journals/README.md)

- [get](xero_accounting_py/resources/journals/README.md#get) - Retrieves a specific journal using a unique journal Id.
- [list](xero_accounting_py/resources/journals/README.md#list) - Retrieves journals

### [linked_transactions](xero_accounting_py/resources/linked_transactions/README.md)

- [create](xero_accounting_py/resources/linked_transactions/README.md#create) - Creates linked transactions (billable expenses)
- [delete](xero_accounting_py/resources/linked_transactions/README.md#delete) - Deletes a specific linked transactions (billable expenses)
- [get](xero_accounting_py/resources/linked_transactions/README.md#get) - Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id
- [list](xero_accounting_py/resources/linked_transactions/README.md#list) - Retrieves linked transactions (billable expenses)
- [update](xero_accounting_py/resources/linked_transactions/README.md#update) - Updates a specific linked transactions (billable expenses)

### [manual_journals](xero_accounting_py/resources/manual_journals/README.md)

- [create](xero_accounting_py/resources/manual_journals/README.md#create) - Creates one or more manual journals
- [get](xero_accounting_py/resources/manual_journals/README.md#get) - Retrieves a specific manual journal
- [list](xero_accounting_py/resources/manual_journals/README.md#list) - Retrieves manual journals
- [update](xero_accounting_py/resources/manual_journals/README.md#update) - Updates a specific manual journal
- [update_or_create](xero_accounting_py/resources/manual_journals/README.md#update_or_create) - Updates or creates a single manual journal

### [manual_journals.attachments](xero_accounting_py/resources/manual_journals/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/manual_journals/attachments/README.md#get_by_id) - Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id
- [list](xero_accounting_py/resources/manual_journals/attachments/README.md#list) - Retrieves attachment for a specific manual journal

### [manual_journals.history](xero_accounting_py/resources/manual_journals/history/README.md)

- [create_record](xero_accounting_py/resources/manual_journals/history/README.md#create_record) - Creates a history record for a specific manual journal
- [list](xero_accounting_py/resources/manual_journals/history/README.md#list) - Retrieves history for a specific manual journal

### [organisation](xero_accounting_py/resources/organisation/README.md)

- [list](xero_accounting_py/resources/organisation/README.md#list) - Retrieves Xero organisation details

### [organisation.actions](xero_accounting_py/resources/organisation/actions/README.md)

- [list](xero_accounting_py/resources/organisation/actions/README.md#list) - Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

### [organisation.cis_settings](xero_accounting_py/resources/organisation/cis_settings/README.md)

- [list](xero_accounting_py/resources/organisation/cis_settings/README.md#list) - Retrieves the CIS settings for the Xero organistaion.

### [overpayments](xero_accounting_py/resources/overpayments/README.md)

- [get](xero_accounting_py/resources/overpayments/README.md#get) - Retrieves a specific overpayment using a unique overpayment Id
- [list](xero_accounting_py/resources/overpayments/README.md#list) - Retrieves overpayments

### [overpayments.allocations](xero_accounting_py/resources/overpayments/allocations/README.md)

- [create](xero_accounting_py/resources/overpayments/allocations/README.md#create) - Creates a single allocation for a specific overpayment
- [delete](xero_accounting_py/resources/overpayments/allocations/README.md#delete) - Deletes an Allocation from an overpayment

### [overpayments.history](xero_accounting_py/resources/overpayments/history/README.md)

- [create_record](xero_accounting_py/resources/overpayments/history/README.md#create_record) - Creates a history record for a specific overpayment
- [list](xero_accounting_py/resources/overpayments/history/README.md#list) - Retrieves history records of a specific overpayment

### [payment_services](xero_accounting_py/resources/payment_services/README.md)

- [create](xero_accounting_py/resources/payment_services/README.md#create) - Creates a payment service
- [list](xero_accounting_py/resources/payment_services/README.md#list) - Retrieves payment services

### [payments](xero_accounting_py/resources/payments/README.md)

- [create](xero_accounting_py/resources/payments/README.md#create) - Creates multiple payments for invoices or credit notes
- [create_1](xero_accounting_py/resources/payments/README.md#create_1) - Creates a single payment for invoice or credit notes
- [delete](xero_accounting_py/resources/payments/README.md#delete) - Updates a specific payment for invoices and credit notes
- [get](xero_accounting_py/resources/payments/README.md#get) - Retrieves a specific payment for invoices and credit notes using a unique payment Id
- [list](xero_accounting_py/resources/payments/README.md#list) - Retrieves payments for invoices and credit notes

### [payments.history](xero_accounting_py/resources/payments/history/README.md)

- [create_record](xero_accounting_py/resources/payments/history/README.md#create_record) - Creates a history record for a specific payment
- [list](xero_accounting_py/resources/payments/history/README.md#list) - Retrieves history records of a specific payment

### [prepayments](xero_accounting_py/resources/prepayments/README.md)

- [get](xero_accounting_py/resources/prepayments/README.md#get) - Allows you to retrieve a specified prepayments
- [list](xero_accounting_py/resources/prepayments/README.md#list) - Retrieves prepayments

### [prepayments.allocations](xero_accounting_py/resources/prepayments/allocations/README.md)

- [create](xero_accounting_py/resources/prepayments/allocations/README.md#create) - Allows you to create an Allocation for prepayments
- [delete](xero_accounting_py/resources/prepayments/allocations/README.md#delete) - Deletes an Allocation from a Prepayment

### [prepayments.history](xero_accounting_py/resources/prepayments/history/README.md)

- [create_record](xero_accounting_py/resources/prepayments/history/README.md#create_record) - Creates a history record for a specific prepayment
- [list](xero_accounting_py/resources/prepayments/history/README.md#list) - Retrieves history record for a specific prepayment

### [purchase_orders](xero_accounting_py/resources/purchase_orders/README.md)

- [create](xero_accounting_py/resources/purchase_orders/README.md#create) - Creates one or more purchase orders
- [get](xero_accounting_py/resources/purchase_orders/README.md#get) - Retrieves a specific purchase order using a unique purchase order Id
- [list](xero_accounting_py/resources/purchase_orders/README.md#list) - Retrieves purchase orders
- [update](xero_accounting_py/resources/purchase_orders/README.md#update) - Updates a specific purchase order
- [update_or_create](xero_accounting_py/resources/purchase_orders/README.md#update_or_create) - Updates or creates one or more purchase orders

### [purchase_orders.attachments](xero_accounting_py/resources/purchase_orders/attachments/README.md)

- [get_as_pdf](xero_accounting_py/resources/purchase_orders/attachments/README.md#get_as_pdf) - Retrieves specific purchase order as PDF files using a unique purchase order Id
- [get_by_id](xero_accounting_py/resources/purchase_orders/attachments/README.md#get_by_id) - Retrieves specific attachment for a specific purchase order using a unique attachment Id
- [list](xero_accounting_py/resources/purchase_orders/attachments/README.md#list) - Retrieves attachments for a specific purchase order

### [purchase_orders.history](xero_accounting_py/resources/purchase_orders/history/README.md)

- [create_record](xero_accounting_py/resources/purchase_orders/history/README.md#create_record) - Creates a history record for a specific purchase orders
- [list](xero_accounting_py/resources/purchase_orders/history/README.md#list) - Retrieves history for a specific purchase order

### [quotes](xero_accounting_py/resources/quotes/README.md)

- [create](xero_accounting_py/resources/quotes/README.md#create) - Create one or more quotes
- [get](xero_accounting_py/resources/quotes/README.md#get) - Retrieves a specific quote using a unique quote Id
- [get_as_pdf](xero_accounting_py/resources/quotes/README.md#get_as_pdf) - Retrieves a specific quote as a PDF file using a unique quote Id
- [list](xero_accounting_py/resources/quotes/README.md#list) - Retrieves sales quotes
- [update](xero_accounting_py/resources/quotes/README.md#update) - Updates a specific quote
- [update_or_create](xero_accounting_py/resources/quotes/README.md#update_or_create) - Updates or creates one or more quotes

### [quotes.attachments](xero_accounting_py/resources/quotes/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/quotes/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific quote using a unique attachment Id
- [list](xero_accounting_py/resources/quotes/attachments/README.md#list) - Retrieves attachments for a specific quote

### [quotes.history](xero_accounting_py/resources/quotes/history/README.md)

- [create_record](xero_accounting_py/resources/quotes/history/README.md#create_record) - Creates a history record for a specific quote
- [list](xero_accounting_py/resources/quotes/history/README.md#list) - Retrieves history records of a specific quote

### [receipts](xero_accounting_py/resources/receipts/README.md)

- [create](xero_accounting_py/resources/receipts/README.md#create) - Creates draft expense claim receipts for any user
- [get](xero_accounting_py/resources/receipts/README.md#get) - Retrieves a specific draft expense claim receipt by using a unique receipt Id
- [list](xero_accounting_py/resources/receipts/README.md#list) - Retrieves draft expense claim receipts for any user
- [update](xero_accounting_py/resources/receipts/README.md#update) - Updates a specific draft expense claim receipts

### [receipts.attachments](xero_accounting_py/resources/receipts/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/receipts/attachments/README.md#get_by_id) - Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id
- [list](xero_accounting_py/resources/receipts/attachments/README.md#list) - Retrieves attachments for a specific expense claim receipt

### [receipts.history](xero_accounting_py/resources/receipts/history/README.md)

- [create_record](xero_accounting_py/resources/receipts/history/README.md#create_record) - Creates a history record for a specific receipt
- [list](xero_accounting_py/resources/receipts/history/README.md#list) - Retrieves a history record for a specific receipt

### [repeating_invoices](xero_accounting_py/resources/repeating_invoices/README.md)

- [create](xero_accounting_py/resources/repeating_invoices/README.md#create) - Creates one or more repeating invoice templates
- [get](xero_accounting_py/resources/repeating_invoices/README.md#get) - Retrieves a specific repeating invoice by using a unique repeating invoice Id
- [list](xero_accounting_py/resources/repeating_invoices/README.md#list) - Retrieves repeating invoices
- [update](xero_accounting_py/resources/repeating_invoices/README.md#update) - Deletes a specific repeating invoice template
- [update_or_create](xero_accounting_py/resources/repeating_invoices/README.md#update_or_create) - Creates or deletes one or more repeating invoice templates

### [repeating_invoices.attachments](xero_accounting_py/resources/repeating_invoices/attachments/README.md)

- [get_by_id](xero_accounting_py/resources/repeating_invoices/attachments/README.md#get_by_id) - Retrieves a specific attachment from a specific repeating invoice
- [list](xero_accounting_py/resources/repeating_invoices/attachments/README.md#list) - Retrieves attachments from a specific repeating invoice

### [repeating_invoices.history](xero_accounting_py/resources/repeating_invoices/history/README.md)

- [create_record](xero_accounting_py/resources/repeating_invoices/history/README.md#create_record) - Creates a history record for a specific repeating invoice
- [list](xero_accounting_py/resources/repeating_invoices/history/README.md#list) - Retrieves history record for a specific repeating invoice

### [reports](xero_accounting_py/resources/reports/README.md)

- [get](xero_accounting_py/resources/reports/README.md#get) - Retrieves a specific report using a unique ReportID
- [get_aged_payables_by_contact](xero_accounting_py/resources/reports/README.md#get_aged_payables_by_contact) - Retrieves report for aged payables by contact
- [get_aged_receivables_by_contact](xero_accounting_py/resources/reports/README.md#get_aged_receivables_by_contact) - Retrieves report for aged receivables by contact
- [get_balance_sheet](xero_accounting_py/resources/reports/README.md#get_balance_sheet) - Retrieves report for balancesheet
- [get_bank_summary](xero_accounting_py/resources/reports/README.md#get_bank_summary) - Retrieves report for bank summary
- [get_budget_summary](xero_accounting_py/resources/reports/README.md#get_budget_summary) - Retrieves report for budget summary
- [get_executive_summary](xero_accounting_py/resources/reports/README.md#get_executive_summary) - Retrieves report for executive summary
- [get_profit_and_loss](xero_accounting_py/resources/reports/README.md#get_profit_and_loss) - Retrieves report for profit and loss
- [get_ten_ninety_nine](xero_accounting_py/resources/reports/README.md#get_ten_ninety_nine) - Retrieve reports for 1099
- [get_trial_balance](xero_accounting_py/resources/reports/README.md#get_trial_balance) - Retrieves report for trial balance
- [list](xero_accounting_py/resources/reports/README.md#list) - Retrieves a list of the organistaions unique reports that require a uuid to fetch

### [setup](xero_accounting_py/resources/setup/README.md)

- [create](xero_accounting_py/resources/setup/README.md#create) - Sets the chart of accounts, the conversion date and conversion balances

### [tax_rates](xero_accounting_py/resources/tax_rates/README.md)

- [create](xero_accounting_py/resources/tax_rates/README.md#create) - Creates one or more tax rates
- [get](xero_accounting_py/resources/tax_rates/README.md#get) - Retrieves a specific tax rate according to given TaxType code
- [list](xero_accounting_py/resources/tax_rates/README.md#list) - Retrieves tax rates
- [update](xero_accounting_py/resources/tax_rates/README.md#update) - Updates tax rates

### [tracking_categories](xero_accounting_py/resources/tracking_categories/README.md)

- [create](xero_accounting_py/resources/tracking_categories/README.md#create) - Create tracking categories
- [delete](xero_accounting_py/resources/tracking_categories/README.md#delete) - Deletes a specific tracking category
- [get](xero_accounting_py/resources/tracking_categories/README.md#get) - Retrieves specific tracking categories and options using a unique tracking category Id
- [list](xero_accounting_py/resources/tracking_categories/README.md#list) - Retrieves tracking categories and options
- [update](xero_accounting_py/resources/tracking_categories/README.md#update) - Updates a specific tracking category

### [tracking_categories.options](xero_accounting_py/resources/tracking_categories/options/README.md)

- [create](xero_accounting_py/resources/tracking_categories/options/README.md#create) - Creates options for a specific tracking category
- [delete](xero_accounting_py/resources/tracking_categories/options/README.md#delete) - Deletes a specific option for a specific tracking category
- [update](xero_accounting_py/resources/tracking_categories/options/README.md#update) - Updates a specific option for a specific tracking category

### [users](xero_accounting_py/resources/users/README.md)

- [get](xero_accounting_py/resources/users/README.md#get) - Retrieves a specific user
- [list](xero_accounting_py/resources/users/README.md#list) - Retrieves users

<!-- MODULE DOCS END -->
