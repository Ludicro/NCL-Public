# Q1: How many users ran sudo commands in the log?
**A1:**
`cat audit.log | grep sudo | awk '{print $4}' | sort | uniq | wc -l`


# Q2: How many unique commands were run?
**A2:**
`grep "COMMAND=" audit.log | awk -F'COMMAND=' '{print $2}' | sort | uniq | wc -l`

# Q3: How many commands were successfully run?
**A3:**
`grep "session opened" audit.log | wc -l`

# Q4: How many commands were unsuccessfully run?
**A4:**
`grep "session closed" audit.log | wc -l`

# Q5: Which user had the most opened sessions?
**A5:**
`grep "session opened" audit.log | awk '{print $13}' | awk -Fu '{print $1}' | sort | uniq -c`
