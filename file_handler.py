# file_handler.py
import os

def access_file(username, requested_file, config):
    """
    Minimal file access enforcement.
    Returns True if the file exists and user is authorized (checked in policy_evaluator).
    For demonstration, we only check if the file exists in a local 'files/' folder.
    """
    # Minimal file storage folder
    files_folder = config.get("files_folder", "files")
    
    # Full path to requested file
    file_path = os.path.join(files_folder, requested_file)
    
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"⚠️ File not found: {requested_file}")
        return False
    
    # Access granted (authorization already checked before calling this)
    return True
