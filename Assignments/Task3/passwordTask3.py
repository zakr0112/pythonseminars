def menu():
  print("1: Add User")
  print("2: Delete User")
  print("3: Change Password")
  print("4: Login")
  menuEntry = input("Enter option: ")
  if menuEntry == "1":
    print()
    addUser()


def findLogin(usernameToFind):
  with open("passwd.txt") as passwordFile:
    for users in passwordFile:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == usernameToFind:
        return True
  return False

def getLoginName(loginNameEntry):
  print("getLoginName")
  loginNameEntry = input("Enter Login Name (q to quit): ")
  if loginNameEntry == "q":
    quit()
  if len(loginNameEntry) == 0:
    print("Invalid Login Name")
    getLoginName("")
  else:
    return loginNameEntry

def getFullName(fullNameEntry):
  fullNameEntry = input("Enter Full Name (q to quit): ")
  if fullNameEntry == "q":
    quit()
  if len(fullNameEntry) == 0:
    print("Invalid Full Name")
    getFullName("")
  else:
    return fullNameEntry

def getUserPassword(passwordEntry):
  passwordEntry = input("Enter Password (q to quit): ")
  if passwordEntry == "q":
    quit()
  if len(passwordEntry) == 0:
    print("Invalid Password")
    getUserPassword("")
  else:
    return passwordEntry

def addUser():
  print("addUser")
  loginNameEntry = getLoginName("")
  if findLogin(loginNameEntry) is True:
    print("Oops! This Login Name is already being used")
    addUser()
  else:
    print("Login Name Accepted:", loginNameEntry)
    fullNameEntry = getFullName("")
    print("Full Name:", fullNameEntry)
    passwordEntry = getUserPassword("")
    print("Password:", passwordEntry)




#run
menu()
