# !/usr/bin/env python3

# Save user's input to the variable char_name from the following question:
# Which character do you want to know about? (Starlord, Mystique, Hulk)

# Save a user's input to the variable char_stat from the following question:
# What statistic do you want to know about? (real name, powers, archenemy)

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

# Create a print function that combines info into this output:
#  <char_name>'s <char_stat> is: <value>


char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")
# make the above case insensitive
char_name = char_name.lower().capitalize()
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
# make the above case insensitive
char_stat = char_stat.upper().lower()
print(marvelchars[char_name][char_stat])

# instructor's method:
#print(f"{char_name}'s {char_stat} is: {marvelchars     [char_stat][char_name]}")

# Create a function that prints all of the stats for a given character
def print_all_stats(character):
    for stat in marvelchars[character]:
        print(f"{stat}: {marvelchars[character][stat]}")

# Call your function
print_all_stats(char_name)


