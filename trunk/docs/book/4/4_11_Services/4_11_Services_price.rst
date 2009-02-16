
.. index::
   single: Refund

Price management policies
===========================

Some companies are notorious for their complicated pricelists. Many forms of price variation are used, such as end-of-year refunds, discounts, changes of terms and conditions with time, various prepayments, cascaded rebates, seasonal promotions, and progressive price reductions.

.. tip::   *Terminology* 

	In some accounting jurisdictions you have to differentiate between the three following terms:

	* Rebate: reimbursement to the client, usually at the end of the year, that depends on the quantity of goods purchased over a period.

	* Refund: reduction on the order line or invoice line if a certain quantity of goods is purchased at one time or is sold in a framework of a promotional activity.

	* Reduction: A one-off reduction resulting from a quality defect or a variation in a product's conformance to a specification.

Intelligent price management is difficult, because it requires you to integrate several conditions from clients and suppliers to create estimates quickly or to invoice automatically. But if you have an efficient price management mechanism you can often keep margins raised and respond quickly to changes in market conditions. A good price management system gives you scope for varying any and all of the relevant factors when you're negotiating a contract.

To help you work most effectively, Open ERP's pricelist principles are extremely powerful yet are based on simple and generic rules. You can develop both sales pricelists and purchase pricelists for products capable of accommodating conditions such as the date period, the quantity requested and the type of product.

.. tip::   **Don't Confuse**  *The different prices* 

	It's important not to confuse the sale price and the base price of a product. In the basic configuration of Open ERP the sale price is made equal to the base price marked on the product file but you can vary the sale price in response to other customer conditions.

	It's the same for purchase price and standard cost. Purchase price is your suppliers' selling price, which changes in response to different criteria such as quantities, dates, and supplier. This is automatically set by the accounting system. You'll find that the two prices have been set to the same for all products by default with the demonstration data, which can be a source of confusion since you're free to set the standard cost to something different.

Each pricelist is calculated from defined policies, so you'll have as many sales pricelists as active sales policies in the company. For example a company that sells products through three sales channels could create the following price lists:

	#. Main distribution:

	- pricelist for Walbury,

	- pricelist for TesMart,

	#. Postal Sales.

	#. Walk-in customers.


A single pricelist can exist in several versions, only one of which is permitted to be active at a given time. These versions let you set different prices at different points in time. So the pricelist for walk-in customers could have five different versions, for example: \ ``Autumn``\,  \ ``Summer``\, \ ``Summer Sales``\, \ ``Winter``\, \ ``Spring``\. Direct customers will see prices that change with the seasons.   

Each pricelist is expressed in a single currency. If your company sells products in several currencies you'll have to create as many pricelists as you have currencies.

The prices on a pricelist can depend on another list, which means that you don't have to repeat the definition of all conditions for each product. So a pricelist in USD can be based on a pricelist in EUR. If the currency conversion rates between EUR and USD change, or the EUR prices change, the USD rates can be automatically adjusted.

.. index::
   single: Pricelists; Create
.. 

Creating pricelists
---------------------

To define a pricelist use the menu  *Products > Pricelists > Pricelists* .

For each list you have to define:

* a  *Name*  for the list,

* a  *Type*  of list: \ ``Sale``\   for customers or \ ``Purchase``\   for suppliers,

* the  *Currency*  in which the prices are expressed.

.. tip::   **Terminology**  *Consumer Price* 

	If you install the module edi a third type of list appears – the Consumer Price, which defines the price displayed for the end user. This doesn't have to match your selling price to an intermediary or distributor.

.. index::
   single: Pricelists; versions
.. 

Pricelist versions
^^^^^^^^^^^^^^^^^^^

Once the list is defined you must provide it with at least one version. To do that use the menu  *Products > Pricelists > Pricelist Versions* . The version contains all of the rules that enable you to calculate a price for a product and a given quantity.

So set the  *Name*  of this associated version. If the list only has a single version you can use the same name for the pricelist and the version. In the  *Pricelist*  field select the pricelist you created.

Then indicate the  *Start date*  and  *End date*  of this version. The fields are both optional: if you don't set any dates the version will be permanently active. Use the  *Active*  field in the versions to activate or disable a pricelist version.

.. tip::   **Note**  **  *Automatically updating the sale pricelist* 

	It's possible to make any sale pricelist depend on one of the other pricelists. So you can decide to make your sale pricelist depend on your supplier's purchase pricelist, to which you add a margin. The prices are automatically calculated as a function of the purchase price and need no further manual adjustment.


.. index:: Price

Rules for calculating price
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A pricelist version is made up of a set of rules that apply to the product base prices.


	.. image::  images/service_pricelist_line.png
	   :align: center

*Detail of a rules in a pricelist version*

You define the conditions for a rule in the first part of the definition screen labeled  *Rules Test Match* . The rule applies to the  *Product*  or  *Product Template*  and/or the named  *Product Category* . If a rule is applied to a category then it is automatically applied to all of its subcategories too (using the tree structure for product categories).

If you set a minimum quantity in  *Min. Quantity*  the rule will only apply to a quantity the same as or larger than that indicated. This lets you set reduced rates in stages that depend on ordered quantities.

Several rules can be applied to an order. Open ERP evaluates these rules in sequence to select which to apply to the specified price calculation. If several rules are valid only the first in sequence is used for the calculation. The  *Sequence*  field determines the order, starting with the lowest number.

Once a rule has been selected, the system has to determine how to calculate the price from the rule. This operation is based on the criteria set out in the lower part of the form, labeled  *Price Computation* .

The first field you have to complete is labeled  *Based on* . You must indicate the mode of calculating the partner price. You have the choice between:

* the \ ``List Price set``\   in the product file,

* the \ ``Standard Cost set``\   in the product file,

* an \ ``Other Pricelist``\   given in the field  *If Other Pricelist* ,

* the price that varies as a function of a supplier defined in the \ ``Partner section of the product form``\  .

Several other criteria can be considered and added to the list, as you'll see in the following section.

Next, various operations can be applied to the base price to calculate the sales or purchase price for the partner at the specified quantities. To calculate it you apply the formula shown on the form:

Price = Base Price x (1 – Field1) + Field2

 *Field1* \ ``0.20``\  \ ``-0.15``\  

 *Field2*  *Field1* 

 *Rounding Method* \ ``0.05``\  \ ``45.66``\  \ ``45.65``\  \ ``14,567``\  \ ``100``\  \ ``14,600``\  

.. tip::   **Attention**  *Swiss special situation* 

	In Switzerland, the smallest monetary unit is 5 cents. There aren't any 1 or 2 cent coins. So you set Open ERP's rounding to 0.05 to round everything in a Swiss franc pricelist.

 *Field2* \ ``9.99``\  \ ``10``\  \ ``-0.01``\   *Field2* 

 *Min. Margin*  *Max. Margin* \ ``10``\  \ ``10``\  \ ``0``\  

Once the pricelist is defined you can assign it to a partner. To do this, find a Partner and select its  *Properties*  tab. You can then change the  *Purchase Pricelist*  and the  *Sale Pricelist*  that's loaded by default for the partner.

.. index::
   single: Pricelists; Default pricelists
.. 

Default pricelists
^^^^^^^^^^^^^^^^^^^


	.. image::  images/product_pricelist_default.png
	   :align: center

*Default pricelists after the installation of Open ERP*

When you install the software two pricelists are created by default: one for sales and one for purchase. These each contain only one pricelist version and only one line in that version.

 *List Price* 

The price for purchases that's defined in the Default Purchase Pricelist is set in the same way by the Standard Cost of the product in the product file.

Case of using pricelists
-------------------------

Let's take the case of an IT systems trading company, for whom the following product categories have been configured:

All products

	#. Accessories

                * Printers

                * Scanners

                * Keyboards and Mice

	#. Computers

                * Portables

	                - Large-screen portables

                * Computers

	                - Office Computers

	                - Professional Computers



In addition, the products presented in the table below are defined in the currency of the installed chart of accounts.

  **Examples of products with their different prices**

TABLE

.. csv-table::

   "Product ","List Price","Standard Price","Default supplier price",
   "Acclo Portable","1 200 ","887 ","893 ",
   "Toshibishi Portable","1 340 ","920 ","920 ",
   "Berrel Keyboard","100 ","50 ","50 ",
   "Office Computer","1 400 ","1 000 ","1 000 ",

.. index::
   single: List price
.. 

Defining the list price
^^^^^^^^^^^^^^^^^^^^^^^^^

Now define the sale price for resellers like this:

* For portable computers, the sale price is calculated from the list price of the supplier Acclo, with a supplement of 23% on the cost of purchase.

* For all other products the sale price is given by the standard cost in the product file, on which 31% is added. The price must end in “.99”.

* The sale price of Berrel keyboards is fixed at 60 for a minimum quantity of 5 keyboards purchased. Otherwise it uses the rule above.

Assume that the Acclo pricelist is defined in Open ERP. The pricelist for resellers and the pricelist version then contains three lines:

	#. \ ``Acclo``\  line:

                *  *Product Category* : \ ``Portables``\  ,

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Acclo pricelist``\  ,

                *  *Field1* : \ ``-0.23``\  ,

                *  *Sequence* : \ ``1``\  .

	#. \ ``Berrel Keyboard``\  line:

                *  *Product Template* : \ ``Berrel Keyboard``\  ,

                *  *Min. Quantity* : \ ``5``\  ,

                *  *Field1* : \ ``1.0``\  ,

                *  *Field2* : \ ``60``\  ,

                * Sequence: \ ``2``\  .

	#. \ ``Other products``\  line:

                *  *Based on:* \ ``Standard Price``\  ,

                *  *Field1* : \ ``-0.31``\  ,

                *  *Field2* : \ ``-0.01``\  ,

                *  *Sequence* : \ ``3``\  .

                 *Sequence* 

Also note that to fix a price of 60 for the 5 Berrel Keyboards, the formula \ ``Price = Base Price x (1 – 1.0) + 60``\   has been used.

Establishing customer contract conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The trading company can now set specific conditions to a customer, such as the company TinAtwo, who might have signed a valid contract with the following conditions:

* For Toshibishi portables, TinAtwo benefits from a discount of 5% of resale price.

* For all other products, the resale conditions are unchanged.

The list price for TinAtwo, called “TinAtwo contract”, contains two rules:

	#. \ ``Toshibishi portable``\  line:

                *  *Product* : \ ``Toshibishi Portable``\  ,

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Reseller pricelist``\  ,

                *  *Field1* : \ ``0.05``\  ,

                *  *Sequence* : \ ``1``\  .

	#. \ ``Other Products``\  

                *  *Product:*

                *  *Based on* : \ ``Other pricelist``\  ,

                *  *Pricelist if other* : \ ``Reseller pricelist``\  ,

                *  *Sequence* : \ ``2``\  .

                \ ``TinAtwo``\   *Properties*  *Sale Pricelist* \ ``TinAtwo Contract``\   *Start date*  *End date* 

Then when salespeople prepare an estimate for TinAtwo prices proposed will automatically be calculated from the contract conditions.

Other bases of price calculation
---------------------------------

Open ERP provides a way of making prices depend on any field of the product form, not just the two predefined fields: \ ``List Price``\   and \ ``Cost Price``\  .

To do this, use the menu  *Products > Configuration > Price Types* . Then create a new entry corresponding to a new type of price. Enter the name of the field (for example: \ ``Public Price``\  ) and the the product field that it corresponds to ( *Public Price* ) and the currency that it's expressed in. New fields are added to the product file so that they can be used in calculations.

Once you've done this you can make a dependency on the new type of price in the pricelist.

 *Weight*  *Volume* 

.. index::
   single: Multi-currency

Managing the price in several currencies
-----------------------------------------

Since each pricelist is defined in a single currency you must create separate pricelists for the other currencies that you sell in. So, if your trading company wants to start a product catalog in a new currency, you have several possibilities:

* Code the price in a new independent pricelist and maintain the lists in the two currencies separately.

* Create a field in the product form for the new currency and make the pricelist depend on the new field: the prices are then maintained separately, but in the product file.

Create a new pricelist for the second currency and make this list depend either on another pricelist or on a product price: the conversion between currencies will be done automatically at the latest rates. This solution is generally the most flexible and the simplest to maintain as prices change with time.


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

