''' Password Complexity Checker:Build a tool that assesses the strength of a 
password based on criteria such as length, presence of uppercase and lowercase 
letters, numbers and special characters. Provide feedback to users on the 
password’s strength.'''

import re

def assess_password_strength(password):
    length_criteria = len(password) >=8
    lowercase = re.search("[a-z]", password) is not None
    uppercase = re.search("[A-Z]", password) is not None
    number = re.search("[0-9]", password) is not None
    special_char = re.search("[^a-zA-Z0-9]", password) is not None

    strength_score= sum([length_criteria, lowercase, uppercase, number, special_char])

    if strength_score == 5:
        feedback= "Very Strong"
    elif strength_score == 4:
        feedback= "Strong"
    elif strength_score == 3:
        feedback= "Moderate"
    elif strength_score == 2:
        feedback= "Weak"
    else:
        feedback= "Very Weak"
    
    return feedback

password= input("enter a password to assess its strength:")
strength= assess_password_strength(password)
print(f"Password strength: {strength}")