Stocks
=======

.. index::
   single: Virtual; Stock

In the product form you can find a report that will give you the stock levels of the various different products in any selected location. If you haven't selected any location, Open ERP calculates stocks for all of the physical locations.

.. tip::   Availability of stock

    Depending on whether you look at the product from a customer order or from the menu of a product form you can get different values for stock availability. If you use the product menu you get the stock in all of the physical stock locations. Looking at the product from the order you will only see the report of the warehouse selected in the order.

The two fields are:

* Real stock: quantity physical present in your warehouse,

* Virtual stock: calculated this way: real stock – outgoing + incoming.

.. tip::   **Point**  *Virtual Stock*

    Virtual stock is very useful because it shows what the salespeople can sell. If it's more than real stock it's because products are coming in and if it's smaller than real stock then it's because certain products are reserved for other orders.

.. tip::   **Point**  *Detail of future stock*

    To get more detail about future stock, you can use the report to the right of the product form 'Forecast of Future Stock'. Open ERP shows a graph of the change of stock in the days to come, varying as a function of purchase orders or confirmed production.

.. image:: images/stock_forecast.png
    :align: center

*Printout of provisional stock.*

Lead times and locations
-------------------------

The tab *Procurement and Locations* contains information about different lead times and locations. Three lead time figures are available:

* Customer Lead Time: lead time promised to the customer, expressed in number of days between the order and the deliver to the customer,

* Manufacturing Lead Time: lead time, in days, between a production order and the end of production of the finished product,

* Warranty: length of time in months for the warranty for the delivered products.

.. tip::   **More information**  *Warranty*

    The warranty will be used in the management of reparis and after-sales service. You will find more information on this subject in the chapter about manufacturing.

Fields in the section *Storage localisation* are given for information – they don't have any impact on the management of stock.

The counterpart locations are automatically proposed by the system but the different values can be modified. You'll find counterpart locations for:

* Production,

* Inventory,

* Procurement.

A procurement location is a temporary location for stock moves that haven't yet been finalized by the scheduler. When the system doesn't yet know if procurement is to be done by a purchase or production, Open ERP uses the counterpart location *Procurement*. You'll find there everything that hasn't yet been planned by the system. The quantities of product in this location cancel each other out.

.. index:: Inventory


Initial Inventory
-----------------

Once a product has been defined, use an initial inventory operation to put actual current quantities into the system by location for the products in stock. Use the menu *Stock Management > Periodical Inventory > New Periodical Inventory* for this.

.. image:: images/stock_inventory_new.png
    :align: center

*Defining a new inventory operation.*

Give a name (for example 'Initial Inventory' or 'Lost Product XYZ') and a date for each inventory operation. You can then enter data about the quantities available for each product by location. Start by showing the location, for example 'Stock', and then select the product. Open ERP automatically completes the actual quantity actually available for that product in the location shown. You can then change that value to correct the value in stock.

Enter data for a single line in your inventory:

* Location: Stock,

* Product: PC1 Computers,

* Quantity: 23 Units.

.. tip::   **Point**  *Inventory Turns*

    You are usually legally required to do a stock check of all your products at least once a year. As well as doing a complete annual stock check, Open ERP also supports the method of periodical inventory. 

    That means you can check the stock levels of a proportion of your products every so often. This system is accepted in France as long as you can guarantee that all of your products have been counted at least once per year. To do this, use the report *Stock Management > Reporting > Dates of Inventories*.

    This gives you the last inventory date by product.

    You can do this the same way for all products and all locations, so you only carry out small inventory operations through the year rather than a single large stock check at one point in the year (which usually turns out to be at an inconvenient time).

When your inventory operation is finished you can confirm it using the button to the bottom right of the form. Open ERP will then automatically create the stock moves to close the gaps, as mentioned at the start of this chapter. You can verify the moves generated using the second tab of the inventory operation form.

The correct levels of your product are now in your stock locations. A simple way of verifying this is to reopen the product form to see the quantities available in stock.

Reception of a supplier order
------------------------------

Supplier goods receipt forms are automatically prepared by Open ERP by the purchase management process. You'll find a list of all the awaited receipts in the menu *Stock Management > Incoming Goods > Items to be Processed*. Use the order number or the supplier name to find the right goods receipt form for confirmation of a goods in. This approach enables you to control quantities received by referring to the quantities ordered.

.. image:: images/stock_picking_in_tree.png
    :align: center

*List of items waiting.*

You can also do goods in data entry manually if there's no order, using the menu *Stock Management > Incoming Goods > Items to be Processed* followed by a click on *New*.

A new goods-in data entry form then opens. Enter the supplier data in the partner field and you can type in the reference number from your supplier in the field 'Origin'. You should then enter data about the products received in lines.

The source location is already completed by default because of your supplier selection. You should then give the destination location where you will place the products. For example, enter 'Stock'. At this stage you can set a lot number for traceability (this function will be described later in this chapter, so leave this field empty for the moment).

Once the form has been completed you can confirm the receipt of all the products at the same time using the *Process Now* button. If you want to enter data for a receipt that you're still waiting for click the button *Process Later* .

.. image:: images/stock_picking_in_form.png
    :align: center

*Form for coding in reception of goods from a supplier order.*

The products then arrive in stock and reflect the quantities shown on the product form.

In the goods receipt form, the field 'Invoicing Control' lets you influence the way you send invoices to suppliers. If this is set to 'To be invoiced' a supplier invoice will now be generated automatically in the draft state, based on the goods received. Your accountant then has to confirm this pre-invoicing once the supplier's invoice is received. This enables you to verify that the invoiced quantities correspond to the quantities received.

Customer delivery
------------------

Everything about goods receipt is also possible to do manually for a customer delivery. But this time, use the automated product delivery processes based on customer orders. Install the ``sale`` module so that you can proceed further in this section of the chapter.

Now create a new customer order from the menu *Sales Management > Sales Orders > New Quotation*. Enter the following data in this order:

* Shop: Tiny SPRL

* Customer: Agrolait

* Order Line:

  * Product: PC1 Computer,

  * Quantity: 3 PCE

  * Procurement Method: from stock.

You've seen already that Open ERP shows you the available product stock when you've selected list mode. The real stock is equal to the virtual stock because you've nothing to deliver to customers and you're not waiting for any of these products to be received into stock. The salesperson then has all the information needed to take orders efficiently.

.. image:: images/stock_sale_form.png
       :align: center

*Encoding an order for three computers.*

Then confirm the quotation to convert it to an order. If you return to the product form you'll see the virtual stock is now smaller than the real stock. That happens because three products have been reserved by the order that you created, so they can't be sold to another customer.

Start the scheduler through the menu *Manufacturing > Compute All Schedulers*. Its functionality will be detailed in the chapter about Manufacturing. This manages the reservation of products and places orders based on the dates promised to customers, and the various internal lead times and priorities.

.. tip::  **Point** *Just in Time*

    You can install the module ``mrp_jit`` to plan each order in real time after it's been confirmed. This means that you don't have to start the scheduler or wait for its periodical start time.

You can now look at the the list of deliveries waiting to be carried out using the menu *Stock Management > Outgoing Products > Available Packings*. You find a line there for your order representing the items to be sent. Double-click the line to see the detail of the items proposed by Open ERP.

.. image:: images/stock_picking_out_form.png
    :align: center

*Items for a customer order.*

.. tip::   **More information**  *States*

    Open ERP distinguishes between the states *confirmed* and *assigned*. You say that an item is confirmed when it's needed but the available stock is insufficient.

    You say that an item is assigned when the storesperson reserves it. The necessary products have been reserved for this specific operation.

You can confirm a customer delivery using the 'Confirm' button. A window then opens where you can enter the quantities actually delivered. If you enter a value less than the forecast one, Open ERP automatically generates a partial delivery notes and a new order for the remaining items. For this exercise, just confirm all the products.

If you return to the list of current orders you will see that your order has now been marked as delivered (done). A progress indicator from 0% to 100% is shown by each order so that the salesperson can follow the progress of their orders at a glance.

.. image:: images/stock_sale_tree.png
    :align: center

*List of orders with their delivery state.*

.. tip::  **More information** *Negative Stock*

    Stock Management is very flexible so that it can be effective. For example if you forget to enter products at goods in, this won't prevent you from sending them to customers. In Open ERP you can force all operations manually using the button “Force assignment”. In this case, your stocks risk falling negative. You should monitor all stocks for negative levels and carry out an inventory correction when that happens.

Analysing stock
---------------

Now look at the effect of these operations on stock management. There are several ways of viewing stocks:

* from the product form,

* from the locations,

* from the orders.

Start by opening the product form from the menu *Products > Products* and looking at the list of items. You'll immediately see the following information about the products:

* Real Stock,

* Virtual Stock.

If you want more information you can use the actions to the right of the form. If you click the report *Future Stock Forecast*, Open ERP opens a graphical view of the stock levels for the selected products changing with time over the days and weeks to come. The value at the left of the graph is the real stock (today) and the value at the right is the virtual stock (stock in the short term future).

To get the stock levels by location use the button *Stock by Location*.  Open ERP then gives you the stock of this product split out over all the possible locations. If you only want to see the physical locations in your company just filter this list using the Location Type *Internal Locations*. By default, physical locatiosn are already coloured red to distinguish them better. Consolidate locations (the sum of several locations, following the hierarchical structure) are coloured blue.

.. image:: images/stock_location_product_tree.png
    :align: center

*Stock quantities by location for a given product.*

You can get more detail about all the stock moves from the product form. You'll then see each move from a source location to a destination location. Everything that influences stock levels corresponds to a stock move.

You could also look at the stocks available in a location using the menu *Stock Management > Stock Locations Structure*. You can then use the structure shortcuts at the and the location tree in the main window. Click a location to look at the stocks by product. A location containing child locations shows the consolidated contents for all of its child locations.

You should now check the product quantities for various locations to familiarize yourself with this double-entry stock management system. You should look at:

* supplier locations to see how goods receipts are linked,

* customer locations to see how packing notes are linked,

* inventory locations to see the accumulated losses and profits,

* production locatiosn to see the value created for the company.

Also look at how the real and virtual stocks depend on the location selected. If you enter a supplier location:

* the real stock shows all of the product receipts coming from this type of supplier,

* the virtual stock takes into account the quantities expected from these suppliers(+ real stock + quantities expected from these suppliers). It's the same scheme for customer locations and production locations.


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
