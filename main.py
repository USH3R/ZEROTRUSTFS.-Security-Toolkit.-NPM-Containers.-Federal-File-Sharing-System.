# main.py

from auth_service import authenticate
from device_validator import validate_device
from policy_evaluator import check_policy
from file_handler import access_file

print("🚀 Welcome to Zero Trust FS")
print("Please enter your username, password, device, and file to begin.\n")

# --- Start authentication workflow ---
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
device_id = input("Enter device ID: ").strip()
file_name = input("Enter file to access: ").strip()

# Authentication
if not authenticate(username, password):
    print("❌ Authentication failed. Access denied.")
    exit(1)

# Device validation
if not validate_device(username, device_id):
    print("❌ Device validation failed. Access denied.")
    exit(1)

# Policy / access check
if not check_policy(username, file_name):
    print("❌ Policy check failed. Access denied.")
    exit(1)

# Access file
if access_file(file_name):
    print(f"✅ Access granted: {file_name}")
else:
    print(f"❌ Unable to access file: {file_name}")
