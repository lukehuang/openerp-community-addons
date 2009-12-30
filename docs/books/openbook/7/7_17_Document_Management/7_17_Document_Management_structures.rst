
Standardizing Structures
-------------------------

You now have a configuration that enables you to automatically get a directory structure linke to Open ERP for each resource, such as for projects and orders. The ideal situation would now be to automatically structure the documents about projects, say. For example, you could classify them depending on their type:

* Quotations,

* Meeting Minutes,

* Delivery Documents,

* Documentation.

Open ERP provides you with a system that lets you create a structure type for each type of a given document. It then provides that classification for all documents in the directories structured in that type.

So create the structure above for your project management system. To do that, create the four directories above and give them the following data:

* **Type** : Static Directory

* **Linked Model** : Analytic Account

Then in each project (represented by analytic accounts) you'll get this substructure for organization your documents efficiently.

.. image::  images/document_shared_structure.png
    :align: center

*Substructure common to all projects.*

.. tip::   **Technique**  *Mapping* 

    In practice, Open Erp doesn't create directories or files for every resource. It actually manages this by mapping between Open ERP resources and the FTP interface

    This approach gives a lot of flexibility because there's no synchronization to do, nor redundancy. Changes in either the document management system or in Open ERP will automatically be reflected over in the other side.

    And at the same time, resources are obviously not used up by storing things twice.

Once a new project has been defined in Open ERP, the system automatically creates a directory corresponding to the project in the right place in the document management system, and creates a structure type there for classifying documents.


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
