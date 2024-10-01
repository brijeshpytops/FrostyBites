import uuid

def generatePrimaryKey(POSTFIX):
    """
    Generate a unique primary key string.

    The primary key is created by generating a UUID and appending a specified POSTFIX.

    Parameters:
    ----------
    POSTFIX : str
        A string to be appended to the generated UUID. This can be used to give context to the primary key.

    Returns:
    -------
    str
        A unique primary key string in the format: 'UUID_POSTFIX'.
    
    Example:
    --------
    >>> primary_key = generatePrimaryKey("user")
    >>> print(primary_key)
    '550e8400-e29b-41d4-a716-446655440000_user'
    """
    return str(uuid.uuid4()) + "_" + POSTFIX
