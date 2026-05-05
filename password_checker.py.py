def password_analyzer(password):
  has_upper= False
  has_lower= False
  has_digit= False
  has_specialchar= False

  for char in password:
     if char.isupper():
         has_upper = True
     elif char.islower():
         has_lower = True
     elif char.isdigit():
         has_digit = True
     else:
         has_specialchar = True
         
  return has_upper,has_lower,has_digit,has_specialchar

def score_calculator(password,has_upper,has_lower,has_digit,has_specialchar):
    score=0

    if len(password) >= 8:
        score = score + 1
    if has_upper:
        score +=1
    if has_lower:
        score +=1
    if has_digit:
        score +=1
    if has_specialchar:
        score +=1
    return score

def suggestions(password,has_upper,has_lower,has_digit,has_specialchar):
   print("\n Suggestions to improve your password:")

   if not has_upper:
       print("- Add atleast one uppercase letter")
   if len(password)<8:
       print("- Make password atleast 8 characters long")
   if not has_lower:
       print("- Add at least one lowercase letter")
   if not has_digit:
       print("- Add atleast one numeric character in the password")
   if not has_specialchar:
       print("- Add at least one special character; e.g !£@ ")

#Main Program
password= input("Enter your password: ")

has_upper,has_lower,has_digit,has_specialchar = password_analyzer(password)

score= score_calculator(password,has_upper,has_lower,has_digit,has_specialchar)

percentage= (score/5)*100

if score<= 2:
    print("Weak password")
    print("Password Strength:",percentage,"%")
    suggestions(password,has_upper,has_lower,has_digit,has_specialchar)

elif score == 3 or score == 4:
    print("Medium strength password")
    print("Password Strength:",percentage,"%")
    suggestions(password,has_upper,has_lower,has_digit,has_specialchar)

else:
    print("Strong password ,no suggestions required")
    print("Password Strength:",percentage,"%")
    
