from importlib import reload 
import programToRun as fp

#os.system('cls||clear')

title = " _____                         _                _   ___  ____   _____ \n|_   _|  ___  _ __  _ __ ___  (_) _ __    __ _ | | |_ _||  _ \ | ____|\n  | |   / _ \| '__|| '_ ` _ \ | || '_ \  / _` || |  | | | | | ||  _|  \n  | |  |  __/| |   | | | | | || || | | || (_| || |  | | | |_| || |___ \n  |_|   \___||_|   |_| |_| |_||_||_| |_| \__,_||_| |___||____/ |_____|\n                                                                      "

def intro():
  print(Fore.GREEN + title)
  print("-----------------------------")
  print("HOW TO USE:")
  print("\n-You specify the line to edit, add or create.\n-You can run the code, and then edit it again after\n-The program will help you if you are confused :)\n")
  input("PRESS ENTER TO CONTiNUE")
  os.system('cls||clear')

def editCode(maxLines, lines):

  while True:
    
    for x in range(maxLines):
      print (Fore.WHITE + f"{x+1}- {lines[x]}")
    print("\n")
  
    exitOption = input("Enter 'e' to run the program, enter any other characters\nto continue coding: ").lower()
    if exitOption == 'e':
      break
      
    while True:
      try:
        lineToEdit = int(input(("\nPlease enter the number of the line you wish to edit: ")) )
      except:
        print("Please enter a number...")
      else:
        break
      
  
    if lineToEdit > maxLines:
      maxLines = lineToEdit
  
    if lineToEdit > len(lines):
      for x in range(lineToEdit - len(lines)):
        lines.append("")
    
    newCode = input("\nPlease enter the new line of code:\n")
  
    lines[lineToEdit - 1] = newCode
    os.system('cls||clear')

  return maxLines, lines

def runCode(lines):

  programFile = open("programToRun.py", "w")
  
  programFile.write("def fileProgram():\n")
  for x in lines:
    programFile.write(f"  {x}\n")
  programFile.close()
  
  reload(fp)
  try:
    fp.fileProgram()
  except:
    print("Your code had an error in it :(")

while True:
  numOfLines = 1
  code = [""]
  intro()
  
  while True:
    
    numOfLines, code = editCode(numOfLines, code)
    os.system('cls||clear')
    runCode(code)
  
    if input("\n" + Fore.GREEN + "Type 'exit', to quit the ide, enter any other\ncharacter to continue: ").lower() == 'exit':
      os.system('cls||clear')
      break
    os.system('cls||clear')
