# Logic Errors Practice
# Complete the TODOs to fix the broken code examples

print("=== LOGIC DEBUGGING PRACTICE ===")
print("Fix each example so it produces the correct results")
print()

# TODO 1: Fix the pizza slice calculator (should be 8 slices total)
print("Example 1: Pizza Party")
people = 4
slices_per_person = 2
total_slices = people * slices_per_person - 2
print(f"We need {total_slices} pizza slices")
print()

# TODO 2: Fix the multiplication table (should show 3x table: 3, 6, 9, 12)
print("Example 2: Multiplication Table")
number = 3
print(f"Multiplication table for {number}:")
for i in range(1, 5):
    result = number * i + 1
    print(f"{number} x {i} = {result}")
print()

# TODO 3: Fix the treasure chest pattern (should make a 4x4 square of X's)
print("Example 3: Treasure Chest Grid")
size = 4
for row in range(size):
    for col in range(size - 1):
        print("X", end=" ")
    print()
print()

# TODO 4: Fix the level up checker (level 10 should show 'Expert')
print("Example 4: Game Level")
player_level = 10
if player_level > 10:
    print("Expert")
elif player_level > 5:
    print("Intermediate")
else:
    print("Beginner")
print()

# TODO 5: Fix the coin collector (while loop should collect exactly 10 coins)
print("Example 5: Coin Collection")
coins = 0
target = 10
while coins <= target:
    coins += 2
    print(f"Collected {coins} coins")
print(f"Final collection: {coins} coins")
print()

# TODO 6: Fix the high score list (should get the highest score)
print("Example 6: Gaming Leaderboard")
scores = [85, 92, 78, 96, 88]
highest_score = scores[0]
print(f"Highest score: {highest_score}")

print("All examples completed!")
