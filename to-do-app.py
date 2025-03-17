import os

TODO_FILE = 'to-do-app.txt'

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE,'r', encoding='utf-8') as file:
                tasks = [line.strip() for line in file]
        except Exception as e:
            print(f"Error:{e}")
    return tasks


def save_tasks(tasks):
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as file:
            file.write("\n".join(tasks))

    except Exception as e:
        print(f"Save Error: {e}")

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1. View tasks")
    print("2. New task")
    print("3. Complete")
    print("4. Delete")
    print("5. Log out")
    print("===============================")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = int(input("Choice (1-5): "))

        if choice == 1:
            print("Your TO-DO list")
            if not tasks:
                print("Nothing! Your diary is empty.")
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")

        elif choice == 2:
            new_task = input("\n Enter new task: ")
            tasks.append(f'[ ] {new_task}')
            print(f"{new_task} added!")


        elif choice == 3:
            try:
                task_num = int(input("Completed task number: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num] = tasks[task_num].replace("[ ]","[✔️]")
                    print("Completed! ✔️")
                else:
                    print("Not valid number")
            except ValueError:
                print("Enter a Number!")

        elif choice == 4:
            try:
                task_num = int(input("Delete task number: ")) - 1
                if 0 <= task_num < len(tasks):
                    remove = tasks.pop(task_num)
                    print(f"Deleted: {remove}")
                else:
                    print("Not valid number")
            except ValueError:
                print("Enter a number!")

        elif choice == 5:
            save_tasks(tasks)
            print("\nTasks saved. See you later! 👋")
            break
        else:
            print("Invalid selection! (1-5 only)")



if __name__ == "__main__":
    main()

