
.. index::
   single: Chart of Accounts

Chart of Accounts
=================

On installation, the software is given a default chart of accounts that's the same regardless of your country. To install the chart of accounts and tax definitions for your own country install the module \ ``l10n_XX``\   where XX represents your country code in two letters. For example to get the chart of accounts for France install the module \ ``l10n_fr``\  . 

Some of these pre-built modules are comprehensive and accurate, others have rather more tentative status and are simply indicators of the possibilities. You can modify these, or build your own accounts onto the default chart, or replace it entirely with a custom chart.

You view active charts of accounts using the menu  *Financial Management > Charts > Charts of Accounts* .

.. tip::   **Advantage**  *Hierarchical charts* 

	Most accounting software packages represent their charts of accounts in the form of a list. You can do this in Open ERP as well if you want to, but its tree view offers several advantages:

	* it lets you show and calculate only the accounts that interest you,

	* it enables you to get a global view of accounts (when you show only summary accounts)

	* it simplifies searches semantically

	* it's more intuitive, because you can search for accounts on the basis of their classification

	* it's flexible because you can easily restructure them.

The structure of the chart of accounts is hierarchical, with account subtotals called account views. You can develop a set of account views to contain only those elements that interest you.

To get the detail of the account entries that are important to you, all you need to do is click the account. You can also click the  *Print*  icon after selecting one or several accounts (do a  *Ctrl-click*  on each line you want to select). The software gives you a choice of at least two reports: print the ledger or the balance of the selected accounts.

Displaying the chart of accounts can take several seconds because Open ERP calculates the debits, credits and balance for each account in real time. If you just want to work with a chart of accounts that has structure but shows no totals, use the function  *Financial Management > Charts > Charts of Accounts > Fast Charts of Accounts* .

Creating a chart of accounts
----------------------------

.. image::  images/account_form.png
	:align: center

*Definition of an account.*

To add, modify or delete existing accounts, use the menu  *Financial Management > Configuration > General Accounts > Accounts Definitions* .

.. index::
   single: Multi-lingual

.. tip::   **Advantage**  *Multi-lingual fields* 

	In Open ERP multi-lingual fields are marked by a small flag to their right. Click on the flag to get a translation of the value of the field in the different installed languages. You can also edit the translation.

	This enables you to efficiently manage other languages as you need them The field's value appears in the language of the logged-in user or, in the case of reports printed for a partner, that of the partner.

The main account fields are:

*  *Name* : the name of the account is a multi-lingual field, which is why there's a little flag to the right. Give the field a name.

*  *Active* : if you deactivate an account (by unchecking the box) it will no longer be visible in the chart of accounts but can be reactivated later. Only accounts which aren't needed for account entries can be deactivated.

*  *Account Type* : account types determine an account's use in each journal. By default the following types are available: \ ``View``\  , \ ``Receivable``\  , \ ``Payable``\  , \ ``Income``\  , \ ``Expense``\  , \ ``Tax``\  , \ ``Cash``\   *, * \ ``Asset``\  , \ ``Equity``\  . You can add new types through the menu:  *Financial Management > Configuration > *  *Charts of Accounts > Type of Accounts* . Use the \ ``View``\   type for accounts that make up the structure of the charts and have no account data inputs of their own.

.. index::
   single: Type of account
   single: Account Type

.. tip::   **Comment**  *Type of account* 

	The account types are mainly used as an informative title, The only two types that have any particular effect are Receivables and Payables.

	These two types are used by reports on partner credits and debits. They're calculated from the list of unreconciled entries in the accounts of one of these two types.

*  *Account Number* : the code isn't limited in number of digits. Use code 0 for all root accounts.

*  *Currency* : the default currency for that account.

*  *Deferral Method* : determines how to treat the account and its entries at the closing of the books at the end of the year. Four methods are available:

	- Balance: an entry is generated for the account balance and carried across to the new year (generally used for bank accounts),

	- None: no accounting entries are transferred across to the new financial year (generally for classes 6 and 7),

	- Detail: all entries are kept for the new fiscal year,

	- Unreconciled: only unreconciled entries are carried over to the new fiscal year (usually used for third-party accounts).

*  *Reconcile* : determines if you can reconcile the entries in this account. Activate this field for partner accounts and for chequing (checking) accounts.

*  *Parents* : determines which account is the parent of this one, to create the tree structure of the chart of accounts.

*  *Default Taxes* : this is the default tax applied to purchases or sales using this account. It enables the system to generate tax entries automatically when entering data in a journal manually.

The tree structure of the accounts can be altered as often and as much as you wish without recalculating any of the individual entries. So you can easily restructure your account during the year to reflect the reality of the company better.

.. index:: Consolidation (Accounting)
.. index:: Virtual (Chart of Accounts)

Using virtual charts of accounts
--------------------------------

The structure of a chart of accounts is imposed by the legislation in effect in the country of concern. Unfortunately that structure doesn't always correspond to the view that a company's CEO needs.

In Open ERP you can use the concept of virtual charts of accounts to manage several different representations of the same accounts simultaneously. These representations can be shown in real time with no additional data entry.

So your general chart of accounts can be the one imposed by the statutes of your country, and your CEO can then have other virtual charts as necessary, based on the accounts in the general chart. For example the CEO can create a view per department, a cash-flow and liquidity view, or consolidated accounts for different companies.

The most interesting thing about virtual charts of accounts is that they can be used in the same way as the default chart of accounts for the whole organization. For example you can establish budgets from your consolidated accounts or from the accounts from one of your companies.


.. index::
   single: Virtual Accounts

.. tip::   **Advantage**  *Virtual accounts* 

	Virtual accounts enable you to provide different representations of one or several existing charts of accounts. Creating and restructuring virtual accounts has no impact on the accounting entries. You can then use the virtual charts with no risk of altering the general chart of accounts or future accounting entries.

	Because they're used only to get different representation of the same entries they're very useful for:

	* consolidating several companies in real time,

	* depreciation calculations,

	* cash-flow views,

	* getting more useful views than those imposed by statute,

	* presenting summary charts to other users that are appropriate to their general system rights.

	So there are good reasons for viewing the execution of financial transactions through virtual charts, such as budgets and financial indicators based on special views of the company.

To create a new chart of accounts you should create a root account using the menu  *Financial Management > Configuration > General Accounts > Accounts Definition* . Your top level account should have  *Code* \ ``0``\   and  *Type* \ ``View``\  . Then you can choose your structure by creating other accounts of  *Type* \ ``View``\   as necessary. Check your virtual structure using the menu  *Financial Management > Charts > Charts of Accounts* .

Finally, when you've got your structure, you must make the general accounts and virtual accounts match. For that search the general accounts and ensure that each non-\ ``View``\   account there also has a virtual account in the field  *Parents* .

You can then check through your general chart of accounts as well as your virtual charts which give you another representation of the company. All the actions and states in your general account are also available in the virtual accounts.

Finally you can also make virtual charts of accounts from other virtual charts. That can give an additional dimension for financial analysis.

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
