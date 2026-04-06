# main.py

import yaml
from auth_service import authenticate_user
from device_validator import validate_device
from policy_evaluator import check_policy
from file_handler import access_file

# 1. Load the configuration (settings.yaml)
# This is required because our functions need to look up hashes and roles
try:
    with open("settings.yaml", "r") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("❌ Error: settings.yaml not found!")
    exit(1)

# 2. Welcome message
print("🚀 Welcome to Zero Trust FS")
print("Please enter your username, password, device, and file to begin.\n")

# 3. Prompt user input (using .strip() to avoid "invisible space" errors)
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
device_id = input("Enter device ID: ").strip()
file_name = input("Enter file to access: ").strip()

# --- STEP 1: Authentication ---
# Checks if username exists and password hash matches
if not authenticate_user(username, password, config):
    print("❌ Authentication failed. Access denied.")
    exit(1)

# --- STEP 2: Device Validation ---
# Checks if the device ID is authorized for this specific user
if not validate_device(username, device_id, config):
    print("❌ Device validation failed. Access denied.")
    exit(1)

# --- STEP 3: Policy / RBAC Check ---
# Checks if the user's role (admin/editor/viewer) allows access to the file
if not check_policy(username, file_name, config):
    print("❌ Policy check failed. Access denied.")
    exit(1)

# --- STEP 4: Final Access ---
# Correctly passing username, file, and config to the handler
if access_file(username, file_name, config):
    print(f"✅ Access granted: {file_name}")
else:
    print(f"❌ Unable to access file: {file_name}")# main.py

import yaml
from auth_service import authenticate_user
from device_validator import validate_device
from policy_evaluator import check_policy
from file_handler import access_file

# === Load configuration from settings.yaml ===
with open("settings.yaml", "r") as f:
    config = yaml.safe_load(f)

# === Welcome message ===
print("🚀 Welcome to Zero Trust FS")
print("Please enter your username, password, device, and file to begin.\n")

# --- Prompt user input ---
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
device_id = input("Enter device ID: ").strip()
file_name = input("Enter file to access: ").strip()

# --- Step 1: Authenticate user ---
if not authenticate_user(username, password, config):
    print("❌ Authentication failed. Access denied.")
    exit(1)

# --- Step 2: Validate device ---
if not validate_device(username, device_id, config):
    print("❌ Device validation failed. Access denied.")
    exit(1)

# --- Step 3: Check policy / access rights ---
if not check_policy(username, file_name, config):
    print("❌ Policy check failed. Access denied.")
    exit(1)

# --- Step 4: Access file ---
if access_file(file_name):
    print(f"✅ Access granted: {file_name}")
else:
    print(f"❌ Unable to access file: {file_name}")
