#!/bin/sh
#
# add_item.cgi
# this script is called from ewp.html for the Add function
# it takes the specified items and creates a new record on the
# end of the named file in the data directory
#

	eval `./qryparse`		# receive form data
	DATAFILE=$pagename.tab		# $pagename set by qryparse

	echo "Content-type: text/plain"	# tell browser type of output
	echo ""				# end of header

	if test ! -d data		# if no data directory
	then
		mkdir data		# try to make it
		if test $? -ne 0	# and check for errors
		then
			echo "Cannot create data directory."
			exit
		fi
	fi

	cd data
	
	# check if the field entered is emtpy, if empty show warning message
	if [  -z "$pagename" -o "$pagename" = " " ]
	then echo "page name incomplete,please press the back button and try again"
	exit 1
	fi	

	if [  -z "$title" -o "$title" = " " ]
		then echo "title incomplete,please press the back button and try again"
		exit 1
	fi

	if [  -z "$titlecolor" -o "$titlecolor" = " " ]
		then echo "title color incomplete,please press the back button and try again"
		exit 1
	fi

	if [  -z "$descrip" -o "$descrip" = " " ]
		then echo "description incomplete,please press the back button and try again"
		exit 1
	fi
		
	if [  -z "$url" -o "$url" = " " ]
		then echo "url incomplete,please press the back button and try again"
		exit 1
	fi

	#if input title name already there, means user want to edit
	#this line, so delete this line first. 
	#if input title name not there, sed does nothing
	sed -i "/title=$title/d" $DATAFILE 
	
	#add the new data to the file.  
	printf "title=%s|tcolor=%s|desc=%s|url=%s\n" \
		"$title" "$titlecolor" "$descrip" "$url" >> $DATAFILE

	# show message of wheather addition successful
	if test $? -eq 0
	then
		echo "Addition of $title was successful."
		echo "Press the Back button now."
	else
		echo "Unable to update file $DATAFILE ."
		echo "Please report to page admin."
	fi



