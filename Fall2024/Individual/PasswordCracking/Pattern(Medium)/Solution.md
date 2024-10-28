# Q1-Q3: These are all salted hashes and are told they follow the pattern: SKY-MASK-####
**A1-A3:** Use a hashcat command to crack the hashes. You can't use crackstation since these are salted.

`hashcat -w 4 -m 500 -a 3 hashes.txt 'SKY-MASK-?d?d?d?d' -o hashes_solved.txt`
