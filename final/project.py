import sys
import os


tasks = []

def main():
    while True:
        print("To-Do List Menu")
        print("1- View Your List")
        print("2- Add To List")
        print("3- Remove From List")
        print("4- EXIT")


        try:
            choice = int(input("Choose an option: ").strip())
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            view(tasks)
        elif choice == 2:
            name = input("Enter the task name: ")
            add(name, tasks)
        elif choice == 3:
            try:
                number = int(input("Enter the task number to delete: "))
                remove(number, tasks)
            except:
                print("Please enter a valid item number.")
        elif choice == 4:
            print("Bye Bye...")
            sys.exit(1)


def add(name, tasks):
    task = {"id": len(tasks) + 1, "name": name}
    tasks.append(task)


def remove(number, tasks):
    try:
        for x in tasks:
            if x["id"] == number:
                tasks.remove(x)

                for i, s in enumerate(tasks):
                    s["id"] = i+1
    except:
        print("Coulnd't find the task")



def view(tasks):

    if not tasks:
        print("There are no tasks yet.")

    else:
        for task in tasks:
            print(f"{task['id']}, {task['name']}")
    
    return tasks


if __name__ == "__main__":
    main()