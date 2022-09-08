import re 

# strip trims whitespace left or right of string 
email = input("What's your email? ").strip() 

''' 
# split splits one string into parts based on parameter 
username, domain = email.split("@")

# if username is string, and "." in domain 
# if (username) and ("." in domain): 
if (username) and (domain.endswith(".edu")): 
    print("Valid") 
else: 
    print("Invalid")
'''

# "r" means raw, "\" as escape to indicate ".edu"
# ".+" means some characters before "@" 
# "^/$" means must start/end with that 
# "[^@]" means can put anything here besides "@"
# "[a-zA-Z0-9._]" means everything in this range 
# "\w" means word characters 
# "?" means optional 
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): 
    print("Valid") 
else: 
    print("Invalid")