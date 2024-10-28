# Q1: How many emails are saved on this device?
**A1:** Count the number of files in `/messages` and divide by 2 as half the files are sig files

# Q2: What is the filename of the email message that was sent by badguy@cityinthe.cloud?
**A2:** Running the command `grep -Rnw '/root/messages' -e 'badguy@cityinthe.cloud'` will give tell you what sig file that shows the email file that was tampered with. 

# Q3: What is the filename of the email message that was tampered with?
**A3:**
Import the keys into gpg

Create a script like:
```bash
#!/bin/bash

# Change to the directory containing the email files
cd /root/messages/

for file in email_*.txt; do
    sig="${file}.sig"

    # Check if the signature file exists
    if [[ -f "$sig" ]]; then
        echo "Verifying $file with key1:"
        gpg --verify "$sig" "$file" 2>&1 | grep -E 'good signature|BAD signature'

        echo "Verifying $file with key2:"
        gpg --verify "$sig" "$file" 2>&1 | grep -E 'good signature|BAD signature'
    else
        echo "Signature file for $file not found."
    fi
done
```
This will run and verify the signature of the email messages with the two keys.

Any output that says `BAD signature` is the file that was tampered with.