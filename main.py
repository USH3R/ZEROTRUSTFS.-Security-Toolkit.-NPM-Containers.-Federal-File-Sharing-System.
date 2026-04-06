# orchestrator/main.py

import sys
import yaml
from identity.auth_service import authenticate_user
from device_trust.device_validator import validate_device
from policy_engine.policy_evaluator import check_policy
from access_gateway.file_handler import access_file

# Load configuration
with open("config/settings.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

def main():
    print("=== Zero Trust FS Minimal Pipeline ===\n")
    
    # Step 1: Get user input
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    device_id = input("Enter device ID: ").strip()
    requested_file = input("Enter file to access: ").strip()
    
    # Step 2: Authenticate
    if not authenticate_user(username, password, CONFIG):
        print("❌ Authentication failed. Access denied.")
        sys.exit(1)
    print("✅ Authentication successful")
    
    # Step 3: Device validation (optional)
    if not validate_device(username, device_id, CONFIG):
        print("❌ Device validation failed. Access denied.")
        sys.exit(1)
    print("✅ Device validation passed")
    
    # Step 4: Authorization / policy check
    if not check_policy(username, requested_file, CONFIG):
        print("❌ Policy check failed. Access denied.")
        sys.exit(1)
    print("✅ Policy check passed")
    
    # Step 5: File access enforcement
    if access_file(username, requested_file, CONFIG):
        print(f"✅ Access granted: {requested_file}")
    else:
        print(f"❌ Access denied: {requested_file}")

if __name__ == "__main__":
    main()
