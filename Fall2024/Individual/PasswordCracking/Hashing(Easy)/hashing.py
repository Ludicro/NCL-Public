
import hashlib

# Open and read strings.txt file
with open('Fall2024\PasswordCracking\Hashing(Easy)\strings.txt', 'r') as file:
    strings = file.readlines()

# Process each line
for line in strings:
    # Remove newline characters
    line = line.strip()
    
    # Calculate hashes
    md5_hash = hashlib.md5(line.encode()).hexdigest()
    sha1_hash = hashlib.sha1(line.encode()).hexdigest()
    sha256_hash = hashlib.sha256(line.encode()).hexdigest()
    
    # Print results
    print(f"String: {line}")
    print(f"MD5: {md5_hash}")
    print(f"SHA1: {sha1_hash}")
    print(f"SHA256: {sha256_hash}")
    print("-" * 50)
