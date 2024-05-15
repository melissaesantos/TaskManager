class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description, due_date):
        if title not in self.tasks:
            task = Task(title, description, due_date)
            self.tasks[title] = task
            print("Task added successfully!")
        else:
            print("Task with this title already exists.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for title, task in self.tasks.items():
                print(f"{title}: {task.description} (Due: {task.due_date}, Completed: {task.completed})")
        else:
            print("No tasks available.")

    def mark_task_as_complete(self, title):
        if title in self.tasks:
            self.tasks[title].completed = True
            print("Task marked as complete!")
        else:
            print("Task not found.")

    def delete_task(self, title):
        if title in self.tasks:
            del self.tasks[title]
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for title, task in self.tasks.items():
                file.write(f"{title},{task.description},{task.due_date},{task.completed}\n")

    def load_tasks(self, filename):
        self.tasks = {}
        with open(filename, 'r') as file:
            for line in file:
                title, description, due_date, completed = line.strip().split(',')
                task = Task(title, description, due_date)
                task.completed = completed == 'True'
                self.tasks[title] = task

def main():
    task_manager = TaskManager()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task_manager.add_task(title, description, due_date)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            title = input("Enter task title to mark as complete: ")
            task_manager.mark_task_as_complete(title)
        elif choice == '4':
            title = input("Enter task title to delete: ")
            task_manager.delete_task(title)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            task_manager.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks from: ")
            task_manager.load_tasks(filename)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()