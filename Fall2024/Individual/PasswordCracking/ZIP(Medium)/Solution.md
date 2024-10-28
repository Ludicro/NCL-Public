# Q1: What is the plaintext password used to open the password-protected zip archive? 
**A1:**
`zip2john zip.zip > zip.hash`
`john zip.hash`

# Q2: What is the flag found after opening the zip archive?
**A2:**
Use the password `john` gives to open the txt file.