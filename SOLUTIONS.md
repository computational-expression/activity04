# Activity 04 - Debugging Practice Solutions

## Syntax Errors Solutions (syntax_errors.py)

### TODO 1: Taco Tuesday Order
**Error**: Missing closing parenthesis in input statement
```python
# BROKEN:
taco_count = input("How many tacos do you want? "
# FIXED:
taco_count = input("How many tacos do you want? ")
```

### TODO 2: Superhero Academy
**Error**: Using assignment operator (=) instead of comparison operator (==)
```python
# BROKEN:
if power_level = 100:
# FIXED:
if power_level == 100:
```

### TODO 3: Coffee Emergency
**Error**: Missing colon after if statement
```python
# BROKEN:
if mood == "tired"
# FIXED:
if mood == "tired":
```

### TODO 4: Love Letter Pattern
**Error**: Missing indentation in nested loop
```python
# BROKEN:
for heart in range(row + 1):
print("♥", end=" ")
# FIXED:
for heart in range(row + 1):
    print("♥", end=" ")
```

### TODO 5: Daily Cat Wisdom
**Error**: Missing closing quote in string
```python
# BROKEN:
cat_fact = "Cats spend 70% of their lives sleeping. Lucky cats!
# FIXED:
cat_fact = "Cats spend 70% of their lives sleeping. Lucky cats!"
```

---

## Runtime Errors Solutions (runtime_errors.py)

### TODO 1: Dance Floor Setup
**Error**: Loop range is 0, so no dancers print
```python
# BROKEN:
cols = 0
for col in range(cols):  # range(0) produces no iterations
# FIXED:
cols = 4  # Or any positive number
for col in range(cols):
```

### TODO 2: Donut Math Gone Wrong
**Error**: Trying to convert string "twelve" to integer
```python
# BROKEN:
donuts = "twelve"
donuts_per_person = int(donuts) / people  # Can't convert "twelve" to int
# FIXED:
donuts = 12  # Use numeric value instead
donuts_per_person = donuts / people
```

### TODO 3: Top Secret Message
**Error**: String index out of range (empty string)
```python
# BROKEN:
secret_message = ""
decoded_letter = secret_message[0]  # Empty string has no index 0
# FIXED:
secret_message = "CLASSIFIED"  # Give it actual content
decoded_letter = secret_message[0]  # Now index 0 exists
```

### TODO 4: Pizza Party Math
**Error**: Division by zero
```python
# BROKEN:
guests = 0
slices_per_guest = pizza_slices / guests  # Division by zero error!
# FIXED:
guests = 6  # Or any positive number
slices_per_guest = pizza_slices / guests
```

### TODO 5: Gaming High Score
**Error**: NameError - undefined variable (typo in variable name)
```python
# BROKEN:
print(f"Player {player_name} achieved a score of {hight_score}!")  # Typo: hight_score
# FIXED:
print(f"Player {player_name} achieved a score of {high_score}!")   # Correct: high_score
```

---

## Logic Errors Solutions (logic_errors.py)

### TODO 1: Chocolate Factory Production Line
**Error**: Off-by-one error creates extra row
```python
# BROKEN:
for row in range(conveyor_rows + 1):  # Creates 4 rows instead of 3
# FIXED:
for row in range(conveyor_rows):      # Creates exactly 3 rows
# Should show:
# Row 1: 🍫 🍫 🍫 🍫 
# Row 2: 🍫 🍫 🍫 🍫 
# Row 3: 🍫 🍫 🍫 🍫 
```

### TODO 2: Rainbow Triangle Pattern
**Error**: Off-by-one error in loop range
```python
# BROKEN:
for col in range(row + 1):  # Prints too many characters: RG, RGB, RGBR
# FIXED:
for col in range(row):      # Prints correct triangle: R, RG, RGB
```

### TODO 3: Rocket Ship Launch Pad (ASCII Art)
**Error**: Using wrong loop variable - rocket doesn't build properly
```python
# BROKEN:
for tip in range(section):    # Starts with 0, first row shows nothing
for body in range(section):   # Same issue with body sections
# FIXED:
for tip in range(section + 1):    # Properly builds rocket width
for body in range(section + 1):   # Creates complete rocket sections
# Creates ASCII rocket ship:
#    /\
#    ||
#   /\/\
#   ||||
#  /\/\/\
#  ||||||
# /\/\/\/\
# ||||||||
```

### TODO 4: Magic Spell Casting
**Error**: Wrong starting position for letter display
```python
# BROKEN:
for repeat in range(letter_pos):     # Starts at 0, shows nothing for first letter
# FIXED:
for repeat in range(letter_pos + 1): # Shows M, AA, GGG, IIII, CCCCC
```

### TODO 5: Birthday Countdown (INFINITE LOOP!)
**Error**: Incrementing instead of decrementing
```python
# BROKEN:
countdown += 1  # This makes countdown grow: 5, 6, 7, 8... forever!
# FIXED:
countdown -= 1  # This makes countdown shrink: 5, 4, 3, 2, 1, done!
```

---

## Key Debugging Strategies Used

### Syntax Errors:
- Check for missing punctuation (parentheses, colons, quotes)
- Verify consistent indentation
- Look for typos in keywords

### Runtime Errors:
- Check for division by zero
- Verify variable names are spelled correctly
- Make sure list/string indices are within bounds
- Ensure variables are defined before use

### Logic Errors:
- Trace through loops step by step
- Check off-by-one errors in ranges
- Verify mathematical operations produce expected results
- Watch for infinite loops (wrong increment/decrement)
- Test edge cases and boundary conditions

---

## Tips for Future Debugging

1. **Read error messages carefully** - they often tell you exactly what's wrong
2. **Use print statements** to see what variables contain
3. **Test with simple inputs** first
4. **Check your math** - logic errors often involve incorrect calculations
5. **Trace through loops** manually with pencil and paper
6. **Be suspicious of while loops** - make sure the condition will eventually become false!
