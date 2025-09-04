"""
Hash Table Implementation

A simple hash table implementation that uses separate chaining for collision resolution.
For this implementation, we use Python lists to handle collisions through chaining.
"""


class HashTable:
    """
    A simple Hash Table that maps keys to values.
    
    This implementation uses separate chaining (linked lists)
    to handle collisions.
    """
    
    def __init__(self, size=10):
        """
        Initialize a hash table with the given size.
        
        Args:
            size: Number of buckets in the hash table (default: 10)
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Create empty buckets

    def _hash_function(self, key):
        """
        Convert a key into an index in our table. Uses the built-in hash function in Python.
        
        Args:
            key: The key to hash (must be hashable)
            
        Returns:
            The bucket index for this key
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert or update a key-value pair in the hash table.
        
        Args:
            key: The key (must be hashable)
            value: The value to store
        """
        index = self._hash_function(key)
        
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Update existing key
                self.table[index][i] = (key, value)
                return
                
        # Key doesn't exist, add new pair
        self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieve a value by its key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key
            
        Raises:
            KeyError: If the key is not found
        """
        index = self._hash_function(key)
        
        # Search for the key in the bucket
        for k, v in self.table[index]:
            if k == key:
                return v
                
        # Key not found
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key: The key to delete
            
        Raises:
            KeyError: If the key is not found
        """
        index = self._hash_function(key)
        
        # Search for the key in the bucket
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                # Remove the key-value pair
                del self.table[index][i]
                return
                
        # Key not found
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """
        Check if a key exists in the hash table.
        
        Args:
            key: The key to check
            
        Returns:
            True if the key exists, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def __str__(self):
        """
        Return a string representation of the hash table.
        """
        return str(self.table)

    def __repr__(self):
        """
        Official string representation of the hash table.
        Shows key-value pairs in dictionary format.
        """
        pairs = []
        for bucket in self.table:
            for key, value in bucket:
                pairs.append(f"{repr(key)}: {repr(value)}")
        return f"HashTable({{{', '.join(pairs)}}})"


# Example usage
if __name__ == "__main__":
    # Create a hash table
    hash_table = HashTable(size=5)
    print("Empty hash table:", hash_table)
    
    # Insert key-value pairs
    print("\nInserting key-value pairs:")
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 25)
    hash_table.insert("city", "New York")
    print("Hash table after insertions:", hash_table)
    
    # Retrieve values
    print("\nRetrieving values:")
    print("name:", hash_table.get("name"))
    print("age:", hash_table.get("age"))
    
    # Update a value
    print("\nUpdating a value:")
    hash_table.insert("age", 26)
    print("Updated age:", hash_table.get("age"))
    
    # Check if keys exist
    print("\nChecking if keys exist:")
    print("Contains 'name':", hash_table.contains("name"))
    print("Contains 'email':", hash_table.contains("email"))
    
    # Handle collisions
    print("\nHandling collisions:")
    # These keys might cause collisions depending on the hash function
    hash_table.insert("country", "USA")
    hash_table.insert("language", "English")
    print("Hash table with potential collisions:", hash_table)
    
    # Delete a key-value pair
    print("\nDeleting a key-value pair:")
    hash_table.delete("city")
    print("After deleting 'city':", hash_table)
    
    # Try to access a non-existent key
    print("\nTrying to access a non-existent key:")
    try:
        hash_table.get("address")
    except KeyError as e:
        print("Error:", e)