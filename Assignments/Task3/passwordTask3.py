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
  if menuEntry == "3":
    print()
    changePassword()
  

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

def getNewPassword(passwordAttempt):
  if passwordAttempt == 1:
    Result = input("Enter New Password (q to quit): ")
  else:
    Result = input("Re-enter New Password (q to quit): ")
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


def changePassword():
  userName = getUserName()
  currentPassword = getUserPassword()
  if validUser(userName, currentPassword) is False:
    print("Invalid credentials")
    changePassword()
  else:
    passwordChange1 = getNewPassword(1)
    passwordChange2 = getNewPassword(2)
    if passwordChange1 != passwordChange2:
      print("Passwords don't match")
      changePassword()
    else:
      # Now we change the password in the file
      changePasswordInFile(userName, rot13(passwordChange1))
      print("Password has been changed")



#run Program
menu()
