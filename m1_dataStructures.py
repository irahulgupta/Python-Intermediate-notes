#---------------------------------------------
#Data Structures 
#----------------------------------------------
from collections import Counter, defaultdict, deque
print("MODULE 1 HANDS-ON: DATA PROCESSING UTILITY")
print("-" * 50)
# --------------------------------------------------
# PART 1: Lists and Tuples
# --------------------------------------------------
print("\n1. LISTS AND TUPLES")

students_list = [
    ["S101", "Rahul", "Python"],
    ["S102", "Anita", "Data Science"],
    ["S103", "John", "Python"],
    ["S104", "Priya", "Web Development"]
]
lab_info_tuple = ("Lab-A", "Batch-1", 25)

print("\nStudent Records (List):")
for student in students_list:
    print(student)

print("\nLab Information (Tuple):")
print(lab_info_tuple)

print("\nAccessing specific elements:")
print("First student name:", students_list[0][1])
print("Lab room:", lab_info_tuple[0])

# --------------------------------------------------
# PART 2: Dictionaries and Sets
# --------------------------------------------------
print("\n2. DICTIONARIES AND SETS")

student_dict = {
    "S101": "Rahul",
    "S102": "Anita",
    "S103": "John",
    "S104": "Priya"
}

courses_list = ["Python", "Data Science", "Python", "Web Development", "Python"]
unique_courses = set(courses_list)

print("\nStudent Dictionary:")
for student_id, name in student_dict.items():
    print(student_id, "->", name)

print("\nOriginal Courses List:")
print(courses_list)

print("\nUnique Courses (Set):")
print(unique_courses)

# --------------------------------------------------
# PART 3: Stack
# --------------------------------------------------
print("\n3. STACK IMPLEMENTATION")

action_stack = []

action_stack.append("Login")
action_stack.append("Open File")
action_stack.append("Run Program")

print("\nStack after push operations:")
print(action_stack)

last_action = action_stack.pop()
print("Popped from stack:", last_action)

print("Stack after pop:")
print(action_stack)

# --------------------------------------------------
# PART 4: Queue
# --------------------------------------------------
print("\n4. QUEUE IMPLEMENTATION")

support_queue = deque()

support_queue.append("Request 1 - Password Reset")
support_queue.append("Request 2 - Lab Access")
support_queue.append("Request 3 - Software Install")

print("\nQueue after enqueue operations:")
print(support_queue)

served_request = support_queue.popleft()
print("Dequeued from queue:", served_request)

print("Queue after dequeue:")
print(support_queue)

# --------------------------------------------------
# PART 5: Linked List
# --------------------------------------------------
print("\n5. LINKED LIST IMPLEMENTATION")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

module_list = LinkedList()
module_list.append("Module 1")
module_list.append("Module 2")
module_list.append("Module 3")

print("\nLinked List Content:")
module_list.display()

# --------------------------------------------------
# PART 6: Collections Module
# --------------------------------------------------
print("\n6. COLLECTIONS MODULE")

course_counter = Counter(courses_list)
print("\nCounter Result:")
print(course_counter)

grouped_students = defaultdict(list)
grouped_students["Python"].append("Rahul")
grouped_students["Python"].append("John")
grouped_students["Data Science"].append("Anita")
grouped_students["Web Development"].append("Priya")

print("\nDefaultdict Result:")
for course, names in grouped_students.items():
    print(course, "->", names)

recent_tasks = deque(["Task 1", "Task 2", "Task 3"])
recent_tasks.appendleft("Task 0")
recent_tasks.append("Task 4")

print("\nDeque Result:")
print(recent_tasks)

print("\nLab completed successfully.")

