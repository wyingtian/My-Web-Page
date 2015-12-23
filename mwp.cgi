#!/bin/sh

# this is a cgi program that generate a html file that display 
# some cities links
echo "Content-type: text/html"
echo ""

#QUERY_STRING is the data file name
DATA_FILE="$QUERY_STRING.tab" 
# cities.head is begining part of an html file
cat ./cities.head
# this command use the "fl" program to generate html based 
# on the cities in files
./fl -d'|' cities.fmt data/$DATA_FILE
# cities.tail is the ending part of an html file
cat ./cities.tail
