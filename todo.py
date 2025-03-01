class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name):
        """Add a new task to the list."""
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' added successfully.")
        else:
            print(f"Task '{task_name}' already exists.")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for task, status in self.tasks.items():
                status_str = "Completed" if status else "Not Completed"
                print(f"- {task}: {status_str}")

    def complete_task(self, task_name):
        """Mark a task as completed."""
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def delete_task(self, task_name):
        """Remove a task from the list."""
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo.add_task(task_name)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_name = input("Enter task name to complete: ")
            todo.complete_task(task_name)
        elif choice == "4":
            task_name = input("Enter task name to delete: ")
            todo.delete_task(task_name)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
