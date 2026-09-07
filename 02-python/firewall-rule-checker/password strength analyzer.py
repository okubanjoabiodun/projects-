import re

def analye_password(password):
    score =  0
    feedback=[]

# check pawword length
    if len( password)>= 8:
     score += 1

# check if it has atleast  12 characters 
    if len(password) >= 12:
     score += 1

# check lowercase letters
    if re.search(r"[a-z]",password):
     score +=1
    else:
     feedback.append(" Add lowercase  letters")

# check uppercase letters
    if re.search(r"[A-Z]" , password):
     score +=  1
    else:
     feedback.append("Add uppercase letters")

# check for numbers
    if re.search(r"[0-9]" , password):
     score += 1
    else:
     feedback.append("Add numbers")

# check for special characters
    if re.search(r"[^A-Za-z0-9]", password):
     score += 1
    else:
     feedback.append("Add special characters")

#deterimine password strength
    if score <=2:
     strength = "Weak"   
    elif score == 3:
     strength = " Moderate"
    elif score == 4:
     strength = "strong"
    else:
     strength = "very strong"
   
    return score,strength,feedback 

password = input("Enter a password to analyze:")
score , strength,feedback = analye_password(password)
print("\n---password Analysis---")

print(f"score:{score}/6")
print(f"strength:{strength}")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print(f"- {item}")
else:
    print("Your password meets all the basic checks.")



































































































