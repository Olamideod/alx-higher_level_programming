#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Example usage:
my_list = [1, 2, 3, 4, 5]

# Retrieving elements at valid and invalid indices
print(element_at(my_list, 2))  # Should print 3
print(element_at(my_list, -1))  # Should print None (negative index)
print(element_at(my_list, 10))  # Should print None (out of range)

