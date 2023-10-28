#!/usr/bin/python3
"""
given a numver of boxes
 determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    canUnlockAll determines if all the boxes can be opened.
    :param boxes: List of boxes, where each box is
        represented by a list of indices.
    :return: True if all boxes can be unlocked, False otherwise.
    """

    # Get the total number of boxes
    num_boxes = len(boxes)

    # Initialize a set to keep track of unlocked_boxes
    # and a set for locked_boxes
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]) - {0}

    # While there are locked boxes
    while locked_boxes:
        # Get the next locked box to explore
        next_locked_box = locked_boxes.pop()

        # Check if the box index is valid
        if next_locked_box < 0 or next_locked_box >= num_boxes:
            continue

        # If the box hasn't been unlocked before,
        # add it to the unlocked set
        if next_locked_box not in unlocked_boxes:
            locked_boxes.update(boxes[next_locked_box])
            unlocked_boxes.add(next_locked_box)

    # Check if all boxes have been unlocked
    return len(unlocked_boxes) == num_boxes
