# Q1: What application layer protocol is used by the client to obtain an IP address in this capture?
**A1:** Look at the protocol in Wireshark

# Q2: What transport layer protocol is used to send this request?
**A2:** Look at the packet and identify if it is TCP or UDP

# Q3: What is the transaction id of the request in hex?
**A3:** Find the transaction ID in the DHCP packet Info

# Q4: What is the length of the parameter request list?
**A4:** Look at the `Length` value in the parameter request list 

# Q5: What is the hostname of the device requesting an address?
**A5:**In the DHCP request, look at the Host Name value

# Q6: How long is the requested lease time in days?
**A6:**Look at the IP Address Lease time

# Q7: How long of a lease does the server actually give the client in minutes?
**A7:** In the DHCP Ack, look at the IP Address Lease time