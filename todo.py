file_name = "tasks.txt"

# This loads the list from file 
def load_tasks():
  try:
    with open(file_name, "r") as file:
      tasks = [task.strip() for task in file.readlines()]
  except FileNotFoundError:
    tasks = [] # if there is not list, then we create empty list
  return tasks


# Save Tasks to file
def save_tasks(tasks):
  with open(file_name, "w") as file:
    for task in tasks:
      file.write(task + "\n")

# Add task to list
def add_task(tasks):
  task = input("Enter the task: ")
  tasks.append(task)
  print(f"{task} added.")

# View Tasks loaded from file
def view_tasks(tasks):
  if not tasks:
    print("No tasks in the list.")
  else:
    print("Your tasks.")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")
  
# Delete task - if valid delete - otherwise - invalid number
def delete_task(tasks):
  view_tasks(tasks)
  if tasks:
    try:
      num_delete = int(input("Enter a number to delete: "))
      if 1 <= num_delete <= len(tasks):
        deleted = tasks.pop(num_delete - 1)
        print(f"'{deleted}' task deleted.")
      else:
        print("Invalid task number. Can't Delete.")
      print(tasks)
    except ValueError:
      print("Only use numbers, not string.")


# Main Program

tasks = load_tasks()

while True:
  print("To Do List.")
  print("1. View Tasks.")
  print("2. Add Tasks.")
  print("3. Delete Tasks.")
  print("4. Exit.")

  choice = input("Enter a number (1 - 4): ")

  if choice == "1":
    view_tasks(tasks)
  elif choice == "2":
    add_task(tasks)
    save_tasks(tasks)
  elif choice == "3":
    delete_task(tasks)
    save_tasks(tasks)
  elif choice == "4":
    print("Exitting To do list.")
    break
  else:
    print("Enter a valid number from 1 to 4.")



