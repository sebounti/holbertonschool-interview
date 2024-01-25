#!/usr/bin/python3
'''A minimal operations algorithm"'''


def minOperations(n):
    if n <= 1:
        return 0
    else:
        '''Iterate through numbers from 2 to n to find the smallest factor'''
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
