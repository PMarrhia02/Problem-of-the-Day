from typing import List

def show_menu():

  """Prints the available options in the main menu."""

  print("\n---- What do you want to do? ----")

  print("1. Add task")

  print("2. Remove task")

  print("3. Show all tasks")

  print("4. Exit")


def add_new_task(task_list: List[str]):

  """Prompts the user to add a task and appends it to the list.

  Args:

    task_list (List[str]): The current list of tasks.

  """

  new_task = input("Type the task to add: ").strip()

  if not new_task:

    print("Hmm, can't add an empty task. Try again.")

    return

  task_list.append(new_task)

  task_list.sort() 

  print(f"Added: '{new_task}'")


def delete_task(task_list: List[str]):

  """Prompts the user to remove a task and deletes it if found.

  Args:

    task_list (List[str]): The current list of tasks.

  """

  task_to_remove = input("Type the task you want gone: ").strip()

   
  if task_to_remove in task_list:

    task_list.remove(task_to_remove)

    print(f"Removed: '{task_to_remove}'")

  else:

    print(f"No task called '{task_to_remove}' was found.")



def list_tasks(task_list: List[str]):

  """Displays the current list of tasks in sorted order.



  Args:

    task_list (List[str]): The list of tasks to show.

  """

  if not task_list:

    print("Your list is currently empty.")

    return



  print("\nYour To-Do List:")

  sorted_tasks = sorted(task_list) 

  for i, task in enumerate(sorted_tasks):

    print(f"{i + 1}. {task}")





def run_app():

  """Runs the main loop of the To-Do application."""

  task_data = [] 

  while True:

    show_menu()

    option = input("Pick (1-4): ").strip()


    if option == "1":

      add_new_task(task_data)

    elif option == "2":

      delete_task(task_data)

    elif option == "3":

      list_tasks(task_data)

    elif option == "4":

      print("Exiting... catch you later.")

      break

    else:

      print("That doesn't look like a valid choice. Try 1 through 4.")



if __name__ == "__main__":

  run_app()

