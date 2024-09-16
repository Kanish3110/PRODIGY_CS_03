import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    feedback = []
    
    # Check the length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
        
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
        
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")
        
    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, etc.).")
    
    # Evaluate strength
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[score]
    
    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions for improvement:")
    for suggestion in feedback:
        print(f"- {suggestion}")
