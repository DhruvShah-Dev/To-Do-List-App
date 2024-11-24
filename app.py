# Initialize an empty list to store tasks
tasks = []

# File where tasks will be saved
TASKS_FILE = "tasks.txt"

# Function to add tasks to the list
def add_task():
    """Prompts the user to enter a task and adds it to the tasks list."""
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to display all tasks
def display_tasks():
    """Displays all tasks currently in the tasks list."""
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to delete a task
def delete_task():
    """Prompts the user to select a task to delete by its number."""
    display_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Function to save tasks to a file
def save_tasks():
    """Saves all tasks in the tasks list to a text file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved!")

# Function to load tasks from a file
def load_tasks():
    """Loads tasks from a text file into the tasks list."""
    try:
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                tasks.append(line.strip())  # Strip to remove newlines
    except FileNotFoundError:
        print("No saved tasks found, starting with an empty list.")

# Function to display the menu options
def show_menu():
    """Displays the main menu options for the user."""
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# Main loop to interact with the user
def main():
    """Main function that controls the flow of the To-Do List app."""
    load_tasks()  # Load tasks when the app starts
    
    while True:
        show_menu()
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            save_tasks()  # Save tasks when exiting
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# Start the app
if __name__ == "__main__":
    main()