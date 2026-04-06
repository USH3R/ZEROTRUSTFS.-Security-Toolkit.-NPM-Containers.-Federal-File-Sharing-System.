# identity/auth_service.py

import hashlib

def authenticate_user(username, password, config):
    """
    Minimal authentication function.
    Checks username and password against settings.yaml.
    Passwords are stored as SHA256 hashes for demonstration.
    """
    users = config.get("users", {})
    
    if username not in users:
        return False
    
    stored_hash = users[username].get("password_hash")
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    
    return input_hash == stored_hash
