# Practical 2 - Password Entry Program
def passwordentry():
  password1 = input("Enter password: ")
  password2 = input("Re-enter password: ")
  if password1 == password2:
    passwordsuccess()
  else:
    print()
    print("Passwords don't match")
    print()
    passwordentry()


def passwordsuccess():
  print()
  print("Passwords Match!")
  print("Access Granted")
  print()


passwordentry()
