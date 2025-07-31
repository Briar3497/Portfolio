todo_list = []

while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  
  choice = input()
  if choice == "1":
    new_task = input("Enter the task you would like to add\n")
    todo_list.append(new_task)
    print("Task added!")
  elif choice == "2":
    if not todo_list:
      print("Your ToDo list is empty")
    elif len(todo_list) > 1:
      pop_num = int(input('What number would you like to remove?\n'))
      todo_list.pop(pop_num - 1)
    else:
      todo_list.pop()
  elif choice == "3":
    print("Quitting")
    break
