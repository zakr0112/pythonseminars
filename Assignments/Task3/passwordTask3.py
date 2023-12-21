def menu():
  print("1: Add User")
  print("2: Delete User")
  print("3: Change Password")
  print("4: Login")


def findUser(usernameToFind):
  with open("passwd.txt") as passwordFile:
    for users in passwordFile:
      splitList = users.split(":", 3)
      iterator = iter(splitList)
      if next(iterator) == usernameToFind:
        return True
  return False
      






#run
menu()
