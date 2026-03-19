# BLAKE2b implementation:

import hashlib
import base64
import argparse


def blake2b(input_, bits=256):
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


def main():
    parser = argparse.ArgumentParser(description="Generate BLAKE2b hash.")
    parser.add_argument("input_", type=str, help="Input string to hash")

    # Parse the arguments
    args = parser.parse_args()

    # Call the blake2b function and print the result
    result = blake2b(args.input_)
    print(result)


if __name__ == "__main__":
    main()
