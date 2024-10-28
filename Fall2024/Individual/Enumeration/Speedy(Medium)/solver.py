import hashlib
import itertools
import string

def try_hash(chars):
    m = hashlib.md5()
    m.update(chars.encode()) # turn chars into bytes then turn bites into hash
    return m.digest() # Return the raw hash as bytes

# Find first 3 chars
for combo in itertools.product(string.printable, repeat=3): #for all possible combinations of 3 chars
    test = ''.join(combo) # join the chars together
    if try_hash(test).hex().startswith('8fcce5'): # if the hash starts with 8fcce5
        print(f"First 3 chars: {test}") 
        break

# Get remaining chars
key = [47, 69, 82, 74, 80, 47, 54, 58, 48, 58] # Creates a list of the key that we need to match
key_byte = 0x8f & 0x12  # Performs bitwise AND between hex values 0x8f and 0x12, result is 0x02 (2)
# ^ is done because the original code does the same with the index of hash[0] (0x8f) and 0x12
rest = ""
for k in key: # For each number in the key list
    rest += chr(k ^ key_byte) # XOR it with the key_byte and convert to a character
print(f"Remaining chars: {rest}")
