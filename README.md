# Purpose
	Using shell written cgi programs to generate dynamic web page.

*
	URL: http://www.people.fas.harvard.edu/~yingtianwang/mwp/ncal3.cgi?[month]
	the [month] in the URL can be a number or word
	This will show the calender of that month.

* Note:
This program shows the month of the year, if the query month past the currrent month 
display the month of next year. it uses the program yearcal and name2num.


*
	files: year.html ncal3.cgi

	usage: URL http://www.people.fas.harvard.edu/~yingtianwang/mwp/year.html
	and then click the month.


*	files: mwp.cgi   
		cities.head  #this is the first part of a html file, used by mwp.cgi
		cities.tail  #this is the ending part of a html file, used by mwp.cgi
		cities.fmt   #this is the format file to generate html, used by fl program
		cities.tab   #this is the data file, used by fl program. This file is under data directory
		fl           #this is a executable c program, used by mwp.cgi to generate html

*	usage: URL http://www.people.fas.harvard.edu/~yingtianwang/mwp/mwp.cgi?cities
			and then click on city name to get to antoher website





*	files: add_edit_item.cgi   #this script add an entry to the datafile
							   #if the title name already exist, delete it and then add the new entry
			delete_item.cgi    #this script accept the name of a page and item from the form and will 					   #delete the specified item from the page.
			view_page.cgi      #show a page of a item
			ewp.html           #main html file 

*	Identify missing data:
			For add_edit_item.cgi and delete_item.cgi, if the user does not provide enough info for the
			script to do the work, the script will send a message of Incomplete data




* a) pick from Lists
		files:  ewp2.cgi      The cgi program that generate html file. It provides a set of checkboxes
							  for the items in data/cities.tab files.  When user click delete, it will 
							  call delete_item_2.cgi to delete this program
				delete_item_2.cgi 
							  This program delete items that is checked in cities.tab
				ewp.head  	  begining part of html, used by ewp2.cgi
				ewp.tail	  end part of html, used by ewp2.cgi
				
		Good thing: the webpage generate checkboxes with the titles in the data file, the user will not need to remembere the exact name of the page
