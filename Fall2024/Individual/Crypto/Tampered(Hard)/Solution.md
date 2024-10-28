# Q1: What variant of the crc32 checksum algorithm is being used on these messages?
**A1:** Copy a line `I just got home, finally!` and paste it into a crc32 calculator and go through different alogorithms until you find one that matches.

# Q2: What is the index (not line number) of the line that has an invalid checksum?
**A2:** I created a script that will calculate the checksum of each line and compare it to the checksum in the file then find which line gets flagged.

# Q3: What should be the checksum based on the contents of the invalid line?
**A3:** The above script will also print the actual checksum.