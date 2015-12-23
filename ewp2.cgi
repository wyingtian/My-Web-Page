#!/bin/sh


# The cgi program that generate html file. It provides a set of checkboxes
# for the items in data/cities.tab files.  When user click delete, it will 
# call delete_item_2.cgi to delete this program
echo "Content-type: text/html"	# tell browser type of output
echo ""	
# display the begining part of this html
cat "ewp.head"
echo "<b>Delete an Item</b></dt>"
echo	"<dd>"
echo	"<p>"
echo	"Use this function to select an item from a page."
echo	"Then press the <b>Delete</b> button."
echo	"<p>"
echo	"<form action='delete_item_2.cgi' method=get>"
# set IFS new line, so it treat city name with sapce such as New York together
IFS=$'\n' 
# iterate the files in ./data direcotry
for i in `ls ./data`
do
echo "<p>"
echo "Page name: $i"	
# iterate through the items in the file
	# N=1		# number the checkboxes so multiple ones are ok
	# 		# note: thanks to bmolay for this idea
	for j in `grep "title="  "./data/$i"|cut -d'|' -f1 |cut -d'=' -f2`
	do  
		echo "<br>"
		echo "Title:"	
		# generate check box
		echo "<INPUT TYPE='CHECKBOX' NAME='check' VALUE='$j'> $j "
		# N=$(expr $N + 1)
	done
echo "</p>"
done
echo	   "<input type=submit value=' delete '>"
echo	"</form>"
echo	"</dd>"
echo "<dt>"
echo "<hr>"
# display the end part of the html
cat "ewp.tail"