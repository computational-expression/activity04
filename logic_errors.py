# Logic Errors Practice
# Fix the following code examples - they run but give wrong results

print("=== LOGIC DEBUGGING PRACTICE ===")
print("Fix each example so it produces the correct results")
print()

# Example 1: Average calculation
print("Example 1: Grade average (should be 85)")
grade1 = 80
grade2 = 85
grade3 = 90
average = (grade1 + grade2 + grade3) / 2  # Wrong divisor!
print(f"Average grade: {average}")
print()

# Example 2: Loop range
print("Example 2: Countdown (should go 5, 4, 3, 2, 1)")
print("Countdown:")
for i in range(5):  # Wrong range!
    print(i)
print("Blast off!")
print()

# Example 3: Comparison logic
print("Example 3: Age category (18 should be 'adult')")
age = 18
if age > 18:  # Wrong comparison!
    print("adult")
elif age < 18:
    print("minor")
else:
    print("exactly 18")
print()

# Example 4: String comparison
print("Example 4: Password check ('password123' should be accepted)")
password = "password123"
if password == "Password123":  # Wrong case!
    print("Access granted")
else:
    print("Access denied")
print()

# Example 5: Loop accumulation
print("Example 5: Sum 1+2+3+4+5 (should be 15)")
total = 1  # Wrong starting value!
for num in range(1, 6):
    total = total + num
print(f"Total: {total}")
print()

# Example 6: List indexing
print("Example 6: Get last item from list")
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits[3]  # Wrong index!
print(f"Last fruit: {last_fruit}")

print("All examples completed!")
