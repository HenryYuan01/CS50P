from pyfiglet import Figlet 
import sys 
import random 

figlet = Figlet() 
randFont = False 

# if 0 command line arguments 
if len(sys.argv) == 1: 
    # use random font 
    randFont = True 
# if 2 command line arguments 
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"): 
    # don't use random font 
    randFont = False 
else: 
    sys.exit("Invalid usage") 


figlet.getFonts() 

if randFont == False: 
    try: 
        figlet.setFont(font=sys.argv[2])
    except: 
        sys.exit("Invalid usage")
else: 
    font = random.choice(figlet.getFonts())
    

text = input("Input: ")
print("Output: ")
print(figlet.renderText(text))