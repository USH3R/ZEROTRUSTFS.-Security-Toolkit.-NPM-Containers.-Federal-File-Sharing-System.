# policy_evaluator.py

def check_policy(username, file_name, config):
    """
    Check if a user is allowed to access a specific file based on their role.
    
    Args:
        username (str): The name of the user trying to access the file.
        file_name (str): The name of the file to access.
        config (dict): The loaded settings.yaml dictionary.

    Returns:
        bool: True if the user is allowed, False otherwise.
    """
    # Lookup the user in the config
    user = config["users"].get(username)
    if not user:
        return False

    # Get the user's role
    role = user.get("role")

    # Option A: Use the "policies" key from settings.yaml
    file_permissions = config.get("policies", {})
    allowed_roles = file_permissions.get(file_name, [])

    # Return True if user's role is allowed for the requested file
    return role in allowed_roles# policy_evaluator.py

def check_policy(username, requested_file, config):
    """
    Minimal policy evaluation function.
    Returns True if the user has permission to access the requested file.
    Uses RBAC-like roles defined in settings.yaml.
    """
    users = config.get("users", {})
    if username not in users:
        return False
    
    role = users[username].get("role")
    file_permissions = config.get("file_permissions", {})
    
    # Get allowed roles for this file
    allowed_roles = file_permissions.get(requested_file, [])
    
    return role in allowed_roles
