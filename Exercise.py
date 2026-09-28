#Balanced brackets
def is_balanced(s):
    stack = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if len(stack) == 0:
                return False
            last = stack.pop()
            if char == ")" and last != "(":
                return False
            if char == "]" and last != "[":
                return False
            if char == "}" and last != "{":
                return False
    return len(stack) == 0

print(is_balanced("(a[b]{c})"))
print(is_balanced("([)]"))
print(is_balanced("(("))

#Two sum

def two_sum(nums, target):
    numbers = {}
    for i in range(len(nums)):
        current = nums[i]
        needed = target - current
        if needed in numbers:
            return (numbers[needed], i)
        numbers[current] = i
    return (-1, -1)

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([1, 5, 3, 7], 10))

#Reverse linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    previous = None
    current = head
    while current != None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def print_list(head):
    current = head
    while current != None:
        print(current.value, end=" ")
        current = current.next
    print()

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
head = reverse_list(a)
print_list(head)

a = Node(5)
a.next = Node(10)
head = reverse_list(a)
print_list(head)

head = None
head = reverse_list(head)
print_list(head)

#Queue two stacks

class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        if len(self.out_stack) == 0:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

queue = QueueFromStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue = QueueFromStacks()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())

queue = QueueFromStacks()
try:
    print(queue.dequeue())
except IndexError as e:
    print(e)

# Validate tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    def check(node, low, high):
        if node == None:
            return True
        if node.value <= low or node.value >= high:
            return False
        if check(node.left, low, node.value) == False:
            return False
        if check(node.right, node.value, high) == False:
            return False
        return True
    return check(root, float("-inf"), float("inf"))

root = Node(5)
root.left = Node(2)
root.right = Node(8)
print(is_valid_bst(root))

root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.right.left = Node(4)
print(is_valid_bst(root))

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
print(is_valid_bst(root))
