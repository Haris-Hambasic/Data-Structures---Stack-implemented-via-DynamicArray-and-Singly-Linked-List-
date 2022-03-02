# Name: Haris Hambasic
# OSU Email: hambasih@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 31 January 2022
# Description: Implementation of a dynamic array by using an underlying static array that grows and shrinks as required.

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self.index]
        except DynamicArrayException:
            raise StopIteration

        self.index = self.index + 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Generates a new dynamic array to accommodate insertion of new element
        when there is not enough allocated memory space in original element
        --> generated new dynamic array becomes new base array... replacing old array

        Args:
            new_capacity (int): the capacity for the newly generated dynamic array

        Return:
            None
        """
        if new_capacity <= 0 or new_capacity < self.length():
            return None
        elif new_capacity > 0 or new_capacity > self.length():
            # set new capacity
            self.capacity = new_capacity

            # copy over elements into new data storage array with new capacity
            new_data = StaticArray(new_capacity)
            for i in range(new_capacity):
                if i < self.length():
                    new_data._data[i] = self.get_at_index(i)
                else:
                    new_data.set(i, None)

            self.data = new_data
            return None


    def append(self, value: object) -> None:
        """
        Adds an element to the end of an array and increments the size
        of the array to reflect the added element

        Args:
            value (object): the element to add to the dynamic array

        Return:
            None
        """
        if self.length() == 0:
            self.data[0] = value

        if self.length() == self.capacity:
            self.resize(self.capacity * 2)
            self.data[self.length()] = value
            self.size += 1
        else:
            self.data[self.size] = value
            self.size += 1

        return None


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts an element into an array at a specified index and
        increments the size of the array to reflect the change

        Args:
            index (int)     : the index to insert the new element
            value (object)  : the new element to insert

        Return:
            None
        """
        if index < 0 or index > self.length():
            raise DynamicArrayException

        if self.length() == self.capacity:
            self.resize(self.capacity * 2)
        
        new_data = StaticArray(self.capacity)

        # handle copying old elements up to where new element is to be inserted
        for i in range(index):
            new_data._data[i] = self.data[i] # copy element from old array into new array

        # handle actual insertion of new element
        new_data._data[index] = value

        # handle copy remaining elements of old array into new array
        for j in range(index + 1, self.length() + 1):
            new_data._data[j] = self.data[j - 1]

        self.data = new_data._data
        self.size = self.size + 1

        return None


    def remove_at_index(self, index: int) -> None:
        """
        Removes an element from an array and decrements the size
        of the array to reflect the removed element

        Args:
            index (int): the element to remove from the dynamic array

        Return:
            None
        """
        # if index < 0 or index > self.size - 1:
        if index < 0 or index >= self.length():
            raise DynamicArrayException

        # handle handling a 'pop' at the end of the array
        if index == self.length():
            self.insert_at_index(index, None)
        
        # handle removing element that is not the last element
        else:
            # create temporary new data storage array
            temo_data = StaticArray(self.capacity)

            # handle copying old elements up to where element is to be deleted lives
            for i in range(index):
                temo_data.set(i, self.get_at_index(i))

            # handle copy remaining elements of old array into new array
            for j in range(index + 1, self.length()):
                temo_data.set(j - 1, self.get_at_index(j))

            self.data = temo_data._data

        # handle reducing size of array if array is strictly less than 1/4 size of capacity
        # new capacity must be reduced to twice the number of current elements
        if self.capacity > 10:
            if self.length() < (.25 * self.capacity):
                self.capacity = self.length() * 2
                if self.capacity < 10:
                    self.capacity = 10

        self.size = self.length() - 1

        return None


    def slice(self, start_index: int, size: int) -> object:
        """
        Generates a new dynamic array by extracting a specified number 
        of elements from the original array

        Args:
            start_index (int): the index of the first element to extract for the new dynamic array
            size        (int): the number of elements to extract from the original array

        Return:
            A newly generated dynamic array with a portion of extracted elements from the original array
        """
        if start_index < 0 or start_index >= self.length():
            raise DynamicArrayException

        if size < 0:
            raise DynamicArrayException

        # not enough elements between start_index and end of array to make slice of correct size
        if self.length() - start_index < size:
            raise DynamicArrayException

        new_data = DynamicArray()

        # handle slicing
        for i in range(0, size):
            # new_data.data[i] = self.data[start_index]
            new_data.append(self.data[start_index])
            # new_data.size = new_data.size + 1
            start_index = start_index + 1

        return new_data

    def merge(self, second_da: object) -> None:
        """
        Performs a union of two dynamic arrays

        Args:
            second_da (object): an array to merge with the base array

        Return:
            None (base array contains elements as a result of the merge)
        """
        for i in range(second_da.length()):
            self.append(second_da.data[i])

        return None

    def map(self, map_func) -> object:
        """
        Invokes a function on each element of the base array and
        stores the return value of that function as the new value
        for the element

        Args:
            map_func (function): the function to invoke on each element
                                 in the base array

        Return:
            A newly generated dynamic array with elements corresponding
            to elements computed by the invocation of 'map_func' on each
            element in the base array
        """
        new_data = DynamicArray()

        for i in range(self.length()):
            new_datum = map_func(self.get_at_index(i))
            new_data.append(new_datum)

        return new_data

    def filter(self, filter_func) -> object:
        """
        Invokes a function on each element in the base array and removes
        elements in the base array for which the function returns false
        when invoked with the element as input

        Args:
            filter_func (function): the function to invoke on each element
                                    in the base array

        Return:
            A newly generated dynamic array with elements that resulted in
            the return value of True when the element was supplied as input
            to 'filter_func'
        """
        new_data = DynamicArray()

        for i in range(self.length()):
            if filter_func(self.get_at_index(i)) == True:
                new_data.append(self.get_at_index(i))

        return new_data

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Invoke a function on each element in the base array and
        merge the return value of the function invocation with the
        running return value of the function's invocation on 
        elements at indices less than the current index

        Args:
            reduce_funct    (function)  : the function to invoke for each element
                                          in the base array
            initializer     (*)     : the starting running value

        Return:
            A value that corresponds to user defined merging of a
            value computer by 'reduce_func' and the current running
            value
        """
        if self.length() == 0:
            if initializer is None:
                return None
            return initializer

        reduce_start_index = 1
        if initializer is None:
            initializer = self.get_at_index(0)
        else:
            reduce_start_index = 0

        for i in range(reduce_start_index, self.length()):
            initializer = reduce_func(initializer, self.get_at_index(i))

        return initializer

def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Returns a tuple containing a dynamic array comprising the mode values
    in the array and an integer that represents the highest frequency

    Args:
        arr (DynamicArray): The dynamic array for which to compute the mode

    Return:
        A tuple where the first element is a dynamic array with elements that
        represents the mode, and the second element is an integer representing
        the frequency of occurence of the mode
    """
    frequency = 1
    new_data = DynamicArray()

    if arr.length() == 1:
        new_data.append(arr.get_at_index(0))
        return (new_data, frequency)

    index = 1
    current_element = arr.get_at_index(0)
    current_element_frequency = 1
    while index < arr.length():
        next_element = arr.get_at_index(index)

        if next_element != current_element:
            new_data.append((current_element, current_element_frequency))
            current_element = next_element
            current_element_frequency = 0

        current_element_frequency = current_element_frequency + 1
        if index == arr.length() - 1:
            new_data.append((current_element, current_element_frequency))
        
        index = index + 1

    # determine highest frequency
    for i in range(new_data.length()):
        frequency_checking = new_data.get_at_index(i)[1]

        if frequency_checking > frequency:
            frequency = frequency_checking

    # generate array with highest frequency items
    final_data = DynamicArray()
    i = 0
    while i < new_data.size:
        current_element = new_data.get_at_index(i)[0]
        frequency_checking = new_data.get_at_index(i)[1]
        if frequency_checking == frequency:
            final_data.append(current_element)
        i = i + 1

    return (final_data, frequency)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)


    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 4, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot", "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
