check = [215, 207, 221, 169, 199, 214, 197, 198, 169, 189, 178, 182, 181]
password = ''
for byte in check:
    password += chr(byte ^ 0x84)
print(password)