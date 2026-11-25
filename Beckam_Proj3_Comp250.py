# Beckam Potter
# Project 3: COMP 250

from collections import deque


class Node:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a student without allowing duplicate IDs
    def insert(self, student_id, name, major):
        new_node = Node(student_id, name, major)
        if self.root is None:
            self.root = new_node
            return True

        current = self.root
        while True:
            if student_id == current.student_id:
                return False
            if student_id < current.student_id:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right

    # Search and keep track of the IDs checked
    def search(self, student_id):
        current = self.root
        path = []
        while current is not None:
            path.append(current.student_id)
            if student_id == current.student_id:
                return current, path
            if student_id < current.student_id:
                current = current.left
            else:
                current = current.right
        return None, path

    # Root, left, right
    def pre_order(self, node):
        if node is not None:
            display_student(node)
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Left, root, right
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            display_student(node)
            self.in_order(node.right)

    # Left, right, root
    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            display_student(node)

    # Visit students one level at a time
    def bfs(self):
        if self.root is None:
            print("The tree is empty.")
            return
        queue = deque([self.root])
        level = 1
        while queue:
            level_size = len(queue)
            students = []
            for i in range(level_size):
                node = queue.popleft()
                students.append(f"{node.student_id} ({node.name}, {node.major})")
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            print(f"Level {level}: " + " | ".join(students))
            level += 1

    # Count every node recursively
    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    # Height is the number of levels
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def smallest(self):
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current

    def largest(self):
        current = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current


def display_student(node):
    print(f"ID: {node.student_id} | Name: {node.name} | Major: {node.major}")


# Make sure the user enters an integer
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")


def add_student(tree):
    student_id = get_int("Enter student ID: ")
    student, path = tree.search(student_id)
    if student is not None:
        print("A student with that ID already exists.")
        return
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    tree.insert(student_id, name, major)
    print("Student added successfully.")


def search_student(tree):
    if tree.root is None:
        print("The tree is empty. Student not found.")
        print("Search path: None")
        print("Nodes checked: 0")
        return
    student_id = get_int("Enter student ID: ")
    student, path = tree.search(student_id)
    if student is None:
        print("Student not found.")
    else:
        display_student(student)
    print("Search path: " + " -> ".join(str(student_id) for student_id in path))
    print(f"Nodes checked: {len(path)}")


def display_dfs(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    print("1. Pre-order")
    print("2. In-order")
    print("3. Post-order")
    while True:
        choice = get_int("Choose a traversal (1-3): ")
        if choice == 1:
            tree.pre_order(tree.root)
            return
        elif choice == 2:
            tree.in_order(tree.root)
            return
        elif choice == 3:
            tree.post_order(tree.root)
            return
        else:
            print("Please choose a number from 1 to 3.")


def display_bfs(tree):
    tree.bfs()


def display_stats(tree):
    if tree.root is None:
        print("The tree is empty.")
    print(f"Total students: {tree.count(tree.root)}")
    print(f"Tree height: {tree.height(tree.root)}")


def display_min_max(tree):
    if tree.root is None:
        print("The tree is empty.")
        return
    print("Student with the smallest ID:")
    display_student(tree.smallest())
    print("Student with the largest ID:")
    display_student(tree.largest())


def exit_program():
    print("Goodbye!")


def main():
    tree = BinarySearchTree()
    while True:
        print("\nStudent Directory")
        print("1. Add a new student")
        print("2. Search for a student")
        print("3. Display students using DFS")
        print("4. Display students using BFS")
        print("5. Display tree stats")
        print("6. Display smallest and largest IDs")
        print("7. Exit")
        choice = get_int("Choose an option (1-7): ")
        if choice == 1:
            add_student(tree)
        elif choice == 2:
            search_student(tree)
        elif choice == 3:
            display_dfs(tree)
        elif choice == 4:
            display_bfs(tree)
        elif choice == 5:
            display_stats(tree)
        elif choice == 6:
            display_min_max(tree)
        elif choice == 7:
            exit_program()
            break
        else:
            print("Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()


# Time Complexity Questions

# 1. When I added 50, 30, 70, 20, 40, 60, and 80, searching for 80 checked 3 nodes. The path was 50 -> 70 -> 80. When I restarted and added 10, 20, 30, 40, 50, 60, and 70, searching for 70 checked 7 nodes. The path was 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70. In a balanced tree, each comparison eliminates about half of the remaining nodes, so the worst-case search time is O(log n). In the unbalanced tree, each node has only a right child, so the search may have to check every node. The worst case is O(n).

# 2. Inserting one student into a balanced BST takes about log n steps because the height grows logarithmically. Building a tree of n students requires n insertions, each taking at most O(log n) steps if the tree stays balanced. This gives O(n log n) total. For 1,000 students, 1000 * log2(1000) is about 9,966 steps, or roughly 10,000 steps. This is a simplified estimate because the tree starts empty and earlier insertions take fewer steps.

