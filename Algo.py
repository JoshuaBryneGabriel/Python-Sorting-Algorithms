class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print("Choose a data structure or algorithm to use:")
    print("1. Stack")
    print("2. Queue")
    print("3. Binary Search")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        stack = Stack()
        while True:
            print("\nStack Operations:")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Size")
            print("5. Exit")
            operation = input("Enter the number of your operation: ")

            if operation == '1':
                item = input("Enter the item to push: ")
                stack.push(item)
                print(f"Pushed {item} onto the stack.")
            elif operation == '2':
                item = stack.pop()
                if item is not None:
                    print(f"Popped {item} from the stack.")
                else:
                    print("Stack is empty.")
            elif operation == '3':
                item = stack.peek()
                if item is not None:
                    print(f"Top of the stack: {item}")
                else:
                    print("Stack is empty.")
            elif operation == '4':
                print(f"Stack size: {stack.size()}")
            elif operation == '5':
                break
            else:
                print("Invalid operation. Please try again.")

    elif choice == '2':
        queue = Queue()
        while True:
            print("\nQueue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Size")
            print("4. Exit")
            operation = input("Enter the number of your operation: ")

            if operation == '1':
                item = input("Enter the item to enqueue: ")
                queue.enqueue(item)
                print(f"Enqueued {item} into the queue.")
            elif operation == '2':
                item = queue.dequeue()
                if item is not None:
                    print(f"Dequeued {item} from the queue.")
                else:
                    print("Queue is empty.")
            elif operation == '3':
                print(f"Queue size: {queue.size()}")
            elif operation == '4':
                break
            else:
                print("Invalid operation. Please try again.")
    elif choice == '3':
        arr = input("Enter a sorted list of numbers separated by spaces: ").split()
        arr = list(map(int, arr))
        target = int(input("Enter the number to search for: "))
        index = binary_search(arr, target)
        if index != -1:
            print(f"Number {target} found at index {index}.")
        else:
            print(f"Number {target} not found in the list.")
    else:
        print("Invalid choice. Please restart the program and choose a valid option.")
