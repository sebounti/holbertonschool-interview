#!/usr/bin/python3

''' rain module'''

def rain(walls):
    """
    Calculate the amount of rainwater trapped after it rains given the heights.

    Parameters:
        walls (list of int): A list of non-negative integers

    Returns:
        int: The total amount of rainwater retained.
    """
    if not walls:
        return 0

    n = len(walls)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n
    water_trapped = 0

    # Fill max_left array
    max_left[0] = walls[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], walls[i])

    # Fill max_right array
    max_right[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], walls[i])

    # Calculate trapped water
    for i in range(n):

        water_trapped += min(max_left[i], max_right[i]) - walls[i]

    return water_trapped
