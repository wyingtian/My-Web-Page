#!/bin/sh
# Assignment7 1a, 
# useage URL http://www.people.fas.harvard.edu/~yingtianwang/mwp/ncal3.cgi?[month]
# shows the month of the year, if the query month past the currrent month 
# display the month of next year
# use the program yearcal

echo "Content-type: text/plain"
echo ""

# find the current month
CUR_MONTH=$(date +%m)
#find the current year
CUR_YEAR=$(date +%Y)

# change the word to num of the year
QUERY_MONTH_NUM=$(./name2num $QUERY_STRING)
CUR_MONTH_NUM=$(./name2num $CUR_MONTH)

# if the ask the month is less than current month,present next year
if [ $QUERY_MONTH_NUM -lt $CUR_MONTH_NUM ]
then 
# calculate next year
	NEXT_YEAR=$(($CUR_YEAR+1))

# present the query month of next year
	./yearcal $QUERY_MONTH_NUM $NEXT_YEAR
else 
	./yearcal $QUERY_MONTH_NUM
fi


