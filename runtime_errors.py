# Runtime Errors Practice
# Fix the following code examples - each will crash when running

print("=== RUNTIME DEBUGGING PRACTICE ===")
print("Fix each example so it runs without crashing")
print()

# Example 1: Division by zero
print("Example 1: Calculator")
num1 = 10
num2 = 0
result = num1 / num2
print(f"Result: {result}")
print()

# Example 2: Index out of range
print("Example 2: List access")
colors = ["red", "blue", "green"]
print(f"First color: {colors[0]}")
print(f"Fourth color: {colors[3]}")
print()

# Example 3: ValueError with int conversion
print("Example 3: Age checker")
age_input = "twenty"
age = int(age_input)
if age >= 18:
    print("You're an adult!")
else:
    print("You're a minor")
print()

# Example 4: NameError - undefined variable
print("Example 4: Grade calculator")
math_grade = 85
science_grade = 92
average = (math_grade + english_grade) / 3
print(f"Average grade: {average}")
print()

# Example 5: String index error
print("Example 5: First letter")
word = ""
first_letter = word[0]
print(f"First letter: {first_letter}")
print()

# Example 6: Type error
print("Example 6: Adding numbers")
number1 = 5
number2 = "3"
total = number1 + number2
print(f"Total: {total}")

print("All examples completed!")
