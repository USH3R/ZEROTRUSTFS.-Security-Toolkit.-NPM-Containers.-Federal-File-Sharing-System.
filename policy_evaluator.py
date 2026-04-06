# policy_evaluator.py

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
