# Q1: How many files in `/bin` were renamed?
**A1:** 

# Q2: What is the full filepath of the program that is printing text to the terminal intermittently?
**A2:** It is occuring regularly so you can check `crontab -e` and see something is happening. From there you can check every `/etc/cron*/*` file to see if there is something there. In one of them, you will see the text that gets printed.

# Q3: What is the flag?
**A3:**