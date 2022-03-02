# Name: Haris Hambasic
# OSU Email: hambasih@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 7 February 2022
# Description: Implementation of a stack ADT via a singly linked list data structure

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self.head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack

        Args:
            value (object): the value to add

        Return:
            None
        """   
        
        new_node = SLNode(value, None)

        if self.is_empty():
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        
        return None

    def pop(self) -> object:
        """
        Removes and returns the top element of the stack

        Args:
            n/a

        Return:
            1) The top element of the stack
            2) StackException: if the stack is empty
        """   
        if self.is_empty():
            raise StackException

        popped_value = self.head.value

        self.head = self.head.next

        return popped_value

    def top(self) -> object:
        """
        Returns the value at the top of the stack, without removing it

        Args:
            n/a

        Return:
            1) The value at the top of the stack
            2) StackException: if the stack is empty
        """   
        if self.is_empty():
            raise StackException

        top_of_stack = self.head.value

        return top_of_stack

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
