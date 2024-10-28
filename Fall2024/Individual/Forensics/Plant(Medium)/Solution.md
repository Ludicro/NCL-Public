# Q1: What is the name of the suspicious file in the installer?
**A1:** I don't know how to find this

This can apparently be found by just opening the file in FTK Imager and going to the root directory and searching for "PDF". It's the first result.

# Q2: What is the flag?
**A2:** Add the Yara rule to autopsy and then add the disk image to the case. When it is done with the analysis, it will flag a PDF. Clicking on it will show the flag.