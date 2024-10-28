# Context of Log
```
    1         2        3     4       5        6              7         8       9         10            11
packet_no,timestamp,src_ip,dst_ip,src_port,dst_port,transport_proto,tcp_seq,tcp_flags,additional,bytes_transferred
```
# Q1: How many unique IP addresses are in this log?
**A1:**
`awk -F',' 'NR > 1 {print $3; print $4}' packets.csv | sort | uniq | wc -l`

# Q2: How much time (in milliseconds) elapsed between the first and last packets in this log?
**A2:**
`awk -F',' 'NR ==2 {first=$2} {last=$2} END {print last - first}' packets.csv`

`-F','`: Sets the field separator to a comma.

`NR==2 {first=$2}`: On the second line (the first data row), store the timestamp in the variable first.

`{last=$2}`: For every line,update last to the current timestamp (so after the last line, last will hold the last packet's timestamp).

`END {print (last - first)`}: At the end, calculate the difference between the last and first timestamps

# Q3: How many UDP packets were seen in this log?
**A3:**
`awk -F',' '{print $7}' packets.csv | grep "UDP" | wc -l`

# Q4: What is the total number of bytes transferred in this log?
**A4:**
`awk -F',' 'NR > 1 {sum += $11} END {print sum}' packets.csv`

# Q5: How many total bytes were sent by 146.75.33.44 (exclude received packets)?
**A5:**
`awk -F',' 'NR > 1 {print $3 " " $11}' packets.csv | grep "146.75.33.44" | awk '{sum += $2} END {print sum}'`

# Q6: What IP address responded to a ping?
**A6:**
`awk -F',' '$7 == "ICMP" {print $3 $10}' packets.csv | grep "type: 0"`

# Q7: What pair of IP addresses generated the largest amount of network traffic? [e.g. `1.1.1.1` <> `2.2.2.2`]
**A7:**
`awk -F',' 'NR > 1 {key = ($3 < $4) ? $3 "," $4 : $4 "," $3; traffic[key] += $11} END {for (pair in traffic) if (traffic[pair] > max) {max = traffic[pair]; max_pair = pair} } END {print max_pair " generated " max " bytes of traffic"}' packets.csv `

`-F','`: Sets the field separator to a comma.

`NR > 1`: Skips the header line.

`key = ($3 < $4) ? $3 "," $4 : $4 "," $3`: Creates a unique key for each pair of IP addresses (regardless of order) to ensure that 1.1.1.1,2.2.2.2 is treated the same as 2.2.2.2,1.1.1.1.

`traffic[key] += $11`: Sums the bytes transferred ($11) for each unique key (IP pair).

The first `END` block: Finds the pair with the maximum traffic.

The second `END` block: Prints the pair of IP addresses and the total bytes of traffic generated.
