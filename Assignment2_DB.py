#Task 5
print("Task 5:")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(has_cycle(a))

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = b
print(has_cycle(a))

a = Node(1)
a.next = a
print(has_cycle(a))

#Task 6
print("Task 6:")
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def get_min(self):
        if len(self.min_stack) == 0:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]

stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
print(stack.get_min())
stack.pop()
print(stack.get_min())

stack = MinStack()
stack.push(10)
stack.push(4)
stack.push(7)
print(stack.top())
print(stack.get_min())

stack = MinStack()
stack.push(8)
stack.push(6)
stack.push(4)
print(stack.get_min())
stack.pop()
print(stack.get_min())

#Task 7
print("Task 7:")

class DynamicArray:
    def __init__(self):
        self.array = [None, None]
        self.size = 0
        self.capacity = 2

    def append(self, x):
        if self.size == self.capacity:
            new_array = [None] * (self.capacity * 2)
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = self.capacity * 2
        self.array[self.size] = x
        self.size = self.size + 1

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        return self.array[i]
    
    def set(self, i, x):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        self.array[i] = x

a = DynamicArray()
a.append(10)
a.append(20)
a.append(30)
print(a.get(0))
print(a.get(1))
print(a.get(2))

a.append(40)
print(a.size)
print(a.capacity)

a.set(1, 99)
print(a.get(1))

#Task 9
print("Task 9: ")
def search_range(nums, target):
    left = 0
    right = len(nums) - 1
    first = -1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            first = middle
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    left = 0
    right = len(nums) - 1
    last = -1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            last = middle
            left = middle + 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return (first, last)

numbers = [5, 7, 7, 8, 8, 8, 10]
print(search_range(numbers, 8))
print(search_range(numbers, 7))
print(search_range(numbers, 6))