#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n
    'H' characters in the file.

    The function works by finding the smallest factor of 'n' (other than 1) and
      then
    recursively applying the same logic to the quotient of 'n' divided by this
    factor.
    This represents the 'Copy All' and 'Paste' operations.

    Args:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations required to achieve exactly n 'H'
    characters.
    If n is 1 or less, which is trivially achieved, returns 0.
    """

    # If n is 1 or less, no operations are needed as we start with one 'H'
    if n <= 1:
        return 0
    else:
        # Iterate through numbers from 2 to n to find the smallest factor
        for i in range(2, n + 1):
            # If i is a factor of n
            if n % i == 0:
                ''' Recursively call minOperations on the quotient n/i
             Add i to the result which represents the 'Copy All'(1 operation)
             and 'Paste' (i - 1 operations) to achieve n 'H's '''

                return minOperations(n // i) + i

        ''' In case n is a prime number, it requires n operations
        (one 'Copy All' and n-1 'Pastes')'''
        return n
