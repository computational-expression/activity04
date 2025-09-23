# Logic Errors Practice
# Complete the TODOs to fix the broken code examples

print("=== LOGIC DEBUGGING PRACTICE ===")
print("Fix each example so it produces the correct results")
print()

# TODO 1: Fix the code below (average should be 85)
print("Example 1: Grade average")
grade1 = 80
grade2 = 85
grade3 = 90
average = (grade1 + grade2 + grade3) / 2
print(f"Average grade: {average}")
print()

# TODO 2: Fix the code below (should count down 5, 4, 3, 2, 1)
print("Example 2: Countdown")
print("Countdown:")
for i in range(5):
    print(i)
print("Blast off!")
print()

# TODO 3: Fix the code below (age 18 should show 'adult')
print("Example 3: Age category")
age = 18
if age > 18:
    print("adult")
elif age < 18:
    print("minor")
else:
    print("exactly 18")
print()

# TODO 4: Fix the code below ('password123' should be accepted)
print("Example 4: Password check")
password = "password123"
if password == "Password123":
    print("Access granted")
else:
    print("Access denied")
print()

# TODO 5: Fix the code below (sum should be 15)
print("Example 5: Sum calculation")
total = 1
for num in range(1, 6):
    total = total + num
print(f"Total: {total}")
print()

# TODO 6: Fix the code below (get the last item)
print("Example 6: Last item")
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits[3]
print(f"Last fruit: {last_fruit}")

print("All examples completed!")
