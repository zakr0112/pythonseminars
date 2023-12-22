#  This masks an input with a character (*)
import pwinput 



def menu():
  print("==================")
  print("=     Options    =")
  print("==================")
  print("1: Add User")
  print("2: Delete User")
  print("3: Change Password")
  print("4: Login")
  print("q: quit")
  print("==================")
  menuEntry = input("Enter option: ")
  if menuEntry == "1":
    print()
    addUser()
  if menuEntry == "2":
    print()
    deleteUser()
  if menuEntry == "3":
    print()
    changePassword()
  if menuEntry == "4":
    print()
    login()
  if menuEntry == "q":
    quit()
  menu()
  

def rot13(password):  #Rotate 13 taken from delphi (pascal) example
  Result = ""
  for i in password:
    ordchar = ord(i)
    if ordchar >= ord('a') and ordchar <= ord('z'):
      if ordchar > ord('m'):
        ordchar -= 13
      else:
        ordchar += 13
    elif ordchar >= ord('A') and ordchar <= ord('Z'):
      if ordchar > ord('M'):
        ordchar -= 13
      else:
        ordchar += 13
    Result += chr(ordchar)
  return Result

def addToFile(userName, fullName, rotPassword):
  outputStr = "\n" + userName + ":" + fullName + ":" + rotPassword 
  #outFile = open('passwd.txt', 'a') # Showed warning underscore for 'open'
  with open('passwd.txt', 'a') as outFile: # Used with as no underline warning
    outFile.write(outputStr)
    outFile.close()

def deleteFromFile(userName):
  # To delete an entry, we have to rewrite the entire file without the entry
  with open('passwd.txt', 'r') as fileData:
    currentPasswords = fileData.readlines()
  fileData.close()
  # Read all the file data entries in, and now we have to write them line by line 
  with open('passwd.txt', 'w') as outFile:
    outFile.truncate() # Clears existing password file as we have in memory
    for users in currentPasswords:
      # If the username matches, we don't want to write it back out
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) != userName:
        outFile.write(users)
    outFile.close()

def changePasswordInFile(userName, password):
  # To change password, we have to rewrite the entire file with the new password
  with open('passwd.txt', 'r') as fileData:
    currentPasswords = fileData.readlines()
  fileData.close()
  with open('passwd.txt', 'w') as outFile:
    outFile.truncate() # Clears existing password file as we have in memory
    for users in currentPasswords:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == userName:
        fName = next(iterator)
        outputStr = userName + ":" + fName + ":" + password
        outFile.write(outputStr)
      else:
        outFile.write(users)
    outFile.close()


def findLogin(usernameToFind):
  with open('passwd.txt', 'r') as passwordFile:
    for users in passwordFile:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == usernameToFind:
        return True
  return False

def validUser(usernameToFind, currentPassword):
  Result = False
  with open('passwd.txt', 'r') as passwordFile:
    for users in passwordFile:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == usernameToFind:
        next(iterator)
        if next(iterator) == rot13(currentPassword):
          Result = True
  return Result


def getUserName(msgtext ="Enter Username (q to quit): "):
  Result = input(msgtext)
  if Result == "q":
    quit()
  if len(Result) == 0:
    print("Invalid User Name")
    getUserName()
  else:
    return Result

def getFullName():
  Result = input("Enter Full Name (q to quit): ")
  if Result == "q":
    quit()
  if len(Result) == 0:
    print("Invalid Full Name")
    getFullName()
  else:
    return Result

def getUserPassword():
  Result = pwinput.pwinput(prompt ="Enter Password (q to quit): ", mask="*")

  if Result == "q":
    quit()
  if len(Result) == 0:
    print("Invalid Password")
    getUserPassword()
  else:
    return Result

def getNewPassword(passwordAttempt = 1):
  if passwordAttempt == 1:
    Result = pwinput.pwinput(prompt ="Enter New Password (q to quit): ", mask="*")

  else:
    Result = pwinput.pwinput(prompt ="Re-enter New Password (q to quit): ", mask="*")

  if Result == "q":
    quit()
  if len(Result) == 0:
    print("Invalid Password")
    getNewPassword(passwordAttempt)
  else:
    return Result

def addUser():
  userName = getUserName()
  if findLogin(userName) is True:
    print("Oops! This User Name is already being used")
    addUser()
    
  #  To get here the user must have entered a new username
  fullName = getFullName()
  password = getUserPassword()
  addToFile(userName, fullName, rot13(password))
  print(userName, "added to the password file")


def deleteUser():
  userName = getUserName("Enter Username To Delete (q to quit): ")
  if findLogin(userName) is False:
    print("\nOops! This User Name doesn't exist, no changes have been made\n")
    deleteUser()
    
  #  To get here the user must have entered a valid username
  confirmDelete = input("Are you sure you want to delete this user? (Y/N) ")
  if confirmDelete == "Y" or confirmDelete == "y":
    deleteFromFile(userName)
    print("\n", userName, "has been removed from the password file\n")
  else:
    print("\nNo changes have been made\n")


def changePassword():
  userName = getUserName()
  currentPassword = getUserPassword()
  if validUser(userName, currentPassword) is False:
    print("Invalid credentials")
    changePassword()
    
  passwordChange1 = getNewPassword()
  passwordChange2 = getNewPassword(2)
  if passwordChange1 != passwordChange2:
    print("Passwords don't match")
    changePassword()
    
  # Now we change the password in the file
  changePasswordInFile(userName, rot13(passwordChange1))
  print("Password has been changed")


def login():
  userName = getUserName()
  currentPassword = getUserPassword()
  if validUser(userName, currentPassword) is False:
    print("Invalid credentials")
    login()
  else:
    print("Welcome to the system")
      

#run Program
menu()
