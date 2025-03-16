class Node:
    """
    Represents an individual node in a linked data structure.
    Each node contains a value and a reference to the next node in the list.
    """
    def __init__(self, value):
        self.value = value  # Stores the value (URL, in this case)
        self.next = None  # Reference to the next node (initially None)

class NavigationHistory:
    """
    Implements a stack to manage navigation history.
    The behavior is LIFO (Last In, First Out), typical of stacks.
    """

    def __init__(self):
        """
        Initializes the navigation history.
        """
        self.top = None  # Reference to the top of the stack
        self.size = 0  # Number of elements in the stack

    def visit_page(self, url):
        """
        Adds a new page to the navigation history.
        
        Parameter:
        - url: The URL of the page to be added.
        """
        new_node = Node(url)  # Creates a new node with the provided URL
        new_node.next = self.top  # The next node of the new node is the current top
        self.top = new_node  # Updates the top to the new node
        self.size += 1  # Increments the size of the stack

    def go_back(self):
        """
        Removes and returns the current page from the top of the history.
        If there are no pages, returns an informational message.
        
        Return:
        - The URL of the removed page or a message if the stack is empty.
        """
        if self.is_empty():
            return "There are no more pages to go back."
        removed_value = self.top.value  # Stores the value of the top to return
        self.top = self.top.next  # Updates the top to the next node
        self.size -= 1  # Decrements the size of the stack
        return removed_value

    def is_empty(self):
        """
        Checks if the navigation history is empty.
        
        Return:
        - True if empty, False otherwise.
        """
        return self.top is None

    def current_page(self):
        """
        Returns the page at the top of the history without removing it.
        
        Return:
        - The URL of the current page or a message if the stack is empty.
        """
        if self.is_empty():
            return "There is no page to be viewed."
        return self.top.value

    def display_history(self):
        """
        Displays all pages in the history, starting from the most recent.
        """
        current = self.top  # Start from the top of the stack
        while current is not None:  # Iterates while there are nodes in the stack
            print(current.value)  # Displays the value of the current node
            current = current.next  # Moves to the next node
