import hashlib
import os


def calculate_checksum(file_path):
    """
    Calculate the checksum (SHA-256) of a file.

    Args:
    - file_path: Path to the file.

    Returns:
    - checksum: The calculated checksum.
    """
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


# Example usage
source_data_path = 'path/to/source/data'
backup_file_path = 'path/to/backup/file'

source_checksum = calculate_checksum(source_data_path)
backup_checksum = calculate_checksum(backup_file_path)

if source_checksum == backup_checksum:
    print("Backup is valid and identical to the source data.")
else:
    print("Backup is corrupted or different from the source data.")
