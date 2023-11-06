#Practical 4 - Calculate Average
"""
In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average
"""

print()

matches = 609
batted = 1014
notout = 162
scoredruns = 48426

stats = [matches, batted, notout, scoredruns]

def Average(stats):
  return sum(stats) / len(stats)

averagestats = Average(stats)
print("Average Stats:", round(averagestats, 2))