def menu():
  print("1: Add User")
  print("2: Delete User")
  print("3: Change Password")
  print("4: Login")
  menuEntry = input("Enter option: ")
  if menuEntry == "1":
    print()
    addUser()
  if menuEntry == "2":
    print()
    deleteUser()
  

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
  #outFile = open('passwd.txt', 'a')
  with open('passwd.txt', 'a') as outFile:
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

def findLogin(usernameToFind):
  with open('passwd.txt', 'r') as passwordFile:
    for users in passwordFile:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == usernameToFind:
        return True
  return False


def getUserName():
  Result = input("Enter Username (q to quit): ")
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
  Result = input("Enter Password (q to quit): ")
  if Result == "q":
    quit()
  if len(Result) == 0:
    print("Invalid Password")
    getUserPassword()
  else:
    return Result

def addUser():
  userName = getUserName()
  if findLogin(userName) is True:
    print("Oops! This User Name is already being used")
    addUser()
  else:
    fullName = getFullName()
    password = getUserPassword()
    #rotPassword = rot13(password)
    addToFile(userName, fullName, rot13(password))
    print(userName, "added to the password file")


def deleteUser():
  userName = getUserName()
  if findLogin(userName) is False:
    print("Oops! This User Name doesn't exist, no changes have been made")
    deleteUser()
  else:
    deleteFromFile(userName)
    print(userName, "has been removed from the password file")
    

#run Program
menu()
