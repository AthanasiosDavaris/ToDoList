import json
from pathlib import Path
from platform import uname


# opens file and checks for errors
try:
  tasks = open("Tasks.json", "r+")
except:
  print("An unexpected error occured.")
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
  command_split = command.split()
  if not command_split:
    print("You just gave an empty command (not cool XXX)")
    continue

  # Checks the command type
  if command_split[0] == "add":
    print("add")
  elif command_split[0] == "update":
    print("update")
  elif command_split[0] == "delete":
    print("delete")
  elif command_split[0] == "quit":
    print("quit")
  elif command_split[0] == "list":
    print("list")
  elif command_split[0] == "done_list":
    print("done_list")
  elif command_split[0] == "not_done_list":
    print("not_done_list")
  elif command_split[0] == "progress_list":
    print("progress_list")