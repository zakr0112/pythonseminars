# Practical 2 - Password Entry Program
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


def passwordentry():
  password1 = input("Enter password: ")
  password2 = input("Re-enter password: ")
  if password1 in BAD_PASSWORDS or password2 in BAD_PASSWORDS:
    print()
    print("Oops! This is a common password")
    print()
    passwordentry()
  elif password1 == password2:
    if len(password1) >= 8 and len(password2) <= 12:
      passwordsuccess()
    else:
      print()
      print("Passwords should be between 8 and 12 characters long")
      print()
      passwordentry()
  else:
    print()
    print("Passwords don't match")
    print()
    passwordentry()


def passwordsuccess():
  print()
  print("Passwords Match!")
  print()


passwordentry()
  

