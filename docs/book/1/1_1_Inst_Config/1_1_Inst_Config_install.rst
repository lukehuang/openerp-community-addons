
The installation of Open ERP OpenERP的安装
"""""""""""""""""""""""""""""

Whether you're from a small company investigating how Open ERP works, or on the IT staff of a larger organization and have been asked to assess Open ERP's capabilities, your first requirement is to install it or to find a working installation.

无论你是从一家小公司来研究OpenERP的工作方式，还是作为大集团的IT员工来调查OpenERP的实用性，你首先要做的就是安装工作。

The table below summarizes the various installation methods that will be described in the following sections.

下表总结了各种安装方法，它们将在余下的章节中进行详述。




 .. csv-table:: Comparison of the different methods of installation on Windows or Linux.
   :header: "Method","Average Time","Level of Complexity","Notes"
   :widths: 20, 15, 15,30

   "All-in-one Windows Installer","A few minutes","Simple","Very useful for quick evaluations because it installs all of the components pre-configured on one computer (using the GTK client)."
   "Independent installation on Windows","Half an hour","Medium","Enables you to install the components on different computers. Can be put into production use."
   "Ubuntu Linux packages","A few minutes","Simple","Simple and quick but the Ubuntu packages aren't always up to date."
   "From source, for all Linux systems","More than half an hour","Medium to slightly difficult","This is the method recommended for production environments because it's easy to keep it up to date."




 .. csv-table:: 在Windows 和 Linux平台下的安装方法.
   :header: "方法","平均耗时","复杂度","注释"
   :widths: 20, 15, 15,30

   "集成化Windows安装","几分钟","简单","非常实用而且快捷，它将会把所有配置好的组件安装在同一台电脑上。（采用GTK客户端）"
   "在Windows下进行独立安装","半小时","中","可以将组件安装在不同的电脑上。可投产使用。"
   "Ubuntu Linuxb包","几分钟","简单","简单快捷，但是Ubuntu的包有时会跟不上更新。"
   "从源代码安装，适用于所有Linux","大于半小时","较难","这种方式推荐投产使用，便于跟上更新。"
   
   
   

Each time a new release of Open ERP is made, Tiny supplies a complete Windows auto-installer for it. This contains all of the components you need – the PostgreSQL database server, the Open ERP application server and the GTK application client.

每次OpenERP有新版本发行时，Tiny公司都会提供一套Windows的自动安装程序。它包含你所需要的所有组件，包括PostgreSQL数据库服务器，OpenERP应用程序服务器和GTK客户端。

This auto-installer enables you to install the whole system in just a few mouse-clicks. The initial configuration is set up during installation, making it possible to start using it very quickly as long as you don't want to change the underlying code. It's aimed at the installation of everything on a single PC, but you can later connect GTK clients from other PCs, Macs and Linux boxes to it as well.

这套自动安装程序可以使得你在几分钟内就完成整个安装。安装过程中就会进行初始化配置，因此只要你不想改变底层代码，你可以很快开始使用OpenERP。它将把所有的组建安装在通一台计算机上，但随后你可以在其他的电脑上，可以是Macs或者Linux系列平台，来使用GTK客户端连接。


The first step is to download the Open ERP installer. At this stage you must choose which version to install – the stable version or the development version. If you're planning to put it straight into production you're strongly advised to choose the stable version.

第一步是下载OpenERP安装程序。你首先要选择要安装的版本，有稳定版和开发版。如果你想直接投入使用的话，强烈建议选择稳定版。

.. index::
   single: Stable versions

.. tip::   **Attention**  *Stable versions and development versions* 

	Open ERP development proceeds on two parallel tracks: stable versions and development versions.

	New functionality is integrated into the development branch. This branch is more advanced than the stable branch, but it can contain undiscovered and unfixed faults. A new development release is made every month or so, and Tiny have made the code repository available so you can download the very latest revisions if you want.

	The stable branch is designed for production environments. Releases of new functionality there are made only about once a year after a long period of testing and validation. Only fault fixes are released through the year on the stable branch.

.. index::
   single: Open ERP Installation; Windows (All-in-One)
.. 


To download the version of Open ERP for Windows, follow these steps:

要下载Windows的OpenERP安装包，按照以下步骤进行：

	#. Navigate to the site http://openerp.com,
           登陆 http://openerp.com 页面，

	#. Click Product on the menu at the left, then Download,
           单击左侧的 Produnct,然后单击 Download

	#. Download the demonstration version Windows installer 
	        – currently Open ERP 5.0.0 Stable Version > Windows Installers > All In One,
           下载Windows演示版安装程序
                - 当前是 Open ERP 5.0.0 Stable Version > Windows Installers > All In One,

	#. Save the file on your PC.
           将文件保存在你的电脑上

To install Open ERP and its database you must be signed in as an Administrator on your PC. Double-click the installer file and accept the default parameters on each dialog box this way:

为了安装OpenERP和它的数据库，你必须以管理员身份登陆你的计算机。按照如下步骤，双击安装文件，在每个对话框中选择默认参数：

	#. Run the installer,
           运行安装文件，

	#. Start the installation procedure by clicking  *Next* in the installation window,
           在安装窗口中点击 *Next* 来开始安装，

	#. Accept the GPL license by clicking  *I Agree*,
           点击 *I Agree* 同意GPL协议，

	#. Install Open ERP in the location in \ ``Program Files``\  hat is suggested by the installer,
           将OpenERP安装在默认的 \ ``Program Files``\ 目录下，

	#. Wait two or three minutes for the installation to complete, then click  *Next*,
           等待两三分钟后安装就可以完成，然后点击 *Next* ，

	#. Close the installation window using the middle button,  *Finish*.
           点击 *Finish* ，关闭安装窗口

The Open ERP client can then be opened, ready to use the Open ERP system. The next step consists of configuring the database, and is covered in the final section of this chapter, *Creating the database.*

随后你就可以打开OpenERP客户端准备使用。接下来的工作包是置数据库，有关操作将在本章最后一节 *建立数据库* 进行讨论。

.. index::
   single: Open ERP Installation; Windows (Independent)
.. 


Independent installation on Windows 在Windows下的独立安装
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System administrators can have very good reasons for wanting to install the various components of a Windows installation separately. For example, your company may not support the version of PostgreSQL or Python that's installed automatically, or you may already have PostgreSQL installed on the server you're using, or you may want to install the database server, application server and web server on separate hardware units. 

系统管理员们倾向于将不同的组件分开安装是很正常的事情。例如，你的公司也许不支持自动安装上的PostgreSQL或者Python的版本，或者你已经有正在使用的PostgreSQL，又或者你想把数据库服务器、应用程序服务器、web服务器安装在不同的计算机上。

For this situation you can get separate installers for the Open ERP server and client from the same location as the all-in-one auto-installer. You'll also have to download and install a suitable version of PostgreSQL independently. 

在这种情况下你可以在你获得allinone自动安装包的地方下载针对OpenERP服务器和客户端的独立安装包。你还需要下载对应版本的PostgreSQL。

You must install PostgreSQL before the Open ERP server, and you must also configure it with a user and password so that the Open ERP server can connect to it. Tiny's web-based documentation gives full and current details.

在安装OpenERP之前，你必须先安装PostgreSQL，还要为OpenERP准备一个可以连接数据库的用户。Tiny的网上文档给出了具体的步骤。

If you had previously tried to install the all-in-one version of Open ERP, you'd best uninstall that in case its embedded PostgreSQL installation interferes with your stand-alone installation.

如果之前安装了allinone的OpenERP，你最好将其卸载掉，以防止它内嵌的PostgreSQL影响你的独立安装。

Connecting users on other PCs to the Open ERP server 连接其他计算机上的OpenERP服务器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect other computers to the Open ERP server you must configure the server so that it's visible to the other PCs, and install a GTK client on each of the those PCs:

想要连接到其他计算机上的OpenERP服务器，你要对OpenERP服务器进行配置使得它对客户端是可见的，在每台客户端计算机上都要安装GTK客户端程序。

	#. Make your Open ERP server visible to other PCs by opening the Windows Firewall in the Control Panel, hen asking the firewall to make an exception of the Open ERP server. In the  *Exceptions* tab of Windows Firewall click on  *Add a program...* and choose  *Open ERP Server* in the list provided. This step enables other computers to see the Open ERP application on this server.
           通过控制面板，更改防火墙设置，使得其他电脑能够看到你的OpenERP服务器，设置防火墙将OpenERP视为例外。在 *例外* 选项卡中点击 *添加程序* ，在提供的列表中选择 *OpenERP服务器* 。这一步骤使得别的电脑可以看到本机运行的OpenERP服务器。

	#. Install the Open ERP client (\ ``openerp-client-4.X.exe``\  , which you can download in the same way as you downloaded the other Open ERP software, onto the other PCs.
           安装OpenERP客户端  （ \ ``openerp-client-4.X.exe``\ ，同样可以在你下在其他OpenERP软件的地方下载到）  

.. tip::   **Attention**  *Version matching* 

	You must make sure that the version of the client matches that of the server. The version number is given as part of the name of the downloaded file. Although it's possible that some different revisions of client and server will function together, there's no certainty about that.

To run the client installer on every other PC you'll need to have administrator rights there. The installation is automated, so you just need to guide it through its different installation steps.

想要运行客户端安装程序，你必须以管理员身份登陆。安装过程是自动的，你只需要在每一步骤按提示操作即可。

To test your installation, start by connecting through the Open ERP client on the server machine while you're still logged in as administrator. 

为了检测安装是否成功，以管理员身份登陆，运行客户端程序连接服务器进行测试。

.. tip::   **Note**  *Why signed in as a PC Administrator?* 


	You'd not usually be signed on as a PC administrator when you're just running the Open ERP client, but if there have been problems in the installation it's easier to remain as an administrator after the installation so that you can make any necessary fixes than to switch user as you alternate between roles as a tester and a software installer.

Start the GTK client on the server through the Windows Start menu there. The main client window appears, identifying the server you're connected to (which is \ ``localhost``\   – your own server PC – by default). If the message  *No database found, you must create one*  appears then you've successfully connected to an Open ERP server containing, as yet, no databases.

通过开始菜单启动GTK客户端，客户端的主窗口便显现出来，确定你要连接的服务器（默认为本机 \ ``localhost``\ ）。如果显示 *没有数据库，请新建* ，虽然还没有数据库，但你已经成功的连接到服务器了。


.. image:: images/new_login_dlg.png
	:align: center

*Dialog box on connecting a GTK client to a new Open ERP server. 连接到新OpenERP的GTK客户端对话框*

.. index::
   single: XML-RPC

.. tip::   **Note**  *Connection modes 连接模式* 

	In its default configuration, the Open ERP client connects to port 8069 on the server using the XML-RPC protocol. You can change this and connect to port 8070 using the NET-RPC protocol instead. NET-RPC is quite a bit quicker, although you may not notice that on the GTK client in normal use.

        按照默认配置，OpenERP客户端将遵循XML-RPC协议使用8069端口连接服务器。你也可以遵循NET-RPC协议使用8070端口连接服务器。NET-RPC能够稍快一些，但是在使用GTK客户端时这种优势很难被察觉到。

Resolving errors with a Windows installation
#############################################

If your system doesn't work after installing your Windows system you'll find some ideas for resolving this below:

	#. Does your PostgreSQL server work? Signed in as administrator, select  *Stop Service* from the menu  *Start > Programs > PostgreSQL*  If, after a couple of seconds, you can read  *The service PostgreSQL4OpenERP has stopped* then you can be reasonably sure that the database server was working. Restart PostgreSQL then, still in the PostgreSQL menu, start the pgAdmin III application which you can use to explore the database. Double-click on the \ ``PostgreSQL4OpenERP``\  connection as in the figure below. If the database server is working you'll be able to see some information about the empty database. If it's not then an error message will appear.

                .. image:: images/pgadmin_window.png
                	:align: center
                	:scale: 85

                *Using pgAdmin III to verify that PostgreSQL is working.*
                        

	#. Is the Open ERP application working? Signed in to the server as an administrator, stop and restart the service using  *Stop Service* and  *Start Service* from the menu  *Start > Programs > OpenERP Server*  Open the log file \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP Server``\   At the end of the file you should see the line  *The server is running, waiting for connections...* 

                .. tip::   **Note**  *Automatically starting the server* 

	                You might find that the server has not started automatically after installation. If this is the case you should restart your computer to ensure that the service is properly registered. You'll only have to do this once. Once registered the server should restart correctly every time.

	#. Is the Open ERP application server configured correctly? Signed in to the server as Administrator, open the file \ ``openerp-server.conf``\  in \ ``C:\Program Files\OpenERP Server``\  and check its content. This file is generated during installation with information derived from the database. If you see something strange it's best to entirely reinstall the server from the demonstration installer rather than try to work out what's happening.


	        .. image:: images/terp_server_conf.png
	        	:align: center
	        	:scale: 80
                   
	#. Are your client programs correctly installed? If your Open ERP GTK clients haven't started then the swiftest approach is to reinstall them.


	        .. image:: images/cmd_prompt_ping.png
	        	:align: center

	#. Can the client computers see the server computer at all? Check this by opening a command prompt window (enter \ ``cmd``\  in the window  *Start > Run...* ) and enter \ ``ping <address of server>``\  there (where \ ``<address of server>``\  represents he IP address of the server). The server should respond as shown in the following figure.

	#. Have you changed any of the server's parameters? At this point in the installation the port number of the server must be 8069 using the protocol XML-RPC.

	#. Is there anything in the server's history that can help you identify the problem? Open the file \ ``openerp-server.log``\  in \ ``C:\Program Files\OpenERP Server``\  and scan through the history for ideas. If something looks strange there, contributors to the Open ERP forums can often help identify the reason.


.. index::
   single: Open ERP Installation; Linux (Ubuntu)
.. 

Installation on Linux (Ubuntu)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section guides you through installing the Open ERP server and client on Ubuntu, one of the most popular Linux distributions. It assumes that you're using a recent release of Desktop Ubuntu with its graphical user interface on a desktop or laptop PC. 

.. tip::   **Alternative**  *Other Linux distributions* 

	Installation on other distributions of Linux is fairly similar to installation on Ubuntu. Read this section of the book so that you understand the principles, then use the online documentation and the forums for your specific needs on another distribution.

For information about installation on other distributions, visit the documentation section by following  *Product > Documentation*  on http://openerp.com. Detailed instructions are given there for different distributions and releases, and you should also check if there are more up to date instructions for the Ubuntu distribution as well.

Installation of Open ERP from packages
#######################################

At the time of writing this book, Ubuntu hadn't yet published packages for Open ERP, so this section describes the installation of version 4.2 of Tiny ERP. This is very similar to Open ERP and so can be used to test the software.

Here's a summary of the procedure:

	#. Start Synaptic Package Manager, and enter your root password as required.

	#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

	#. Search for a recent version of PostgreSQL, for example \ ``postgresql-8.3``\ then select it for installation along with its dependencies.

	#. Search for \ ``tinyerp``\  then select \ ``tinyerp-client``\  and \ ``tinyerp-server``\  for installation along with their dependencies. Click  *Update Now* to install it all.

	#. Close Synaptic Package Manager.

Installing PostgreSQL results in a database server that runs and restarts automatically when the PC is turned on. If all goes well with the tinyerp-server package then tinyerp-server will also install, and restart automatically when the PC is switched on.

Start the Tiny ERP GTK client by clicking its icon in the  *Applications*  menu, or by opening a terminal window and typing \ ``tinyerp-client``\  . The Tiny ERP login dialog box should open and show the message  *No database found you must create one!*.

Although this installation method is simple and therefore an attractive option, it's better to install Open ERP using a version downloaded from http://openerp.com. The downloaded revision is likely to be far more up to date than that available from a Linux distribution.

.. tip::   **Attention**  *Package versions* 

	Maintaining packages is a process of development, testing and publication that takes time. The releases in Open ERP (or Tiny ERP) packages are therefore not always the latest available. Check the version number from the information on the website before installing a package. If only the third figure differs (for example 5.0.1 instead of 5.0.2) then you may decide to install it because the differences may be minor – fault fixes rather than functionality changes between the package and the latest version.

Manual installation of the Open ERP server
###########################################

In this section you'll see how to install Open ERP by downloading it from the site http://openerp.com, and how to install the libraries and packages that Open ERP depends on, onto a desktop version of Ubuntu. Here's a summary of the procedure:

	#. Navigate to the page http://openerp.com with your web browser,

	#. Click  *Downloads* on the left menu,

	#. Download the client and server files from the *Sources (Linux)* section into your home directory (or some other location if you've defined a different download area).

To download the PostgreSQL database and all of the other dependencies for Open ERP from packages:

	#. Start Synaptic Package Manager, and enter the root password as required.

	#. Check that the repositories \ ``main``\   \ ``universe``\  and \ ``restricted``\  are enabled.

	#. Search for a recent version of PostgreSQL (such as \ ``postgresql-8.3``\   then select it for installation along with its dependencies.

	#. Select \ ``python-xml``\   \ ``python-libxml2``\   \ ``python-libxslt1``\   \ ``python-psycopg2``\  ``python-tz``\   \ ``python-imaging``\   \ ``python-pyparsing``\   \ ``python-reportlab``\   \ ``graphviz``\  and its dependences, \ ``python-matplotlib``\  and its ependences (some of which might already be installed), then click  *Update Now* to install them.

.. index::
   single: Python

.. tip::   **Language**  *Python* 

	Python is the programming language that's been used to develop Open ERP. It's a dynamic, non-typed language that is object-oriented, procedural and functional. It comes with numerous libraries that provide interfaces to other languages and has the great advantage that it can be learnt in only a few days. It's the language of choice for large parts of NASA's, Google's and many other enterprises' code.

	For more information on Python, explore http://www.python.org.

Once all these dependencies and the database are installed, install the server itself by following the steps below:

	#. Open a terminal window and change directory to wherever you downloaded the server source files.

	#. Decompress the file using the command \ ``tar xzf openerp-server.5.X.tar.gz``\  

	#. Change directory: \ ``cd openerp-server-5.X``\  

	#. Build the Open ERP server: \ ``python setup.py build``\  

	#. Install the Open ERP server: \ ``sudo python setup.py install``\  

Open a terminal window to start the server with the command \ ``sudo -i -u postgres openerp-server``\  , which should result in a series of log messages as the server starts up. If the server is correctly installed, the message  *[...] waiting for connections...* should show within 30 seconds or so, which indicates that the server is waiting for a client to connect to it.

.. image:: images/terps_startup_log.png
	:align: center
	:scale: 95

.. index::
  single: Client; GTK
  single: Installation; GTK clients
..

Manual installation of Open ERP GTK clients
#############################################

To install an Open ERP GTK client, follow the steps below:

	#. Install the \ ``xpdf``\  package using Ubuntu's Synaptic Package Manager.

	#. Open a terminal and change directory to wherever you downloaded the client file.

	#. Decompress the file using the command: \ ``tar xzf openerp-client.5.X.tar.gz``\  

	#. Change directory: \ ``cd openerp-client-5.X``\  

	#. Build the Open ERP client: \ ``python setup.py build``\  

	#. Install the Open ERP client: \ ``sudo python setup.py install``\  

.. tip::   **Note**  *Survey: Don't Cancel!* 

	When you start the GTK client for the first time, a dialog box appears asking for various details that are intended to help the Tiny company assess the prospective user base for its software.

	If you click the Cancel button, the window goes away – but Open ERP will ask the same questions again next time you start the client. It's best to click OK, even if you choose to enter no data, to prevent that window reappearing next time.


.. image:: images/terp_client_startup.png
	:align: center

Open a terminal window to start the client using the command openerp-client. When you start the client on the same Linux PC as the server you'll find that the default connection parameters will just work without needing any change. The message  *No database found, you must create one!*  shows you that the connection to the server has been successful and you need to create a database on the server.

Creating the database

You can connect other GTK clients over the network to your Linux server. Before you leave your server, make sure you know its network address – either by its name (such as \ ``mycomputer.mycompany.net``\  ) or its IP address (such as \ ``192.168.0.123``\  ).

.. index::
   single: Port

.. tip::   **Note**  *Different networks* 

	Communications between an Open ERP client and server are based on standard protocols. You can connect Windows clients to a Linux server, or vice versa, without problems. It's the same for Mac versions of Open ERP – you can connect Windows and Linux clients and servers to them.

To install an Open ERP client on a computer under Linux, repeat the procedure shown earlier in this section. You can connect different clients to the Open ERP server by modifying the connection parameters on each client. To do that, click the Change button on the connection dialog and set the following field as needed:

*  *Server* : \ ``name``\   or \ ``IP address``\   of the server over the network,

*  *Port* : the port, whose default is \ ``8069``\  ,

*  *Connection protocol* : \ ``XML-RPC``\  .


.. image:: images/terp_client_server.png
	:align: center
	
*Dialog box for defining connection parameters to the server.*

It's possible to connect the server to the client using a secure protocol to prevent other network users from listening in, but the installation described here is for direct unencrypted connection.

If your Linux server is protected by a firewall you'll have to provide access to port \ ``8069``\   for users on other computers with Open ERP GTK clients.

.. index::
  single: Installation; eTiny web server
..

Installation of an Open ERP web server
#######################################

Just as you installed a GTK client on a Linux server, you can also install the Open ERP web server. It's possible to install it from sources after installing its dependencies from packages as you did with the Open ERP server, but Tiny have provided a much simpler way to do this for eTiny – using a system known as ez_setup.

Before proceeding, confirm that your Open ERP installation is functioning correctly with a GTK client. If it's not you'll need to go back now and fix it, because you need to be able to use it fully for the next stages. 

To install eTiny:

	#. From Synaptic Package Manager install \ ``build-essential,``\  and then check that \ ``python-matplotlib``\  and \ ``python-imaging``\  are installed (which they should have been during the installation of the server).

	#. Now download the web framework directly to your download directory by entering: \ ``wget``\  http://www.turbogears.org/download/tgsetup.py

	#. Run the installer using: \ ``python tgsetup.py``\  

	#. Finally, install eTiny by entering the command: \ ``sudo easy_install eTiny.``\  

.. tip::   **Tool**  *Ez* 

	Ez is the packaging system used by Python. It enables the installation of programs as required just like the packages used by a Linux distribution. The software is downloaded across the network and installed on your computer by ez_install.

	ez_setup is a small program that installs ez_install automatically.

The Open ERP Web server connects to the Open ERP server in the same way as an Open ERP client using the NET-RPC protocol. Its default configuration corresponds to that of the Open ERP server you've just installed, so should connect directly at startup.

	#. At the same console as you've just been using, go to the Openerp web directory by typing \ ``cd openerp-web-5.X``\  .

	#. At a terminal window type \ ``start-openerp-web``\  to start the Open ERP Web server.


.. image:: images/web_welcome.png
	:align: center

You can verify the installation by opening a web browser on the server and navigating to http://localhost:8080 to connect to eTiny as shown in the figure below. You can also test this from another computer connected to the same network if you know the name or IP address of the server over the network – your browser should be set to http://<server_address>:8080 for this.

Verifying your Linux installation
###################################

.. index::
   single: pgAdmin III
.. 

You've used default parameters so far during the installation of the various components. If you've had problems, or you just want to set this up differently, the following points provide some indicators about how you can configure your installation.

.. tip::   **Tools**  *psql and pgAdmin* 

	psql is a simple client, executed from the command line, that's delivered with PostgreSQL. It enables you to execute SQL commands on your Open ERP database.

	If you prefer a graphical utility to manipulate your database directly you can install pgAdmin III (it is commonly installed automatically with PostgreSQL on a windowing system, but can also be found at \ ``http://www.pgadmin.org/`` \ ). 

""""""""""""""""""

	#. The PostgreSQL database starts automatically and listens locally on port 5432 as standard: check this by entering \ ``sudo netstat -anpt``\  t a terminal to see if port 5432 is visible there.

	#. The database system has a default role of \ ``postgres``\   accessible by running under the Linux postgres user: check this by entering \ ``sudo su postgres -c psql``\  at a terminal to see the psql startup message – then type \ ``\q``\  to quit the program.

	#. Start the Open ERP server from the postgres user (which enables it to access the PostgreSQL database) by typing \ ``sudo su postgres -c tinyerp-server.``\  

	#. If you try to start the Open ERP server from a terminal but get the message  *socket.error: (98, 'Address already in use')* then you might be trying to start Open ERP hile an instance of Open ERP is already running and using the sockets that you've defined (by default 8069 and 8070). If that's a surprise to you then you may be coming up against a previous installation of Open ERP or Tiny ERP, or something else sing one or both of those ports. Type \ ``sudo netstat -anpt``\  to discover what is running there, and record the PID. You can check that the PID orresponds to a program you can dispense with by typing \ ``ps aux | grep <PID>``\   and you can then stop the program from running by typing \ ``sudo kill <PID>``\   You need additional measures to stop it from restarting when you restart the server.

	#. The Open ERP server has a large number of configuration options. You can see what they are by starting the server with the argument \ ``–help``\   By efault the server configuration is stored in the file \ ``.terp_serverrc``\  in the user's home directory (and for the postgres user that directory is \ ``/var/lib/postgresql``\  .

	#. You can delete the configuration file to be quite sure that the Open ERP server is starting with just the default options. It is quite common for an upgraded system to behave badly because a new version server cannot work with options from a previous version. When the server starts without a configuration file it will write a new one once there is something non-default to write to it – it will operate using defaults until then.

	#. To verify that the system works, without becoming entangled in firewall problems, you can start the Open ERP client from a second terminal window on the server computer (which doesn't pass through the firewall). Connect using the XML-RPC protocol on port 8069 or NET-RPC on port 8070. The server can use both ports simultaneously. The window displays the log file when the client is started this way.

	#. The client configuration is stored in the file \ ``.terprc``\  in the user's home directory. Since a GTK client can be started by any user, each user would have their setup defined in a configuration file in their own home directory.

	#. You can delete the configuration file to be quite sure that the Open ERP client is starting with just the default options. When the client starts without a configuration file it will write a new one for itself.

	#. The eTiny web server uses the NET-RPC protocol. If a GTK client works but eTiny doesn't then the problem is either with the NET-RPC port or with eTiny itself, and not with the Open ERP server.

.. tip::   **A step further**  *One server for several companies* 

	You can start several Open ERP application servers on one physical computer server by using different ports. If you have defined multiple database roles in PostgreSQL, each connected through an Open ERP instance to a different port, you can simultaneously serve many companies from one physical server at one time.


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

