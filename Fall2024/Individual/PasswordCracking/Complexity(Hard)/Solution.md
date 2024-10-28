# Q1-Q3: Passwords Meet the Following Password Requirements:
```
1. Password length is at least 8 characters
2. Contains 2 from the following categories:
    - Uppercase Letters
    - Lowercase Letters
    - Numbers (0-9)
```
***A1-A3:***

hashcat -w 4 -a 3 -o solved_pass.txt hashes.txt ?a?a?a?a?a?a?a?a --increment-min=8 -1 ?u?l?d


# Q4-Q5: Passwords Meet the Following Password Requirements:
```
1. Be a minimum of ten (10) characters in length
2. Contain characters from all of the following categories:
    - Uppercase letter (A-Z)
    - Lowercase letter (a-z)
    - Number (0-9)
```
***A4-A5:***

# Q6: Passwords Meet the Following Password Requirements:
```
1. Be a minimum of ten (10) characters in length
2. Contain characters from all the following categories:
    - Uppercase letter (A-Z)
    - Lowercase letter (a-z)
    - Number (0-9)
3. Must not repeat a character three (3) or more times in a row (e.g. secret111, sssecret)

```
***A6:***

# Q7: Passwords Meet the Following Password Requirements:
```
1. Be a minimum of ten (10) characters in length
2. Contain characters from all the following categories:
    - Uppercase letter (A-Z)
    - Lowercase letter (a-z)
    - Number (0-9)
3. Must not repeat a character three (3) or more times in a row (e.g. secret111, sssecret)
4. Must not contain any english dictionary words
```
***A7:***

# Q8: Passwords Meet the Following Password Requirements:
```
1. Be a minimum of ten (10) characters in length
2. Contain characters from all the following categories:
    - Uppercase letter (A-Z)
    - Lowercase letter (a-z)
    - Number (0-9)
    - Special characters (~!@#$%^&*_-+=`|(){}[]:;"'<>,.?/)
3. Must not repeat a character three (3) or more times in a row (e.g. secret111, sssecret)
4. Must not contain any english dictionary words
```
***A8:***

