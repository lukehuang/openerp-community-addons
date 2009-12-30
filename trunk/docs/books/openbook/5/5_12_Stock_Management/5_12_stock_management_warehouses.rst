.. index:: Warehouse

Warehouses
===========

Warehouses are designed for physical locations from which you can deliver to the customer and to which you receive raw materials. Then when you buy products from a supplier you should take account of which Warehouse you use for this purchase. This also enables the end user to not have to choose from a list of locations but simply a real warehouses.

Use the menu *Stock Management > Configuration > Warehouses* then click *New* to configure a new warehouse.

A warehouse is defined by a link between three locations:

* The stock location shows the place of products available for delivery to a customer direct from this warehouse. Availability is given by all the products in that location and any child locations.

* The entry location shows where ordered products are received from a supplier to that warehouse. It can be the same as the stock location if, for example, you want to do a quality control operation on your incoming raw materials.

* The outgoing location (called Output in the demonstration database) is designed as a buffer zone in which you store all the items that have been picked but not yet delivered to a customer. You're strongly advised not to put this location within the stock hierarchy but instead at a level higher or the same. 

    .. image:: images/stock_warehouse.png
       :align: center

*Warehouse parameters.*

You can also set an address for the warehouse. This address should ideally be an address for your company. Once the warehouse has been defined it can be used in:

* Minimum stock rules,

* Supplier orders,

* Customer orders (using the definition of a point of sale, which is linked to a warehouse).

.. index:: Procurement

Automatic procurement
------------------------

Several methods of automatically procuring products can be carried out by Open ERP:

* the workflow used by products that have the procurement mode *Make to Order*,

* using minimum stock rules for “Make to Stock” products,

* using the master production schedule for “Make to Stock” products.

The two last methods are described below.

.. index:: Orderpoint
.. index:: Minimum Stock Rule

Minimum stock rules
--------------------

To automatically make stock replenishment proposals, you can use minimum stock rules. To do this use the menu *Stock Management > Automatic Procurements > Minimum Stock Rules*. 

The rule is the following: if the virtual stock for the given is lower than the minimum stock indicated in the rule, the system will automatically propose a replenishment to increase the level of virtual stock to the maximum level given in the rule.

    .. image:: images/stock_min_rule.png
       :align: center

*List of minimum stock rules.*

.. tip::   **Point**  *Conflict resolution*

You may find that draft production or procurement orders don't happen correctly. That can happen if the system is badly configured (for example if you've forgotten to set the supplier on a product).

To check this, look at the list of procurements in the exception state in the menu *Stock Management > Automatic Procurements > Procurement Exceptions*. More detail on handling these exceptions is given in the chapter on Manufacturing.

It's important to underline that the rule is based on virtual quantities and not just on real quantities. It then takes account of the calculation of orders and receipts to come.

Take the following example:

* Products in stock: 15

* Products ordered but not delivered: 5

* Products in manfacture: 2

The rules defined are:

Minimum stock: 13

Maximum stock: 25.

Once the rules have been properly configured the purchasing manager only needs to look at the list of orders for confirmation with the supplier using the menu *Purchase Management > Purchase Orders > Requests for Quotation*.

Note that the restocking doesn't require that you buy from a supplier. If the product has a restocking method of 'to manufacture' the scheduler will generate a production order and not a supplier order.

You can also set multiple quantities in the minimum stock rules. If you set a multiple quantity of 3 the system will propose a restocking of 15 pieces not the 13 it really needs. In this case it automatically rounds the quantity upwards.

Once the rules have been properly configured the purchasing manager only needs to look at the list of orders for confirmation with the supplier using the menu *Purchase Management > Purchase Orders > Requests for Quotation*. He should then confirm them one by one starting with the most urgent at the top of the list.

In a minimum stock rule, when you indicate a warehouse it suggest a stock location by default in that warehouse. You can change that location by default when the scheduler completes, by location and not by warehouse.


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
