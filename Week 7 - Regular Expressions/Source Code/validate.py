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
if re.search(r".+@.+\.edu", email): 
    print("Valid") 
else: 
    print("Invalid")