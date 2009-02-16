Use case
=========

Configure a system that enables you to:

* buy products from a supplier,

* stock the products in a warehouse,

* sell these products to a customer.

The system should support all aspects of invoicing, payments to suppliers and receipts from customers.

Functional requirements
=========================

For working out the business case you'll have to model:

* the suppliers,

* the customers,

* some products,

* inventory for despatch,

* a purchase order,

* a sale order,

* invoices,

* payments.

To test the system you'll need at least one supplier, one customer, one product, a warehouse, a minimal chart of accounts and a bank account.

Database creation
===================

Use the technique outlined in Chapter 1 to create a new database, \ ``openerp_ch03``\  . This database will be free of data and contain the least possible amount of functionality as a starting point. You'll need to know your super administrator password for this – or you'll have to find somebody who does have it to create this seed database. You won't be able to use the \ ``openerp_ch1``\   or \ ``openerp_ch2``\   databases that you might have created so far in this book because they both contain demonstration data.

Start the database creation process from the  *Database Administration*  page by clicking  *Create*  and then completing the following fields on the  *Create Database*  form:

*  *Super administrator password* : by default it's \ ``admin``\  , if you or your system administrator haven't changed it,

*  *New database name* : \ ``openerp_ch03``\  ,

*  *Load Demonstration Data*  checkbox: \ ``not checked``\  ,

*  *Default Language* : \ ``English``\  .

Installing and configuring modules
===================================

All of the functional needs are provided by core modules from Open ERP:

* product management (the  ``product``  module),

* inventory control (the  ``stock``  module),

* accounting and finance (the  ``account``  module),

* purchase management (the  ``purchase``  module),

* sales management (the  ``sale``  module).

Connect to the new \ ``openerp_ch03``\   database as user \ ``admin``\   with its default password \ ``admin``\   (you might have to wait a few seconds before the system will allow you to connect if you've only just created it). Since this is the first time you've connected to it you'll have to go through the Setup wizard in steps:

	#.  *Select a profile*  select  *Profile* \ ``Minimal Profile``\  

	#.  *Define Main Company* and  *Report Header*  leave everything untouched on this page.

	#.  *Summary*  just click the  *Install* button.

	#.  *Installation done*  click  *Ok* 

Use the menu  *Administration > Modules Management > Modules > Uninstalled Modules*  to show the list of all modules that are registered within Open ERP but as yet uninstalled. Then:

	#. Enter \ ``product``\  into the  *Name* field and click  *Filter* to list the product module.

	#. Click the name \ ``product``\  in the list to display the product module in form view, rather than the list view that a search displays.

	#. Click the  *Install* button on the product module form.

	#. Click the  *Search* button at the top of the form to toggle back to the list view with search selection fields on it.

	#. Search for the sale module then select it, too, as you did with product, to show it in form view.

	#. Click the  *Dependencies* tab to see that you'll automatically be loading the \ ``product``\   \ ``stock``\  and \ ``mrp``\  modules along with the \ ``sale``\  module.

	#. Return to the  *Module* tab and then click its  *Install* button.

	#. Click  *Apply Upgrades* in the toolbar to the right.

	#. When the  *System Upgrade* form appears, review the list of Modules to update – it may be longer than you had expected, and now includes all the modules you need, because the dependencies themselves had their own dependencies.

	#. Click  *Start Upgrade*  wait for  *System Upgrade Done* to be displayed, then click  *Close* on that form.

	#. The main menu now displays all of the menu items that were loaded by the modules you installed.


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

