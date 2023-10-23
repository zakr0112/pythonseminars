def display_heading(text):
  """ Prints a heading between two bars """
  print("==================================")
  print(text)
  print("==================================")


if __name__ == "__main__":
  import sys
  if len(sys.argv) > 1:
    display_heading(sys.argv[1])