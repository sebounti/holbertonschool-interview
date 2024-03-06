#!/usr/bin/env python3
"""
Main file for testing
"""
def validUTF8(data):
    """
    Method that determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes   = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return True
        else:
            if byte >> 6 != 2:
                return False
        num_bytes -= 1

        return num_bytes == 0
