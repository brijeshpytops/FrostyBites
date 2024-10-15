import random

def generate_otp(length=6):
    """
    Generates a random OTP of the specified length.
    
    Args:
        length (int): The length of the OTP to generate. Default is 6.
    
    Returns:
        str: A randomly generated OTP as a string.
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])
