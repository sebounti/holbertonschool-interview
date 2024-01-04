# Lockboxes

## Description
In this project, we face an algorithmic challenge where we have a number `n` of locked boxes in front of us. Each box is numbered sequentially from 0 to `n - 1`. Each box may contain keys to open other boxes.

The goal is to write a method to determine if all the boxes can be opened.

## Method
`def canUnlockAll(boxes)`

- **Parameters**: `boxes`, a list of lists. Each sublist represents a box and contains keys to open other boxes.
- **Returns**: `True` if all boxes can be opened, else `False`.

## Rules
- A key with the same number as a box opens that box.
- All keys will be positive integers.
- There can be keys that do not have boxes.
- The first box (`boxes[0]`) is always unlocked.

## Usage
To use this method, import the `canUnlockAll` function from the `0-lockboxes` script. Then, you can test different sets of boxes to see if all can be opened.

### Example Usage
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
