password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase
if any(char.isupper() for char in password):
    score += 1

# Check lowercase
if any(char.islower() for char in password):
    score += 1

# Check digit
if any(char.isdigit() for char in password):
    score += 1

# Check special character
if any(not char.isalnum() for char in password):
    score += 1

# Determine strength
if score <= 1:
    print("Very Weak")
elif score == 2:
    print("Weak")
elif score == 3:
    print("Medium")
else:
    print("Strong")