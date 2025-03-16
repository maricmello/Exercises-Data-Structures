class Node:
    """
    Class that represents a node in a linked structure.
    Each node contains a value and a reference to the next node.
    """
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None  # Reference to the next node (initially None)


class Hybrid:
    """
    Class that implements a hybrid structure, functioning as:
    - Stack (LIFO - Last In, First Out)
    - Queue (FIFO - First In, First Out)
    """
    def __init__(self, type):
        """
        Initializes the hybrid structure.

        Parameter:
        - type: Must be "queue" or "stack", indicating the desired behavior.
        """
        self.type = type  # Defines whether the structure is a stack or a queue
        if type not in ["queue", "stack"]:
            raise ValueError("Error: the type must be 'queue' or 'stack'.")
        
        self.front = None  # Reference to the first element of the structure
        self.rear = None  # Reference to the last element (used only in the queue)
        
        if self.type == "stack":
            self.size = 0  # Used only in the stack to track the size

    def add(self, value):
        """
        Adds a new element to the structure.

        Parameter:
        - value: The value to be added.
        """
        new_node = Node(value)  # Creates a new node with the given value
        if self.type == "stack":  # Stack behavior (LIFO)
            new_node.next = self.front  # The next node of the new node will be the current top
            self.front = new_node  # Updates the top to the new node
            self.size += 1  # Increments the size of the stack
        else:  # Queue behavior (FIFO)
            if self.is_empty():  # Special case: empty queue
                self.front = new_node  # The new node will be the first node
                self.rear = new_node  # The new node will also be the last node
            else:
                self.rear.next = new_node  # Adds the new node to the end of the queue
                self.rear = new_node  # Updates the reference to the last node

    def remove(self):
        """
        Removes and returns the element at the front of the structure.

        Return:
        - Removed value or None if the structure is empty.
        """
        if self.is_empty():  # Checks if the structure is empty
            return None
        
        removed_value = self.front.value  # Stores the value of the element to be removed
        self.front = self.front.next  # Moves the front reference to the next node

        if self.type == "stack":  # Stack behavior (LIFO)
            self.size -= 1  # Decreases the size of the stack
            return removed_value
        else:  # Queue behavior (FIFO)
            if self.front is None:  # Special case: queue becomes empty after removal
                self.rear = None  # Removes the reference to the last node
            return removed_value

    def is_empty(self):
        """
        Checks if the structure is empty.

        Return:
        - True if the structure is empty, False otherwise.
        """
        return self.front is None

    def view_first_element(self):
        """
        Returns the element at the top (stack) or at the front (queue) without removing it.

        Return:
        - Value of the first element or informative message if empty.
        """
        if self.is_empty():  # Checks if the structure is empty
            return "There is no element."
        return self.front.value  # Returns the value of the element at the front


# Example of usage as a STACK
hybrid = Hybrid("stack")  # Creates a structure of type stack
hybrid.add(1)  # Adds element 1 to the top of the stack
hybrid.add(2)  # Adds element 2 to the top of the stack
hybrid.add(3)  # Adds element 3 to the top of the stack
hybrid.remove()  # Removes the element from the top (3)
hybrid.remove()  # Removes the element from the top (2)
print(f"Stack: the top element is {hybrid.view_first_element()}")  # Shows the remaining element at the top (1)

# Example of usage as a QUEUE
hybrid = Hybrid("queue")  # Creates a structure of type queue
hybrid.add(1)  # Adds element 1 to the queue
hybrid.add(2)  # Adds element 2 to the queue
hybrid.add(3)  # Adds element 3 to the queue
hybrid.remove()  # Removes the element at the front of the queue (1)
hybrid.remove()  # Removes the next element at the front of the queue (2)
print(f"Queue: the front element is {hybrid.view_first_element()}")  # Shows the remaining element at the front (3)
