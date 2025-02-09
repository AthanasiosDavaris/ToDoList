import json
from pathlib import Path
from platform import uname

#function that checks if task exists
def string_in_file(filename, string):
  print("3")
  for line in filename:
    print (line)
    print(filename)
    print("1")
    if string in line:
      print(string)
      print(line)
      print("2")
      return True
  
  print("4")
  return False

# opens file and checks for errors
try:
  tasks = open("Tasks.json", "a+")
except:
  print("An unexpected error occured.")
  exit()
  # following code is in development
  """
  error ={
    "ErrorType" : "FileError",
    "FileName" : "Tasks.json",
    "FilePath" : Path.cwd(),
    "SysInfo" : uname()
  }
  with open("ErrorLog.json", "w") as outfile:
    json.dump(error, outfile)
  """


# Start of the app and command prompt
print("Welcome to your ToDo list!")
while True:
  command = input("What do you want ToDo? ").lower()

  # Splits the command prompt
  splited_command = command.split()
  if not splited_command:
    print("You just gave an empty command (not cool XXX)")
    continue

  # Checks the command type
  if splited_command[0] == "add":
    # Checks if the task exists
    print(string_in_file(tasks, splited_command))
    if string_in_file(tasks, splited_command):
      print("Task already exists!")
      continue
    try:
      splited_command.remove("add")
      tasks.write(" ")
      tasks.write(''.join(s.replace('"', '') for s in splited_command))
      tasks.write(" False")
      for word in splited_command:
        print(word)
    except:
      print("The input format is wrong!")
  elif splited_command[0] == "update":
    # Checks if the task exists
    if not string_in_file:
      print("Task already exists!")
      continue

    # updates the task state
    splited_command.remove("update")
    taskname = ''.join(s.replace('"', '') for s in splited_command)
    filedata = tasks.read()
    filedata = filedata.replace(taskname + " False", taskname + " True")
    tasks.write(filedata)
  elif splited_command[0] == "delete":
    print("delete")
    try:
      pass
    except:
      pass
  elif splited_command[0] == "quit":
    tasks.close()
    break
  elif splited_command[0] == "list":
    print("list")
    try:
      pass
    except:
      pass
  elif splited_command[0] == "done_list":
    print("done_list")
    try:
      pass
    except:
      pass
  elif splited_command[0] == "not_done_list":
    print("not_done_list")
    try:
      pass
    except:
      pass
  elif splited_command[0] == "progress_list":
    print("progress_list")
    try:
      pass
    except:
      pass