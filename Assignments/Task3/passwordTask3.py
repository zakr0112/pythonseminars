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
    print("Oops! This Login Name is already being used")
    addUser()
  else:
    print("Login Name Accepted:", userName)
    fullName = getFullName()
    print("Full Name:", fullName)
    password = getUserPassword()
    print("Password:", password)




#run
menu()
