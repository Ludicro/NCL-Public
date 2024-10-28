# Q1: What is the record type of scan.domain.cityinthe.cloud?
**A1:**Run a DNS query on `scan.domain.cityinthe.cloud` and you'll get 2 records, one is a full type that makes logical sense.

# Q2: What value is given by scan.domain.cityinthe.cloud?
**A2:**Take the value given in that record type, it may even be another domain

# Q3: What is the flag?
**A3:**Doing DNS lookups on `dnschecker.org` with the clues they give "scan" -> "info" -> "mail" -> "answer", you get a SRV with the flag.