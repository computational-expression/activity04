# Runtime Errors Practice
# Complete the TODOs to fix the broken code examples

print("=== RUNTIME DEBUGGING PRACTICE ===")
print("Fix each example so it runs without crashing")
print()

# TODO 1: Fix the treasure map grid creator
print("Example 1: Treasure Map Grid")
rows = 3
cols = 0
for row in range(rows):
    for col in range(cols):
        print(f"({row},{col})", end=" ")
    print()
print("Map created!")
print()

# TODO 2: Fix the high score tracker
print("Example 2: High Score List")
high_scores = [95, 87, 92]
print(f"Top score: {high_scores[0]}")
print(f"Fourth place: {high_scores[3]}")
print()

# TODO 3: Fix the password strength checker
print("Example 3: Password Checker")
password = "abc123"
strength = int(password)
if strength > 6:
    print("Strong password!")
else:
    print("Weak password")
print()

# TODO 4: Fix the quest item counter (nested loops)
print("Example 4: Quest Items")
backpack = [["sword", "shield"], ["potion", "scroll"]]
total_items = 0
for bag_section in backpack:
    for item in bag_section:
        item_value = inventory_values[item]
        total_items += item_value
print(f"Total items: {total_items}")
print()

# TODO 5: Fix the guessing game (while loop)
print("Example 5: Number Guessing Game")
secret_number = 7
guess = 0
attempts = 0
while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    if attempts > 3:
        break
print(f"You guessed {guess} in {attempts} attempts!")
print()

# TODO 6: Fix the spell checker
print("Example 6: Magic Spell")
spell_word = ""
first_letter = spell_word[0]
print(f"Spell starts with: {first_letter}")

print("All examples completed!")
