Logistics and Stock Management
###############################

*Open ERP's stock management is at once very simple, flexible and complete. It's based on the concept of double entry that revolutionized accounting. The system can be described by Lavoisier's maxim “nothing lost, everything changed” or, better, “everything moved”. In Open ERP you don't talk of disappearance, consumption or loss of products: instead you talk only of stock moves from one place to another.*

Just as in accounting, the Open ERP system manages counterparts to each of its operations such as receipts from suppliers, deliveries to customers, profits and losses from inventory, and consumption of raw materials. Stock movements are always made from one location to another. To satisfy the need for a counterpart to each stock movement, the software supports different types of stock location:

* Physical stock locations,

* Partner locations,

* Virtual counterparts such as production and inventory.

Physical locations represent warehouses and their hierarchical structure. These are generally the locations that are managed by traditional stock management systems.

Partner locations represent your customers' and suppliers' stocks. To reconcile them with your accounts, these stores play the role of third-party accounts. Reception from a supplier can be shown by the movement of goods from a partner location to a physical location in your own company. As you see, supplier locations usually show negative stocks and customer locations usually show positive stocks.

Virtual counterparts for production are used in manufacturing operations. Manufacturing is characterized by the consumption of raw materials and the production of finished products. Virtual locations are used for the counterparts of these two operations.

Inventory locations are counterparts of the stock operations that represent your company's profits and losses in terms of your stocks.

The following figure shows the initial configuration of the stores locations when the software is installed.

.. image:: images/stock_location_tree.png
    :align: center

*Stores location structure when Open ERP has just been installed.*

.. tip::   **More information**  *Hierarchical stock locations*

    In Open ERP locations are structured hierarchically. You can structure your locations as a tree, dependent on a father-son relationship. This lets you have more detailed levels of analysis of your stock operations and the organization of your warehouses.

.. tip:: **Terminology** *Locations and Warehouses*

    In Open ERP warehouses represent your places of physical stock. A warehouse can be structured in several locations at multiple levels. Locations are used to manage all types of storage place, such as at the customer and the production counterparts.


.. raw:: html

    <div class="all-toctree">

.. toctree::

    5_12_stock_management_illustration
    5_12_stock_management_wf
    5_12_stock_management_stocks
    5_12_stock_management_logistic
    5_12_stock_management_import
    5_12_stock_management_warehouses
    5_12_stock_management_production.rst
    5_12_stock_management_lots.rst
    5_12_stock_management_journals.rst
    5_12_stock_management_advanced.rst

.. raw:: html

    </div>

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
    