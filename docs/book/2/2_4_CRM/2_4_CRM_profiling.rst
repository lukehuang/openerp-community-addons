.. index::
   single: Profiling
.. 

Profiling
===========

.. index:: Prospect
.. index:: Profiling

Establishing the profiles of prospects
---------------------------------------

During presales activities it's useful to qualify your prospects quickly. You can pose a series of questions to find out what product to offer to the customer, or how quickly you should handle the request. 

.. tip::   **Method**  *Profiling* 

	This method of rapidly qualifying prospects is often used by companies who carry out presales by phone. A prospect list is imported into the Open ERP system as a set of partners and the operators then pose a series of questions to each prospect by phone.

	Responses to these questions enable each prospect to be qualified automatically which leads to a specific service being offered based on their responses

As an illustration, take the case of the Tiny company which offers a service based on the Open ERP software. The company goes to several exhibitions and encounters dozens of prospects over a few days. It's important to handle each request quickly and efficiently.

The products offered by Tiny at these exhibitions are:

* training on Open ERP – for independent people or small companies,

* partner contract – for IT companies that intend to offer an Open ERP service,

* Open ERP as SaaS – for small companies,

* a meeting in conjunction with a partner to provide a demonstration aimed at providing a software integration – for companies that are slightly larger.

The Tiny company has therefore put a decision tree in place based on the answers to several questions posed to prospects. These are given in the following figure:


.. image::  images/crm_profile_tree.png
   	:align: center

*Example of profiling customer prospects by the Tiny company*


The sales person starts by asking the questions mentioned above and then with a couple of minutes of work can decide what to propose to the prospective customer.

At the end of the exhibition prospects' details and their responses to the questionnaire are entered into Open ERP. The profiling system automatically classifies the prospects into appropriate partner categories.

This enables your sales people to follow prospects up efficiently and adapt their approach based on each prospect's profile. For example, they can send a letter based on a template developed for a specific partner category. They'd use Open ERP's report editor and generator for their sales proposition, such as an invitation to a training session a week after the show.

Using profiles effectively
---------------------------

To use the profiling system you'll need to install Open ERP's \ ``crm_profiling``\   module. It's part of the core Open ERP system in version 5.0.0 so you don't have to download it separately from ``addons-extra``.

Once the module is installed you can create a list of questions and the possible responses through the menu  *CRM & SRM > Configuration > Segmentation > Questions* .

To obtain the scheme presented earlier you can create the following questions and responses:


.. csv-table::  **Questionnaire for defining profiles**
   :header: "Questions","Possible Responses"
   :widths: 20, 30
   
   "Journalist ?","Yes / No"
   "Industry Sector ?","IT / ERP Consultant / Services / Industry / Others"
   "Number of Staff ?","1 / 2-20 / 21-50 / 51-100 / 101-500 / 500+"
   "Contact's job function ?","Decision-maker / Not decision-maker"
   "Already created a specification for the work ?","Yes / Soon / No"
   "Implementation budget ?","Unknown  / <100k / 101-300k / >300k"
   

For instance, a sales person specializing in large accounts for the service sector could have a profile defined like this:

* Budget for integration: \ ``Unknown``\  , \ ``100k-300k``\   or \ ``>300k``\  ,

* Already created a specification for the work? \ ``Yes``\  ,

* Industry Sector? \ ``Services``\  .

When entering the details of a specific prospect, the prospect's answers to various questions can be entered in the new fifth tab of the partner form. Open ERP will automatically assign prospects to the appropriate partner category based on these answers.

.. tip::   **A step further**  *commercial objectives* 

	The module ``report_invoice_salesman`` enables you to set up regular business targets. These can be based on sales turnover or sales margins.

	With this module you can compare the performance of each sales person with their targets for the period. Sales people can view their own performance against target in real time through a dashboard.

	This module is totally integrated with the rest of accounting so there's no need to extract any data from another system to get the sales figures against objectives by sales person or sector – it's just available all the time in real time.

Customers corresponding to a specific search profile can be treated as a priority. The sales person can access the profile of the large active accounts from the menu  *Partners > Partners by category* .


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

