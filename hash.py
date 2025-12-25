# BLAKE2b implementation:

import hashlib
import base64

def blake2b(input_, bits):
    try:
        if not isinstance(bits, int):
            raise ValueError("The 'bits' parameter must be an integer.")
        if bits % 8 != 0 or bits <= 0:
            raise ValueError("The 'bits' parameter must be a positive multiple of 8.")
        
        string_ = str(input_)
        blake2b = hashlib.blake2b(digest_size=(bits // 8))
        blake2b.update(string_.encode())

        # Return the hash encoded in base64
        return base64.b64encode(blake2b.digest()).decode()
    
    except Exception as e:
        # Handle exceptions and return an error message
        return f"Error: {str(e)}"
