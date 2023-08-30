class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{idx}. {task.name} - {task.description} ({status})")

    def complete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            task = self.tasks[task_idx - 1]
            task.complete()
            print(f"Task '{task.name}' marked as completed.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task = Task(name, description)
            task_manager.add_task(task)
            print("Task added.")

        elif choice == '2':
            task_manager.list_tasks()

        elif choice == '3':
            task_manager.list_tasks()
            task_idx = int(input("Enter the index of the task to complete: "))
            task_manager.complete_task(task_idx)

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
