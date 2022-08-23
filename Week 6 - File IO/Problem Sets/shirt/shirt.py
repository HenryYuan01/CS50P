import sys 
from os.path import splitext
from PIL import Image, ImageOps


if len(sys.argv) < 3: 
    sys.exit("Too few command-line arguments") 
if len(sys.argv) > 3: 
    sys.exit("Too many command-line arguments") 
else: 
    if sys.argv[1].endswith((".jpg", ".jpeg", ".png")): 
        if sys.argv[2].endswith((".jpg", ".jpeg", ".png")): 
            file1 = splitext(sys.argv[1]) 
            file2 = splitext(sys.argv[2])
            if file1[1].lower() == file2[1].lower(): 
                try: 
                    with open(sys.argv[1]) as file: 
                        shirt = Image.open("shirt.png")
                        size = shirt.size
                        photo = ImageOps.fit(file, size) 
                        photo.paste(shirt, shirt)
                        photo.save(sys.argv[2])
                except FileNotFoundError: 
                    sys.exit("File does not exist") 
            else: 
                sys.exit("Input and output have different extensions")
        else: 
            sys.exit("Invalid output")
    else: 
        sys.exit("Invalid input")