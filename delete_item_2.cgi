#!/bin/sh
#
# delete_item_2.cgi
# called by ewp2.cgi to delete items by checked box
# it will delete the specified item from the page. 
# it will send back a status report indicating if the 
# item was there and if wad removed successfully.
#
# note: 
#       thanks to bmolay for hints on how to process multiple check boxes with
#        spaces in values
#
eval `./qryparse`		# receive form data

# tell browser type of output

echo "Content-type: text/plain"	
echo ""				# end of header

#echo "$check"
cd data
../qryparse | grep '^check=' | cut -d"'" -f2 | while read check
do
 # delete this item
	sed -i "/title=$check|/d" cities.tab    
	if test $? -eq 0
		then echo "$check is deleted"
	fi
done