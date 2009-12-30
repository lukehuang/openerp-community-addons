Complete workflow from supplier to customer
===========================================

Now you'll follow a practical example by adapting stock management operations. In order you'll see:

* defining a new product,

* initial setting of inventory,

* receiving products from a supplier,

* delivering to a customer,

* analysis of the state of stock.

Defining a new product
-----------------------

To start, define the following product:

==================== ======================
Field                Value
==================== ======================
Name                 Central Heating Type 1
Code                 CCT1
Product Type         Stockable
Method of restocking Purchase
==================== ======================

Use the menu *Products > Products*, then click *New* to define a new product. 

    .. image:: images/stock_product.png
       :align: center

*Definition of a new product.*

Three fields are important for stock management when you're configuring a new product:

* Product Type,

* Procure Method,

* Supply Method.

Product Types
--------------

The product type indicates if the product is handled in stock management and if Open ERP manages its procurement. The three distinct product types are:

* Stockable Product: this product is used in stock management and its replenishment is more or less automated as defined by the rules established in the system. Examples, a bicycle, a computer or a central heating system.

* Consumable: handled in stock management, you can receive it, deliver it and make it. But its stock level isn't managed by the system. Open ERP assumes that you've got sufficient levels in stock at all time, so it doesn't restock it automatically. Example, nails.

* Services: don't appear in the various stock operations. Example, a consulting service.

Procurement Methods – Make to Stock and Make to Order
------------------------------------------------------

The procurement method shows how the product will be replenished:

* Make to Stock: your customers are supplied from available stock. You procure a significant quantity of each product when its stock is too low. Example, a classic distributor.

* Make to Order: when a customer order is confirmed, you then procure or manufacture the products for this order. A customer order 'Make to Order' won't modify stock in the medium term because you restock with the exact amount that was ordered. Example, computers from a large supplier assembled on demand.

You find a mix of these two modes used for the different final and intermediate products in most industries. The procurement method shown on the product form is a default value for the order, enabling the salesperson to choose the best mode for fulfilling a particular order.

The figures below show the change of stock levels for a product managed Make to Order and one managed Make to Stock. The two figures are taken from Open ERP's *Future Stock Moves* report, available from the product form.

    .. image:: images/stock_from_stock.png
       :align: center

*Change in stock for a product managed as Make to Stock.*

    .. image:: images/stock_from_order.png
       :align: center

*Change in stock for a product managed as Make to Order.*

.. tip::  *Information** *Logistical Methods*

     The *Make to Stock* logistical approach is usually used for high volumes and when the demand is seasonal or otherwise easy to forecast. The *Make to Order* approach is used for products that are measured, or very costly to stock or have a short re-stocking time.

Supply Methods
---------------

Open ERP supports two methods of procurement:

* Make: when the product or service is supplied from internal resources,

* Buy: when the product is bought from a supplier.

These are just the default settings used by the system during automated replenishment. The same product can be either manufactured internally or bought from a supplier.

The three fields (Supply Method, Procurement Method, Product Type) determine the system's behaviour when a product is required. The system will generate different documents depending on the configuration of these three fields when satisfying an order, a price quotation to a supplier or a manufacturing order.

Open ERP manages both stockable products and services. A service bought from a supplier in *Make to Order* mode, will generate a subcontract order from the supplier in question.

The following illustrates the different cases for automatic restocking.

    .. image:: images/stock_flow.png
       :align: center

*Workflow for automatic restocking, depending on the configuration of the product.*

The table below shows all possible cases for the figure.

================== ===================== =====================
Mode of restocking Make                  Buy
================== ===================== =====================
MTS                Wait for availability Wait for availability
MTO                Production Order      Supplier Order
================== ===================== =====================

*Showing restocking for a product of type 'stockable' or 'consumable'.*

================== ===================== =====================
Mode of restocking Produce               Purchase
================== ===================== =====================
MTS                /                     /
MTO                Create task           Subcontract
================== ===================== =====================

*Showing restocking for a product of type 'service'.*

You'll see the automated management processes for restocking in detail further on in this chapter.

Units of Measure
-----------------

Open ERP supports several units of measure. Quantities of the same product can be expressed in several units of measure at once. For example you can buy grain by the tonne and resell it by kg.  You just have to make sure that all the units of measure used for a product are in the same units of measure category.

.. tip:: **Definition** *Categories of units of measure*

    All units of measure in a category are convertible from one unit to another.

The table below shows some examples of units of measure and their category. The factor is used to convert from one unit of measure to another as long as they are in the same category.

========= ============ ======
UoM       Category     Factor
========= ============ ======
Kg        Weight            1
Gram      Weight         1000
Tonne     Weight         0.01
Hour      Working time      8
Day       Working time      1
Half-day  Working time      2
Item      Unit              1
100 Items Unit           0.01
========= ============ ======

Depending on the table above you have 1Kg = 1000g = 0.001 Tonnes. A product in the “Weight” category could be expressed in Kg, Tonnes or Grammes. You can't express them in hours or pieces.

Use the menu *Products > Configuration > Units of Measure > Units of Measure* to define a new unit of measure. 

In the definition of a Unit of Measure, you have a *Rounding precision* factor which shows how amounts are rounded after the conversion. A value of 1 gives rounding to the level of one unit. 0.01 gives rounding to one hundredth.

.. tip::   **Advice**  *Secondary Units*

    Open ERP supports double units of measure. In this case, the whole of the stock management system is encoded in two units that don't have a real link between them. This is very useful in the agro-food industry, for example: you sell ham by the piece but invoice by the Kg. A weighing operation is needed before invoicing the customer.

To activate the management options for double units of measure, assign the group *Useability / Product UoS View* to your user.

In this case the same product can be expressed in two units of measure belonging to different categories. You can then distinguish between the unit of stock management (the piece) and the unit of invoicing or sale (kg).

In the product form you can then set one unit of measure for sales and stock management, and one unit of measure for purchases. 

These units are given suggested titles. For each operation on a product you can use another unit of measure, as long as it can be found in the same category as the two units already defined. If you use another unit of measure, Open ERP automatically handles the conversion of prices and quantities.

So if you have 430 Kg of carottes at 5.30 EUR/Kg, Open ERP will automatically make the conversion if you want to sell in tonnes – 0.43 tonnes at 5300 EUR / tonne. If you had set a rounding factor of 0.1 for the *tonne* unit of measure then Open ERP will tell you that you have only 0.4 tonnes available.


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
