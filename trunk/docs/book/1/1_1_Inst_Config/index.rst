
Installation and Configuration 安装和配置
###############################

 *Installing Open ERP under Windows or Linux for familiarization use should take you only half an hour or so and needs only a couple of operations. The first operation is installation of the application and database server on a server PC (that's a Windows or Linux or Macintosh computer). You've a choice of approaches for the second operation: either install a web server (most probably on the original server PC) to use with standard web clients that can be found on anybody's PC, or install application clients on each intended user's PC. When you first install Open ERP you'll configure a database containing a little functionality and some demonstration data to test the installation.* 

 *为了熟悉使用OpenERP，你只需要花半个小时左右的时间和有限的操作来将其安装在Windows或者Linux下。第一步是在服务器(Windows Linux Macintosh均可)上安装数据库和应用程序。第二步，你可以任选其一：安装网络服务器（通常和应用服务器在同一台主机上）来使用任意一台电脑上标准网络浏览器进行操作，或者在每一台客户终端PC上安装客户端应用程序。当你第一次安装OpenERP后，你需要为数据库配置功能并且安装一些演示数据来测试安装结果。*


	.. image:: images/ch1_outline.png
		:align: center

*Your options for reading this section of the book. 你阅读本书的顺序方案*

This chapter focuses on the installation of Open ERP so that you can begin to familiarize yourselves with its use. If you're not a systems administrator, or if you've already installed Open ERP, or if you're planning to use an online SaaS provider, then you can skip this chapter and move straight to Chapter 2. If you've already used Open ERP (or Tiny ERP) a bit then you can move past that to Chapter 3 in this section of the book.

本章重点在于OpenERP的安装，因此你可以借此机会开始熟悉使用OpenERP。如果你不是一个系统管理员，或者你已经成功安装了OpenERP，或者你打算使用OpenERP的在线服务，那么你可以跳过这一章，直接到第2章。如果你已经使用了OpenERP（也许是TinyERP），那么你可以直接去本部分的第3章。

.. index::
   single: Tiny ERP

.. tip::   **Reminder注意**  *Renaming from Tiny ERP to Open ERP 从TinyERP 到 OpenERP* 


	Tiny ERP was renamed to Open ERP early in 2008 so somebody who's already used Tiny ERP should be equally at home with Open ERP. The two names refer to the same software, so there's no functional difference between versions 4.2.X of Open ERP and 4.2.X of Tiny ERP. This book applies to versions of Open ERP from 5.0.0 onwards, with references to earlier versions from time to time. 

        2008年，我们将TinyERP更名为OpenERP，因此那些使用TinyERP的用户就是OpenERP的用户。二者指的是同一款软件，同一版本的TinyERP和OpenERP没有任何差别。本书适用于OpenERP 5.0.0及以上版本，有时也会参照旧版本。

.. index::
   single:SaaS
..

.. tip::   **Advice 建议**  *The SaaS, or “on-demand”, offer 软件即服务，按需定制，设备供应* 


	SaaS (Software as a Service) is delivered by a hosting supplier and paid in the form of a monthly subscription that includes hardware (servers), system maintenance, provision of hosting services, and support.

        SaaS(软件即服务)是由主机供应商提供服务，并按月收取费用，包括硬件（服务器）、系统维护、主机服务、技术支持。

	You can get a month's free trial on Tiny's http://ondemand.openerp.com, which enables you to get started quickly without incurring costs for integration or for buying computer systems. Many of Tiny's partner companies will access this, and some may offer their own similar service.

        在 http://ondemand.openerp.com ，你可以获得一个月的免费试用，你可以在不花费资金进行系统集成或购买硬件的情况下快速开始使用OpenERP。许多Tiny的合作者趋向于此，有些人可能提供他们自己的类似服务。

	This service should be particularly useful to small companies that just want to get going quickly and at low cost. It gives them immediate access to an integrated management system that's been built on the type of enterprise architecture used in banks and other large organizations. Open ERP is that system, and is described in detail throughout this book.

        这种服务对于那些希望尽快实施企业信息化又非常在乎成本的小企业来说是非常有益的。SaaS使得在银行等大型集团应用的企业级集成化管理系统对这些小公司来说触手可及了。OpenERP就是这样一套系统，本书将对其进行详尽的阐述。

Whether you want to test Open ERP or to put it into full production, you have at least two starting points:

无论你是试用OpenERP还是将其投入实际应用，你必须先做两件事情：

* evaluate it on line at http://openerp.com and ask Tiny for an SaaS trial hosted at http://ondemand.openerp.com, or the equivalent service at any of Tiny's partner companies,

* 登陆 http://openerp.com 进行升级，并且登陆 http://ondemand.openerp.com 请求Tiny提供SaaS服务进行试用，或者通过Tiny的合作公司获得类似的服务。

* install it on your own computers to test it in your company's systems environment.

* 在你公司的系统环境中安装OpenERP进行测试。

There are some differences between installing Open ERP on Windows and on Linux systems, but once installed, it gives the same functions from both so you won't generally be able to tell which type of server you're using.

在安装OpenERP的过程中，Windows和Linux会有所不同，但只要安装成功了，二者提供的功能是完全相同的，你不需要关心服务器的运行平台。

.. tip::   **Alternative**  *Linux, Windows, Mac* 

	Although this book deals only with installation on Windows and Linux systems, the same versions are also available for the Macintosh on the official website of Open ERP.

.. tip::   **URL**  *Web sites for Open ERP* 

	* Main Site: http://openerp.com,

	* SaaS or “on-demand” Site: http://ondemand.openerp.com,

	* Community discussion forum where you can often receive informed assistance: http://openobject.com/forum.

.. tip::   **Note**  *Current documentation* 

	The procedure for installing Open ERP and its web server are sure to change and improve with each new version, so you should always check each release's documentation – both packaged with the release and on the website – for exact installation procedures.

Once you've completed this installation, you'll create and configure a database to confirm that your Open ERP installation is working.

一旦您完成OpenERP的安装，您将创建和配置一个数据库，以确认您的OpenERP系统成功安装。


.. raw:: html

    <div class="all-toctree">

.. toctree::

   1_1_Inst_Config_architecture   
   1_1_Inst_Config_install
   1_1_Inst_Config_db_create   

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

