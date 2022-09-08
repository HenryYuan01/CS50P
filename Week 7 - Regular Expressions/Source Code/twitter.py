import re 

url = input("URL: ").strip() 

''' 
# replace() has 2 arguments, what u wanna replace, what u wanna replace that with 
# remove prefix in sentence 
username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")
'''

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# "?:" means yes I'm grouping but not always necessary 
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE): 
    print(f"Username: ", matches.group(1))
