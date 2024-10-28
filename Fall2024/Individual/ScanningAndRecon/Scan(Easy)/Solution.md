# Q1-Q3: What are the 1st, 2nd, and 3rd lowest ports?
**A:**Run `nmap -Pn -sT -p- target`

This will show all ports on TCP

# Q4: What is the only service that responds with actual data?
**A4:**Attempt to scan each one with `nmap -sV -p PORT target` and if they take too long, cancel and go to the next until you find it.