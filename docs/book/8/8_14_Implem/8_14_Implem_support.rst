
.. index::
   single: Maintenance
   single: Support

Support and maintenance
=========================

It's when you actually use your ERP that you will obtain value from your investment. For that reason maintenance and support are critical for your long term success.

* Support aims to ensure that end users get the maximum productivity from their use of Open ERP by responding to their questions on the use of the system. Support can be technical or functional.

* Maintenance aims to ensure that the system itself continues to function as required. It includes system upgrades, which give you access to the latest functionality available.

Some partners offer preventative maintenance. This makes sure that all the specific developments for your system are revised and tested for each new version so that they remain compatible with the base Open ERP.

If you haven't anticipated your needs with a preventive maintenance contract, the costs of migration after a few years can become significant. If special modules that you developed have been allowed to become too old you may eventually need a new development to your specifications.

Updates and Upgrades
---------------------

There are four sources of code change for Open ERP:

* patches supplied by Tiny to correct faults: after validation these patches won't cause any secondary effects,

* minor updates, which gather the fault corrections together in one package, and are generally announced with a modification of the version number, such as from 5.0.0 to 5.0.1,

* upgrades, which bundle both the fault corrections and the improvements to the functionality in a major release such as from 5.0.3 to 5.2.0.

* new functions generally released in the form of new modules.

You should establish a procedure with your supplier to define how to respond to changes in the Open ERP code.

For simple updates your maintenance team will evaluate the patches to determine if they are beneficial to the use of your Open ERP. These patches should be tested on an offline instance of Open ERP before being installed in your live production version.

The maintenance team would also take charge of regular updates to the software.

Patches and updates can only be installed if you have the necessary access to the Open ERP server. You must first install the patch or update and then restart the server using the command line: \ ``–update=all``\  .

Once Tiny has released a new upgraded version your response should be a cautious one. If you're perfectly satisfied with the existing system it would be best to not touch the new version. If you want to have access to the new functionality supplied by an upgraded version, you have a delicate operation to carry out. Most upgrades require your data to be migrated because the databases before and after the upgrade can be a little different.

Version Migration
-------------------

Open ERP has a system to manage migrations automatically. To update specific modules, or the whole database, you only need to start the server with the argument:–\ ``update=NAME_OF_MODULE``\   or \ ``–update=all``\  ..

New stable versions of Open ERP sometimes require operations that aren't provided in the automated migration. Tiny, the creator and maintainer of Open ERP, has a policy of supporting migration from all official stable releases to the latest. Scripts are provided for each new release of a stable version. These carry out the upgrade from the previous major version to the new major version.

The managers responsible for the migration between two versions of Open ERP will find the documentation and the necessary scripts in the directory \ ``doc/migrate``\   of the Open ERP server.

The procedure for migrating runs like this:

	#. Make a backup of the database from the old version of Open ERP

	#. Stop the server running the old version

	#. Start the script called \ ``pre.py``\  for the versions you're moving between.

	#. Start the new version of the server using the option –\ ``update=all``\  

	#. Stop the server running the new version.

	#. Start the script called post.py for the versions you're moving between.

	#. Start the new version of the server and test it.

A migration is never an easy process. It may be that your system doesn't function as it did before or that something requires new developments in the functionality of the modules that have already been installed. So you should only move to a new version if you have a real need and should engage a competent partner to help if the version that you use differs greatly from the basic version of Open ERP.

Similarly you should take care that this migration does not correct any setting that was done incorrectly. It's can be the case, for example, that the main menu structure has been modified without recording it. You may find that you're making the wrong assumptions about that structure when loading data in that was recorded with the Module Recorder.


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

