def password_strength(password):
  length_score = 0
  uppercase_score = 0
  lowercase_score = 0
  digit_score = 0
  special_char_score = 0

  if len(password) >= 8:
    length_score += 1
  if len(password) >= 12:
    length_score += 1
  if len(password) >= 16:
    length_score += 1

  if any(char.isupper() for char in password):
    uppercase_score += 1

  if any(char.islower() for char in password):
    lowercase_score += 1

  if any(char.isdigit() for char in password):
    digit_score += 1

  if any(char in "!@#$%^&*()_+-=[]{};':\",<.>/?\\|~" for char in password):
    special_char_score += 1

  total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

  if total_score < 3:
    return "Weak"
  elif total_score < 5:
    return "Medium"
  else:
    return "Strong"

while True:
    password = input("Enter a password: ")
    strength = password_strength(password)
    print("Password strength:", strength)
    another_check = input("Do you want to check another password? (yes/no): ")
    if another_check.lower() != 'yes':
        break 
