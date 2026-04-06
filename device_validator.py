# device_validator.py

def validate_device(username, device_id, config):
    """
    Minimal device/context validation.
    Returns True if device_id is listed for the user in settings.yaml.
    If device checking is not configured, defaults to True.
    """
    device_config = config.get("devices", {})
    
    # If no devices configured, skip check
    if not device_config:
        return True
    
    user_devices = device_config.get(username, [])
    return device_id in user_devices
