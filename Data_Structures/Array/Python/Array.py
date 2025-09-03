"""
Unlike traditional arrays, this implementation uses a dictionary for storage, allowing for
dynamic resizing while maintaining O(1) access time.
"""

class Array:
    """
    A custom Array implementation using Python dictionaries.
    
    This implementation provides constant time access while allowing dynamic resizing.
    It uses a dictionary for internal storage where keys are indices and values are elements.
    
    Attributes:
        length (int): The number of elements in the array.
        data (dict): Dictionary storing the array elements with indices as keys.
    """
    
    def __init__(self):
        """
        Initialize an empty Array.
        
        The array starts with zero length and an empty dictionary for data storage.
        """
        self.length = 0
        self.data = {}

    def __str__(self):
        """
        Return a string representation of the Array.
        
        Returns:
            str: String representation of the array's internal state.
        """
        return str(self.__dict__)

    def get(self, index):
        """
        Retrieve an element at the specified index.
        
        Args:
            index (int): The index of the element to retrieve.
            
        Returns:
            The element at the specified index.
            
        Raises:
            KeyError: If the index is out of bounds.
        """
        return self.data[index]

    def push(self, item):
        """
        Add an element to the end (push) of the array.
        
        Args:
            item: The element to add to the array.
        """
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        """
        Remove and return the last element (pop) from the array.
        
        Returns:
            The last element of the array.
            
        Raises:
            KeyError: If the array is empty.
        """
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        """
        Delete an element at the specified index.
        
        This operation shifts all elements after the deleted element
        one position to the left to maintain array continuity.
        
        Args:
            index (int): The index of the element to delete.
            
        Returns:
            The deleted element.
            
        Raises:
            KeyError: If the index is out of bounds.
        """
        deleted_item = self.data[index]
        
        # Shift all elements to the left
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
            
        # Remove the last element
        del self.data[self.length - 1]
        self.length -= 1
        
        return deleted_item
    
    def insert(self, index, item):
        """
        Insert an element at the specified index.
        
        This operation shifts all elements at and after the specified index
        one position to the right, making space for the new element.
        
        Args:
            index (int): The index at which to insert the element.
            item: The element to insert.
            
        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index > self.length:
            raise IndexError("Array index out of bounds")
            
        # Shift all elements to the right
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
            
        # Insert the new element
        self.data[index] = item
        self.length += 1
    
    def search(self, item):
        """
        Search for an item in the array.
        
        Args:
            item: The item to search for.
            
        Returns:
            int: The index of the first occurrence of the item, or -1 if not found.
        """
        for i in range(self.length):
            if self.data[i] == item:
                return i
        return -1


# Example usage
if __name__ == "__main__":
    # Create an empty array
    print("Step 1: Creating new array")
    my_array = Array()
    print(f"Empty array: {my_array}")
    
    # Add elements using push 
    print("\nStep 2: Adding elements to the array")
    my_array.push("apple")
    my_array.push("banana")
    my_array.push("cherry")
    my_array.push("date")
    print(f"Array after pushing 4 elements: {my_array}")
    
    # Access elements for a specific index
    print("\nStep 3: Accessing elements")
    print(f"Element at index 0: {my_array.get(0)}")
    print(f"Element at index 2: {my_array.get(2)}")
    
    # Search for an element
    print("\nStep 4: Searching for elements")
    search_item = "banana"
    index = my_array.search(search_item)
    print(f"'{search_item}' found at index: {index}")
    
    search_item = "grape"
    index = my_array.search(search_item)
    print(f"'{search_item}' found at index: {index}")  # Should return -1
    
    # Insert an element at a specific position
    print("\nStep 5: Inserting an element")
    my_array.insert(2, "blueberry")
    print(f"Array after inserting 'blueberry' at index 2: {my_array}")
    
    # Delete an element
    print("\nStep 6: Deleting an element")
    deleted = my_array.delete(1)  # Delete 'banana'
    print(f"Deleted element: {deleted}")
    print(f"Array after deletion: {my_array}")
    
    # Pop the last element
    print("\nStep 7: Popping last element")
    popped = my_array.pop()
    print(f"Popped element: {popped}")
    print(f"Array after pop: {my_array}")
    
    # Show the internal structure 
    print("\nStep 8: Internal structure of the array")
    print(f"Length: {my_array.length}")
    print(f"Data dictionary: {my_array.data}")