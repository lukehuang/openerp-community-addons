
.. index::
   single: Timesheets
.. 

Timesheets
===========

In most service companies where Open ERP has been integrated, service sheets, or timesheets, have revolutionized management practices. These service sheets are produced by each employee as they work on the different cases or projects that are running. Each of these is represented by an analytic account in the system.

Throughout the day, when employees work on one project or another, they add a line to the timesheets with details of the time used on each project. At the end of the day, each employee must mark all the time worked on client or internal projects to make up the full number of hours worked in the day. If an account isn't in the system then the time is added to the hours that haven't been assigned for the day.

.. image::  images/service_timesheet_list.png
	:align: center

*Timesheet for a working day.*

The figure gives an example of a timesheet for an employee.

.. tip::   *Don't confuse* 

	The timesheet system isn't intended to be a disguised attendance form. There's no control over the service times and the employee is free to encode 8 or 9 hours or more of services each day if they want.

	If you decide to put such a system into place, it's important to clarify this point with your staff. The objective here isn't to control hours, because the employees decide for themselves what they'll be entering – but to track the tasks running and the allocation of costs between them.

Amongst the many uses of such a timesheet system for a company, here are some of the most important:

* enabling tracking of the true costs of a project by accounting for the time used on it,

* tracking the services provided by different employees,

* comparing the hours really used on a project with the initial planning estimates,

* automatically invoicing based on the service hours provided,

* obtaining a list of the service hours for a given client,

* knowing the costs needed to run the company, such as the marketing costs, the training costs for a new employee, and the invoicing rates for a client. 

.. index::
   single: Employee; Configuration
.. 

Employee configuration
-----------------------

To be able to use the timesheets at all, you must first define those employees who are system users. The employee definition forms contain the information necessary to use that sheet, such as the job title, and hourly costs.

Two fields will be of particular interest to you for managing timesheets: the  *Analytic Journal * and the  *Product* .

In the analytic journal will be stored all the analytic entries about the costs of service times. These enable you to isolate the cost of service from other company costs such as the purchase of raw materials, expenses receipts and subcontracting. You can use different journals for each employee to separate costs by department or by function.

The employee is also associated with a product in your database in Open ERP. An employee is linked with a product so they can be 'bought' (subcontracting) or 'invoiced' (project management). You have to create a product for each job type in your company.

The following information is important in the product form:

*  *Name* \ ``Secretary``\  \ ``Salesperson``\  \ ``Project Manager``\  

*  *Product Type* \ ``Service``\  

*  *Unit of Measure* \ ``Hour``\  \ ``Day``\  

*  *List Price* 

*  *Standard Price* 

.. tip::   *A step further* 

	The module ``product_index`` lets you generate indexes connected to the change of purchase or sale price for individual products. 

	In human resources, this module can be used to change your prices or costs in step with a national index.

 *Product Category* \ ``Employees``\  

In summary, each company employee corresponds, in most cases, to:

*  *Partner* 

* an Employee form,

*  *System User.* 

And each company job position corresponds to a *Product* .


.. tip::   *Note* 

	By default the hourly cost of an employee is given by the standard cost of the product linked to that employee. But if you install the ``hr_contract`` module it's possible to manage contracts differently. The hourly cost of the employee is then automatically calculated from their employment contract when they enter their timesheet data.

	To do this, the software uses a factor defined in the contract type (for example, the gross monthly salary, calculated per day). Ideally this factor should take into account the salary costs, and the taxes, insurances and other overheads associated with pay.

.. index::
   single: Timesheets; Entering data
.. 

Entering timesheet data
-------------------------

To be able to use timesheets, you should install the module \ ``hr_timesheet``\  . Once this module has been installed and the employees configured, the different system users can enter their timesheet data in the menu  *Human Resources > Hours Encoding > For me > My Works of the Day* .

.. tip::   *Advice* 

	It's a good idea if all employees who use timesheets place this menu in their shortcuts. That's because they'll need to return to them several times each day.

 *New* 

	#. The  *User* is proposed by default, but you can change it if you're encoding the first timesheet for another company employee.

	#. The  *Date* is automatically proposed as today's date, but it's possible to change it if you're encoding the timesheet for a prior day.

	#.  *Analytic Account* 

	#.  *Quantity* 

 *Description* 

The other fields are automatically completed but can be modified: the  *Product* , the  *Unit of Measure* , the  *Cost*  of the service, and the associated  *General Account* .

The hours are then encoded throughout the day by each employee. It helps to revisit the list at the end of the day to verify that the number of hours of attendance in the company has been properly accounted for. The total entered is shown at the bottom right of the list of service hours.

The accuracy of the services entered is crucial for calculating the profitability of the different jobs and the recharging of services. Different reports are therefore available for verifying employees' data entry. Employees can verify their own timesheet using the following reports:

* Printing the timesheets per month, using the menu  *Human Resources > Reporting > Timesheet > Print My Timesheet* .

* Reviewing all service entries using the menu  *Human Resources > Hours Encoding > For Me > All My Work* . You can then use the filters to analyze your services by project, by period or by product.

.. tip::   *Technique* 

	By default, Open ERP is configured to show the cost of each service when an employee encodes the number of hours per project. You can modify this field by adding the attribute invisible=True in the timesheet view.

	The value in this field shows employees the cost of their time used in the company, so masking this field might not always be the best option.

Managers can draw on different reports for managing timesheets quite easily. You can print a summary in the form of a table per user and per day in the menu  *Human Resources > Reporting > Timesheet > Print Summary Timesheet* . This helps you spot when an employee has forgotten to encode her timesheet on a certain day.

.. image::  images/service_timesheet_all.png
	:align: center

*Employee's monthly summary timesheet.*

Many graphs are available through the menus  *Human Resources > Reporting > This Month / All Months* , for example:

*  *Timesheet by User* 

*  *Timesheet by Account* 

*  *Timesheet by Invoice* 

*  *Daily Timesheet by Account* 

.. image::  images/service_timesheet_graph.png
	:align: center

*Chart of timesheet by account.*

The data making up these graphs can be varied using the filters available in the upper part of the screen. If you want to get more exact figures, switch to the list view.

.. tip::   *Note* 

	The dashboard for managing projects has a graphical view that summarizes the current user's timesheet for the last seven days.

	It's possible to assign a dashboard to users so that it appears when they sign onto Open ERP. Then each employee will be able to notice if they've forgotten to complete their timesheet when they signed out of the system.

	To use this dashboard, install the module ``board_project``.

.. index::
   single: Timesheets; Evaluation
.. 

Evaluation of service costs
-----------------------------

You already know that timesheets are closely linked with analytic accounts. The different projects reported on the timesheets correspond to analytic accounts. The timesheet entries themselves are analytic entries. These entries comprise various analytic operations that don't correspond to any of the general accounts. Therefore all operations that modify and create timesheet lines automatically impact the corresponding analytic line and, conversely are automatically modified by changes in that line.

.. tip::   *Technique* 

	The implementation of timesheets in Open ERP relating to analytic entries is managed by an inheritance mechanism: the timesheet object inherits the analytic entry object.

	The information is therefore not encoded into the database as two separate events, which avoids many synchronization problems. They are stored in two different tables, however, because a service is an analytical entry, but an analytical entry isn't necessarily a service.

This isn't a classical approach but it's logical and pragmatic. Employee timesheets are a good indication of how the costs of a service enterprise are spread across different cases as reported in the analytic accounts.

An analytic account should be reflected in the general accounts, but there's no direct counterpart of these analytic accounts in the general accounts. Instead, if the hourly costs of the employees are correctly accounted for, the month's timesheet entries should be balanced by the salary + benefits package paid out to all the employees at the end of the month.

Despite all this it's quite difficult to work out the average hourly cost of an employee precisely because it depends on:

* the extra hours that they've worked,

* holidays and sickness,

* salary variations and all the linked costs, such as social insurance charges.

The reports that enable you to relate general accounts to analytic accounts are valuable tools for improving your evaluation of different hourly costs of employees. The difference between product balances in the analytic account and in the general accounts, divided by the total number of hours worked, can then be applied to the cost of the product. Some companies adjust for that difference by carrying out another analytic operation at the end of the month in an account created for that purpose. This analytic account should have a balance that tends towards zero.

Because you've got a system with integrated timesheets you can then:

* track the profitability of projects in the analytic accounts,

* look at the history of timesheet entries by project and by employee,

* regularly adjust hourly costs by comparing your rates with reality,

.. tip::   *Important* 

	Controlling the costs and the profitability of projects precisely is very important.

	It enables you to make good estimates and to track budgets allocated to different services and their projects, such as sales and, R&D costs. You can also refine your arguments on the basis of clear facts rather than guesses if you have to renegotiate a contract with a customer following a project slippage.

The analyses of profitability by project and by employee are available from the analytic accounts. They take all of the invoices into account, and also take into account the cost of the time spent on each project.

 *Cost Ledger (only by quantity)* 

.. index:: Department

Managing by department
-----------------------

When they're used properly, timesheets can be a good control tool for project managers and can provide awareness of costs and times.

When employee teams are important, a control system must be implemented. All employees should complete their timesheets correctly because this forms the basis of planning control, and the financial management and invoicing of projects

You'll see in the next chapter that it's possible to automatically invoice services at the end of the month based on the timesheet. But at the same time some contracts are limited to prepaid hours. These hours and their deduction from the original limit are also managed by these timesheets.

In such a situation, hours that aren't coded into the timesheets represent lost money for the company. So it's important to establish effective follow-up of the services timesheets and their encoding. To set up a structure for control using timesheets you should install the module \ ``hr_timesheet_sheet``\  .


.. image::  images/timesheet_flow.png
	:align: center

*Process of approving a timesheet.*

This module supplies a new screen enabling you to manage timesheets by period. Timesheet entries are made by employees each day. At the end of the week, employees validate their week's sheet and it's then passed to the services manager, who must approve his team's entries. Periods are defined in the company forms, and you can set them to run monthly or weekly.

To enter timesheet data each employee uses the menu  *Human Resources > Timesheets > My Timesheets > My Current Timesheet* .

.. image::  images/service_timesheet_sheet_form.png
	:align: center

*Form for entering timesheet data.*

In the upper part of the screen the user starts with the sign-in and sign-out times. The system enables the control of attendance day by day. The two buttons Sign in and Sign out enable the automatic completion of hours in the area to the left. These hours can be modified by employee, so it's not a true management control system.

The area to the bottom of the screen represents a sheet of the employee's time entries for the selected day. In total, this should comprise the number of hours worked in the company each day. This provides a simple verification that the whole day's attendance time has been coded in properly.

The second tab of the timesheet  *by day*  gives the number of hours worked on the different projects. When there's a gap between the attendance and the timesheet entries, you can use the second tab to detect the days or the entries that haven't been correctly coded in.

.. image::  images/timesheet_sheet_hours.png
	:align: center

*Detail of hours worked by day for an employee.*

The third tab,  *By account*  shows the time worked on all the different projects. That enables you to step back to see an overview of the time an employee has worked spread over different projects.

At the end of the week or the month, the employee confirms his timesheet. If the attendance time in the company corresponds to the encoded entries, the whole timesheet is then confirmed and sent to his department manager, who is then responsible for approving it or asking for corrections.

Each manager can then look at a list of his department's timesheets waiting for approval using the menu  *Human Resource > Timesheets > My Department's Timesheets > Timesheets to validate* . He then has to approve them or return them to their initial state.

To define the departmental structure, use the menu  *Administration > Users > Department Structure > Define Departments.* 

.. tip::   *Advice* 

	At first sight, the approval of timesheets by a department manager can seem a bureaucratic hindrance. This operation however is crucial for effective management. We have too frequently seen companies in the situation where managers are so overworked that they don't know what their employees are doing.

	So this approval process supplies the manager with an outline of each employee's work at least once a week. And this is carried out for the hours worked on all the different projects.

Once the timesheets have been approved you can then use them for cost control and for invoicing hours to clients.

Contracts and their rates, planning, and methods of invoicing are the object of the following chapter.




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

