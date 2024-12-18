def find_minimum(numbers: list) -> int:
    # Check if the list is empty.
    if not numbers:
        return None
    # Set smallest number with the first element of list.
    smallest_value = numbers[0]
    
    # Iterate through the list to find the minimum value
    for number in numbers:
        if number < smallest_value:
            # Update if the minimum number found.
            smallest_value = number
    # Return smallest number found in the list.
    return smallest_value