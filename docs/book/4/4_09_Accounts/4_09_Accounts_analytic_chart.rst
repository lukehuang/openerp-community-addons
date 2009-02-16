.. index::
   single: Chart of Accounts; Analytic

To each enterprise its own analytic chart
===========================================

To illustrate analytic accounts clearly, you can follow three use cases, each in one of three different types of company:

	#. An industrial manufacturing enterprise.

	#. A law firm.

	#. An IT services company.

Case 1: an industrial manufacturing enterprise
-----------------------------------------------

In industry, you'll often find analytic charts of accounts structured into the departments and products that the company itself is built on.

So the objective is to examine the costs, sales and margins by department and by product. The first level of the structure comprises the different departments and the lower levels represent the product ranges that the company makes and sells. 

	.. note::  *Example Analytic representation of the chart of accounts for an industrial manufacturing company* 

		#. Marketing Department

		#. Commercial Department

		#. Administration Department

		#. Production

			* Product Range 1

			* Sub-groups

			* Product Range 2

In daily use it's useful to mark the analytic account on each purchase invoice. The analytic account is the one to which the costs of that purchase should be allocated. When the invoice is approved it will automatically generate the entries for both the general and the corresponding analytic accounts. So, for each entry on the general accounts there's at least one analytic entry that allocates costs to the department that incurred them.

Here's a possible breakdown of some general accounting entries for the example above, allocated to various analytic accounts:


.. csv-table::  **Breakdown of general and analytic accounting entries (Case 1)**
   :header: "General accounts","","","","","Analytic accounts",""
   :widths: 10,5,5,5,2,10,8
   
   "Title","Account","Debit","Credit","","Account","Value"
   "Purchase of Raw Material","600","1500","","","Production / Range 1","1 500"
   "Subcontractors","602","450","","","Production / Range 2","-450"
   "Credit Note for defective materials","600","","200","","Production / Range 1","200"
   "Transport charges","613","450","","","Production / Range 1","-450"
   "Staff costs","6201","10000","","","Marketing","-2 000"
   "","","","","","Commercial","-3 000"
   "","","","","","Administrative","-1 000"
   "","","","","","Production / Range 1","-2 000"
   "","","","","","Production / Range 2"," 2 000"
   "PR ","614","450","","","Marketing"," 450 "

The analytic representation by department enables you to investigate the costs allocated to each department in the company.

So the analytic chart of accounts shows the distribution of the company's costs using the example above:



.. csv-table::  **Analytic chart of accounts (Case 1)**
   :header: "Account","Total"
   :widths: 10, 5
   
   "Marketing Department","-2 450 "
   "Commercial Department","-3 000 "
   "Administration Department","-1 000 "
   "Production","-6 200 "
   "Product Range 1","-3 750"
   "Product Range 2","-2 450"

In this example of a hierarchical structure in Open ERP you can analyze not only the costs of each product range but also the costs of the whole of production. The balance of a summary account ( *Production* ) is the sum of the balances of the child accounts.

A report that relates both general accounts and analytic accounts enables you to get a breakdown of costs within a given department. An analysis of the Production / Product Range 1 department is shown in this table:



.. csv-table:: **Report merging both general and analytic accounts for a department (Case 1)**
   :header: "Production / Product Range 1",""
   :widths: 10,5
   
   "General Account","Amount"
   "600 – Raw Materials"," 1 300"
   "613 – Transport charges","- 450"
   "6201 – Staff costs","-2 000"
   "Total","-3 750"



The examples above are based on a breakdown of the costs of the company. Analytic allocations can be just as effective for sales. That gives you the profitability (sales - costs) of different departments.

.. tip::   **Alternative**  *Representation by unique product range* 

	This analytic representation by department and by product range is usually used by trading companies and industry.

	A variant of this is not to break it down by commercial and marketing departments but to assign each cost to its corresponding product range. This will give you an analysis of the profitability of each product range.

	Choosing one over the other depends on how you look at your marketing effort. Is it a global cost allocated in some general way or does each product range have responsibility for its own marketing costs?

Case 2: a law firm
-------------------

Law firms generally adopt management by case where each case represents a current client file. All of the expenses and products are then attached to a given file.

A principal preoccupation of law firms is the invoicing of hours worked and the profitability by case and by employee.

Mechanisms used for encoding the hours worked will be covered in detail in the following chapter. Like most system processes, hours worked are integrated into the analytic accounting. Every time an employee enters a timesheet for a number of hours, that automatically generates analytic accounts corresponding to the cost of those hours in the case concerned. The hourly charge is a function of the employee's salary.

So a law firm will opt for an analytic representation which reflects the management of the time that employees work on the different client cases.

	.. note::  *Example Representation of an analytic chart of accounts for a law firm* 

		#. Absences

			* Paid Absences

			* Unpaid Absences

		#. Internal Projects

			* Administrative

			* Others

		#. Client cases

			* Client 1

			* Case 1.1

			* Case 1.2

			* Client 2

			* Case 2.1

All expenses and sales are then attached to a case. This gives the profitability of each case and, at a consolidated level, of each client.

Billing for the different cases is a bit unusual. The cases don't match any entry on the general account and nor do they come from purchase or sale invoices. They're represented by the various analytic operations and don't have exact counterparts in the general accounts. They're calculated on the basis of the hourly cost per employee. These entries are automatically created on billing worksheets.

At the end of the month when you pay salaries and benefits, you integrate them into the general accounts but not in the analytic accounts, because they've already been accounted for in billing each account. A report that relates data from the analytic and general accounts then lets you compare the totals, so you can readjust your estimates of hourly cost per employee depending on the time actually worked.

The following table gives an example of different analytic entries that you can find for your analytic account:


.. csv-table::  **Analytic entries for the account chart (Case 2)**
   :header: "Title","Account","Amount","","General Account","Debit","Credit"
   :widths: 15, 10, 8 ,2,15 ,8,8
   
   "Study the file (1 h)","Case 1.1","-15","","","",""
   "Search for information (3 h)","Case 1.1","-45","","","",""
   "Consultation (4 h)","Case 2.1","-60","","","",""
   "Service charges","Case 1.1","280","","705 – Billing services","","280"
   "Stationery purchase","Administrative","-42","","601 – Furniture purchase","42",""
   "Fuel Cost -Client trip","Case 1.1","-35","","613 – Transports","35",""
   "Staff salaries","","","","6201 – Salaries","","3 000"

You'll instantly see that it allows you to make a detailed study of the profitability of different transactions. In this example the cost of Case 1.1 is 95.00 (the sum of the analytic costs of studying the files, searching for information and service charges), but has been invoiced for 280.00, which gives you a gross profit of 185.00.

But an interest in analytical accounts isn't limited to a simple analysis of the profitability of different cases.

This same data can be used for automatic recharging of the services to the client at the end of the month. To invoice clients just take the analytic costs in that month and apply a selling price factor to generate the invoice. Invoicing mechanisms for this are explained in greater detail in chapter 11. If the client requires details of the services used on the case, you can then print the service entries in the analytic account for this case.

.. tip::   **Advantage**  *Invoicing analytic costs* 

	Most software that manages billing enables you to recharge for hours worked. In Open ERP these services are automatically represented by analytic costs. But many other Open ERP documents can also generate analytic costs, such as credit notes and purchases of goods.

	So when you invoice the client at the end of the month it's possible for you to include all the analytic costs, not just the hours worked. So, for example you can easily recharge the whole cost of your journeys to the client.

Case 3 : An IT Services Company
---------------------------------

Most IT services companies face the following problems:

* project planning,

* invoicing, profitability and financial follow-up of projects,

* managing support contracts.

To deal with these problems you'd use an analytic chart of accounts structured by project and by contract. A representation of that is given in the following example.

	.. note::  *Example Analytic representation of a chart of accounts for an IT Services company* 

		#. Internal Projects

			* Administrative and Commercial

			* Research and Development

		#. Client Projects

			* Client 1

			* Project 1.1

			* Project 1.2

			* Client 2

			* Project 2.1

			* Project 2.2

		#. Support Contracts – 20h

			* Customer X

			* Customer Y

The management of services, expenditures and sales is similar to that presented above for lawyers. Invoicing and the study of profitability are also similar.

But now look at support contracts. These contracts are usually limited to a prepaid number of hours. Each service posted in the analytic accounts shows the remaining available hours of support. For the management of support contracts you'd use the quantities and not the amounts in the analytic entries. 

In Open ERP each analytic line lists the number of units sold or used, as well as what you'd usually find there – the amount in currency units (USD or GBP, or whatever other choice you make). So you can sum the quantities sold and used on each analytic account to determine whether any hours of the support contract remain.

To differentiate services from other costs in the analytic account you use the concept of the analytic journal. Analytic entries are then allocated into the different journals:

* service journal,

* expense journal,

* sales journal,

* purchase journal.

So to obtain the detailed breakdown of a support contract you only have to look at the service journal for the analytic account corresponding to the contract in question.

Finally, the analytic account can be used to forecast future needs. For example, monthly planning of staff on different projects can be seen as an analytic budget limited to the service journal. Accounting entries are expressed in quantities (such as number of hours, and numbers of products) and in amounts in units of currency (USD or GBP perhaps). 

So you can set up planning on the basis just of quantities. Analyzing the analytic budget enables you to compare the budget (that is, your plan) to the services actually carried out by month end.

.. tip::   **Advice**  *Cash Budgets* 

	Problems of cash management are amongst the main difficulties encountered by small growing businesses. It's really difficult to predict the amount of cash that will be available when a company is young and rapidly growing. 

	If the company adopts management by case, then staff planning can be represented on the analytic accounts report, as you have seen. 

	But since you know your selling price for each of the different projects, you can see that it's easy to use the plan in the analytic accounts to precisely anticipate the amounts that you'll invoice in the coming months.


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

