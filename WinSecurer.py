import os
import ctypes
import hashlib
from getpass import getpass

def hash_password(password: str) -> str:
    """Hashes a password with SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def lock_directory(directory: str, password: str):
    """Locks a directory with a password."""
    hashed_password = hash_password(password)
    password_file = os.path.join(directory, '.pwd')
    
    # Save hashed password to a hidden file
    with open(password_file, 'w') as f:
        f.write(hashed_password)
    
    # Hide the directory
    ctypes.windll.kernel32.SetFileAttributesW(directory, 0x02)  # 0x02 = Hidden attribute

def unlock_directory(directory: str, password: str):
    """Unlocks a directory if the correct password is provided."""
    password_file = os.path.join(directory, '.pwd')
    
    if not os.path.exists(password_file):
        print("Directory is not locked.")
        return
    
    with open(password_file, 'r') as f:
        stored_password_hash = f.read()
    
    if stored_password_hash == hash_password(password):
        # Remove hidden attribute
        ctypes.windll.kernel32.SetFileAttributesW(directory, 0x80)  # 0x80 = Normal attribute
        os.remove(password_file)
        print("Directory unlocked.")
    else:
        print("Incorrect password.")

def main():
    print("WinSecurer - Enhance your file security with password protection.")
    choice = input("Do you want to (L)ock or (U)nlock a directory? (L/U): ").strip().upper()

    if choice not in ['L', 'U']:
        print("Invalid choice. Please select 'L' to lock or 'U' to unlock.")
        return

    directory = input("Enter the full path of the directory: ").strip()
    
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    if choice == 'L':
        password = getpass("Enter a password to lock the directory: ")
        lock_directory(directory, password)
        print("Directory locked.")
    elif choice == 'U':
        password = getpass("Enter the password to unlock the directory: ")
        unlock_directory(directory, password)

if __name__ == "__main__":
    main()