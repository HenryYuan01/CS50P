import sys 

lines = [] 

if len(sys.argv) < 2: 
    sys.exit("Too few command-line arguments") 
elif len(sys.argv) > 2: 
    sys.exit("Too many command-line arguments") 
else: 
    if sys.argv[1].endswith(".py"): 
        try: 
            with open(sys.argv[1]) as file: 
                for line in file: 
                    if not line.isspace(): 
                        if not line.startswith("#"): 
                            lines.append(line.lstrip())
                print(len(lines))
        except FileNotFoundError: 
            sys.exit("File does not exist") 
    else: 
        sys.exit("Not a Python file")
    
