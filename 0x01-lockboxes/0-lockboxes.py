#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize a list to keep track of the boxes that we have opened
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True # the first box is already opened
    
    # Initialize a list to keep track of the keys that we have collected
    key_ring = boxes[0]
    
    # Keep trying to open more boxes as long as we have new keys
    while key_ring:
        # Get the next key from the key ring
        key = key_ring.pop(0)
        
        # Check if the key opens a new box
        if not opened_boxes[key]:
            # Add the new key to our key ring
            key_ring.extend(boxes[key])
            
            # Mark the new box as opened
            opened_boxes[key] = True
    
    # Check if all boxes have been opened
    return all(opened_boxes)
