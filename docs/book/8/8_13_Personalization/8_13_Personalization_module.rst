.. index::
   single: Personalizing; Module
.. 

Creating a Configuration Module
=================================

It's very helpful to be able to backup your specific configuration settings in an Open ERP module dedicated just to that. That enables you to:

* automatically duplicate the configuration settings by installing the module in another database,

* reinstall a clean database with your own configuration in case you have problems with the initial configuration,

* publish your specific configuration to benefit other companies in the same industrial sector,

* simplify migrations, if you have modified some elements of the basic configuration, there's a risk in returning them to their original state after the migration, unless you've saved the modifications in a module.

Start by installing the module \ ``base_module_record``\   in the usual way. Then start recording your actions using the menu  *Administration > Modules Management > Modules Recording > Start Recording* . Manually make all your configuration changes through the user interface as you would normally (such as menu management, dashboard assignments, screen personalization, new reports, and access rights management – details of some of these possibilities are described later in this chapter).

Once you've done all this, go to the menu  *Administration > Modules Management > Modules Recording > Save Recorded Module* . 

.. tip::   **A step further**  *Contributing to the development of Open ERP* 

	Once your personal configuration has been saved into a module, install the module ``base_module_publish``. This gives you a new possible action Publish Module in the menu Administration > Modules Manage > Modules. 

	Use this function to publish your module on the official Open ERP site. It could then be reused by other companies that have the same needs as yours. You could then yourselves benefit from improvements made by these same companies in future. 

	Don't forget to create a user account beforehand on http://openerp.com.

Open ERP then creates a ZIP file for you containing all of the modifications you made while you were carrying out your configuration work. You could reinstall this module on other databases and/or publish it online to help other companies. This could turn out to be useful if you want to install a test server for your company's users and give them the same configuration as the production server.

To install a new module saved in ZIP file form, use the menu  *Administration > Modules Management > Import a new module* .


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

