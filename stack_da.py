# Name: Haris Hambasic
# OSU Email: hambasih@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 7 February 2022
# Description: Implementation of a stack ADT via a dynamic array data structure


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack

        Args:
            value (object): the value to add

        Return:
            None
        """   
        self._da.append(value)

        return None

    def pop(self) -> object:
        """
        Removes and returns the top element of the stack
        Args:
            n/a

        Return:
            1) The top element of the stack
            2) StackException: if there are no elements in the stack
        """   
        index = self._da.length() - 1

        if index < 0:
            raise StackException

        popped_value = self._da.get_at_index(index)
        self._da.remove_at_index(index)

        return popped_value

    def top(self) -> object:
        """
        Returns the top element of the stack without removing it

        Args:
            n/a

        Return:
            1) The top element of the stack
            2) StackException: if the stack is empty
        """   
        if self.is_empty():
            raise StackException

        top_item = self._da.get_at_index(self._da.length() - 1)

        return top_item


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
