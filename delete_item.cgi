#!/bin/sh
#
# delete_item.cgi
# this script is called from ewp.html for the delete function, it will delete
# the specified item from the page. it will send back a status report indicating if the 
# item was there and if wad removed successfully.
#

eval `./qryparse`		# receive form data
DATAFILE=$pagename.tab		# $pagename set by qryparse

echo "Content-type: text/plain"	# tell browser type of output
echo ""				# end of header

# check if page name or title is empty
	if [  -z "$pagename" -o "$pagename" = " " ]
		then echo "please enter page name"
		exit 1
	fi	

	if [  -z "$title" -o "$title" = " " ]
		then echo "please enter title"
		exit 1
	fi

# check if the data direcotry there
	if test ! -d data		# if no data directory
	then
		echo "$pagename not found"
		exit 1
	fi

	cd data
# check if the <pagename> file exist
	if test ! -f $DATAFILE
	then 
		echo "$pagename not found"
		exit 1
	fi
# if title is not found, show the info, otherwise delete this item
	if ! grep "title=$title" $DATAFILE > ./tmp 
		then echo "$title not found"
	else 
		sed -i "/title=$title/d" $DATAFILE     # delete this item
		if test $? -eq 0
			then echo "$title is deleted"
		fi
	fi