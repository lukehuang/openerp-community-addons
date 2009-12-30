.. index::
   single: Contracts
.. 

Managing Service Contracts
===========================

Contracts can take different forms within Open ERP, depending on their nature. So you can have several distinct types of service contract, such as:

* fixed-price contracts

* cost-reimbursement contracts, invoiced when services are completed,

* fixed-price contracts, invoiced monthly as services are carried out

.. tip::   **Case**  *Contract quotations* 

	Some companies commit to contracts on the basis of a requested volume at a certain price for a defined period. In this case the contract is represented by a pricelist for that specific customer.

	The pricelist is linked in the Properties tab of the customer's Partner form, so that it is brought up whenever anything is bought from or sold to this partner (depending on whether it's a purchase or sales agreement). Open ERP automatically selects a price based on this agreed pricelist.

Fixed Price contracts
-----------------------

Fixed price contracts for the sale of services are represented in Open ERP by a Sales Order. In this case, the supply of services is managed just like all other stockable or consumable products. 

You can add new orders using the menu  *Sales Management > Sales Order* .

The new Sales Order document starts in the \ ``Quotation``\   state, so the estimate has no accounting impact on the system until it's confirmed. When you approve the document, your estimate moves into the state \ ``In Progress``\  .

.. image::  images/service_sale_workflow.png
	:align: center

*Process for handling a Sales Order*

Once the order has been approved, Open ERP will automatically generate an invoice and/or a delivery document proposal based on the parameters you set in the order. 

The invoice will be managed by the system depending on the setting of the field  *Shipping Policy*  on the order's second tab,  *Other data* :

*  *Payment before delivery* : Open ERP creates an invoice in the \ ``Draft``\   state. Once this is confirmed and paid the delivery is activated.

*  *Automatic Invoice after delivery* : the delivery order is produced when the order is validated. A draft invoice is then created when the delivery has been completed.

*  *Shipping & Manual Invoice* : Open ERP starts the delivery from the confirmation of the order, and adds a button which you manually click when you're ready to create an invoice.

*  *Invoice from the Packings* 

.. index:: Delivery

.. tip::   **Attention**  **  *Delivery of an order* 

	The term 'delivery' should be taken in the broadest sense in Open ERP. The effect of a delivery depends on the configuration of the sold product.

	If its type is either Stockable Product or Consumable, Open ERP will make a request for it to be sent for packing. If the product's type is Service Open ERP's scheduler will create a task in the project management system, or create a subcontract purchase order if the product's Procure Method is Make to Order.

	Invoicing after delivery does as it says: invoicing for the services when the tasks have been closed.

When you sign a new contract you can just enter the order into the system and Open ERP will track the order.

This works well for small orders. But for larger value services orders you might want to invoice several times through the contract, for example:

* 30% on order,

* 40% on completion,

* 30% one month after the system has gone into production.

In this case you should create several invoices for the one order. You've two options for this:

* Don't handle invoicing automatically from the order but carry out manual invoicing instead,

* Create draft invoices and then link to them in the third tab  *History* , in the  *Related Invoices*  section. When you create an invoice from the order, Open ERP deducts the amounts of the invoices already linked to the order to calculate the proposed invoice value.

Cost-reimbursement contracts
-----------------------------

Some contracts aren't invoiced from a price fixed on the order but from the cost of the services carried out. That's usually what happens in the building sector or in large projects.

The approach you use for this is totally different because instead of using the sales order as the basis of the invoice you must use the analytic accounts. For this you have to install the module \ ``hr_timesheet_invoice``\  .

An analytic account is created for each new contract. The following fields must be completed in this analytic account:

*  *Partner* : partner associated with the contract,

*  *Sale Pricelist* 

*  *Invoicing* 

The selection of an invoicing rate is an indirect way of specifying that the project will be invoiced on the basis of analytic costs. This can take different forms, such as delivery of services, purchase of raw materials, and expense reimbursements.

.. index::
   single: Pricelists
.. 

.. tip::   **Advice**  *Pricelists and billing rates* 

	You can select a pricelist on the analytic account without having to use it to specify billing rates.

	This case is for a client project that is to be invoiced, but not directly from the analytic costs. Putting the price list on the analytic account makes it possible to compare the actual sales with the best case where all the services would be invoiced. To get this comparison you have to print the analytic balance from the analytic account.

Services are then entered onto timesheets by the various people who work on the project. Periodically the project manager or account manager uses the following menu to prepare an invoice:  *Financial Management > Periodical Processing > Invoicing on a Time basis > Uninvoiced Hours* .

Open ERP then displays all of the costs that haven't yet been invoiced. You can filter the proposed list and click the appropriate action button to generate the corresponding invoices. You can select the level of detail which is reported on the invoice, such as the date and details of the services.

.. image::  images/service_timesheet_invoice.png
	:align: center

*Screen for invoicing services*

 *Project Management > Analytic Accounts* 

.. tip::   **Point**  *Project Management and analytic accounts* 

	The menu *Project Management > Analytic Accounts* is only available once you have installed the module ``account_analytic_analysis``. It provides various global financial and operational views of a project manager's projects.

Select a project and open its analytic entries using the  *Costs to invoice*  button. You'll find a list of costs that can be invoiced to the client:

* time worked,

* expense reimbursement,

* purchase of raw materials.

You can then invoice the selected lines using the action  *Invoice costs* .

Fixed-price contracts invoiced as services are worked
-------------------------------------------------------

For larger-value projects, fixed-price invoicing based on the sales order isn't always appropriate. In the case of a services project planned to run for about six months. invoicing could be based on the following:

* 30% on order,

* 30% at the project mid-point,

* 40% at delivery.

Such an approach is often used in a company but there are other options. This method of invoicing can pose many problems for the organization and invoicing of the project:

* It's extremely difficult to determine if the project is on track or not.. The endpoint is fuzzy, which can result in a tricky discussion with the client at the moment of final invoicing.

* If the project takes more or less time than forecast, it will effectively result in under- or over- invoicing during the project.

* Whether you get a proper return can depend on the client. For example if the client takes a long time to sign off on project acceptance you can't invoice the remaining 40% even though you might have supplied the agreed service properly.

* The account manager and the project manager are often different people. The project manager has to alert the account manager the moment that the client can be invoiced, but that moment easily can be forgotten or mistaken.

* The project can be fixed for service costs but have agreed extras, such as reimbursement for travel expenses. Invoicing from the order doesn't adapt well to such an approach.

Open ERP provides a third method for invoicing services that can be useful on long projects. This consists of invoicing the project periodically on the basis of time worked up to a fixed amount that can't be exceeded. At the end of the project a final invoice or a credit note is generated to meet the total amount of value fixed for the project.

To configure such a project you must set an invoicing rate, a pricelist and a maximum amount on the analytic account for the project. The services are then invoiced throughout the project by the different project or account managers, just like projects that are invoiced by time used. The managers can apply a refund on the final invoice if the project takes more time to complete than permitted under the contract.

When the project is finished you can generate the closing invoice using the  *Final Invoice*  button on the analytic account. This automatically calculates the final balance of the bill, taking the amounts already charged into account. If the amount already invoiced is greater than the maximum agreed amount then Open ERP generates a draft credit note.

This approach offers many advantages compared with the traditional methods of invoicing in phases for fixed-price contracts:

* Fixed-price contracts and cost-reimbursable contracts are invoiced in the same way, which makes the company's invoicing process quite simple and systematic even when the projects are mixed.

* Everything is invoiced on the basis of worked time, making it easy to forecast invoicing from plans linked to the different analytical accounts.

* This method of proceeding educates project managers just as much as the client because refunds have to be given for work done if the project slips.

* Invoicing follows the course of the project and avoids a supplier's dependence on the goodwill of the client in approving certain phases.

* Invoicing of expenses follows the same workflow and is therefore very simple.

.. tip::   **Advice**  *Negotiating contracts* 

	In contract negotiation, invoicing conditions are often neglected by the client. So it can often be straightforward to apply this method of invoicing.

Contracts limited to a quantity
---------------------------------

Finally certain contracts are expressed in terms of a quantity rather than a fixed amount. Support contracts comprising a number of prepaid hours are a case in point. To generate such contracts in Open ERP you should start by installing the module \ ``account_analytic_analysis``\  .

Then you can set a maximum number of hours for each analytic account. When employees enter their time worked on the support contract in the timesheets, the hours are automatically deducted from the maximum set on each analytic account.

You must also name someone in the company responsible for renewing expired contracts. They become responsible for searching through the list of accounts showing negative remaining hours.

The client contract can be limited to a certain quantity of hours, and it can also be limited in time. For that, you set an end date for the corresponding analytic account.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Presses) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open ERP Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open ERP Press, Grand Rosière, Belgium

