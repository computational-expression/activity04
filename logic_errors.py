# Logic Errors Practice
# Complete the TODOs to fix the broken code examples

print("=== LOGIC DEBUGGING PRACTICE ===")
print("Fix each example so it produces the correct results")
print()

# TODO 1: Fix the chocolate factory conveyor belt (should show 3 rows of 4 chocolates each)
print("Example 1: Chocolate Factory Production Line")
conveyor_rows = 3
chocolates_per_row = 4
for row in range(conveyor_rows + 1):  # Off-by-one error!
    print(f"Row {row + 1}: ", end="")
    for chocolate in range(chocolates_per_row):
        print("🍫", end=" ")
    print()
print("Production complete!")
print()

# TODO 2: Fix the rainbow pattern (should make a triangle: R, RG, RGB)
print("Example 2: Rainbow Triangle")
colors = "RGB"
for row in range(1, 4):
    for col in range(row + 1):
        print(colors[col], end="")
    print()
print()

# TODO 3: Fix the rocket ship pattern (should make a complete rocket)
#    /\
#    ||
#   /\/\
#   ||||
#  /\/\/\
#  ||||||
# /\/\/\/\
# ||||||||
print("Example 3: Rocket Ship Launch Pad")
rocket_parts = 4
for section in range(rocket_parts):
    # Nose cone
    for space in range(rocket_parts - section):
        print(" ", end="")
    for tip in range(section):
        print("/\\", end="")
    print()
    # Body section  
    for space in range(rocket_parts - section):
        print(" ", end="")
    for body in range(section):
        print("||", end="")
    print()
print()

# TODO 4: Fix the word spell-checker (should spell "MAGIC" letter by letter)
print("Example 4: Magic Spell Casting")
magic_word = "MAGIC"
for letter_pos in range(5):  # 5 letters in MAGIC
    print(f"Casting letter {letter_pos + 1}: ", end="")
    for repeat in range(letter_pos):
        print(magic_word[letter_pos], end="")
    print()
print()

# TODO 5: Fix the birthday countdown (while loop should count down from 5 to 1)
print("Example 5: Birthday Party Countdown")
countdown = 5
while countdown >= 1:
    print(f"🎉 {countdown}!")
    countdown += 1  
print("🎂 Happy Birthday!")

print("All examples completed!")
