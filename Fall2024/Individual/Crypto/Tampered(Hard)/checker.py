import crc32c

def calculate_crc32c(message: str) -> str:
    """Calculate CRC32C (iSCSI) checksum for a given message and return as lowercase hex string."""
    return f"{crc32c.crc32c(message.encode('utf-8')):08x}"

def verify_checksums(messages_file: str, checksums_file: str) -> None:
    """Verify CRC32C checksums for each line in messages_file against checksums_file."""
    with open(messages_file, 'r', encoding='utf-8') as f_messages, open(checksums_file, 'r', encoding='utf-8') as f_checksums:
        messages = [line.strip() for line in f_messages]
        checksums = [line.strip() for line in f_checksums]

    # Iterate through each line, calculate the checksum and verify
    all_match = True
    for i, (message, checksum_line) in enumerate(zip(messages, checksums)):
        checksum_from_file = checksum_line.split('|')[-1].strip().lower()
        calculated_checksum = calculate_crc32c(message)
        
        if calculated_checksum != checksum_from_file:
            print(f"Mismatch on line {i}: Calculated={calculated_checksum}, Expected={checksum_from_file}")
            all_match = False
        else:
            print(f"Line {i} matches: {calculated_checksum}")

    if all_match:
        print("All checksums match!")
    else:
        print("Some checksums did not match.")

# Run the verification
verify_checksums("Fall2024\Individual\Crypto\Tampered(Hard)\checksums_linesonly.log", "Fall2024\Individual\Crypto\Tampered(Hard)\checksums.log")
