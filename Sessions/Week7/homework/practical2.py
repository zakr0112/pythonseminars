#Practical 2 - Three Functions
"""
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.

Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.
"""

print()

def eitherword(word1, word2):
  return sorted(set(word1) | set(word2))

def bothwords(word1, word2):
  return sorted(set(word1) & set(word2))

def eitherbutnotbothwords(word1, word2):
  return sorted((set(word1) | set(word2)) - (set(word1) & set(word2)))

wordone = input("Enter word 1: ")
wordtwo = input("Enter word 2: ")

print("Letters in either word:", eitherword(wordone, wordtwo))
print("Letters in both words:", bothwords(wordone, wordtwo))
print("Letters in either, but not both:", eitherbutnotbothwords(wordone, wordtwo))



#do later