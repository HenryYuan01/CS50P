import sys 
import csv 

output = [] 

if len(sys.argv) < 3: 
    sys.exit("Too few command-line arguments") 
elif len(sys.argv) > 3: 
    sys.exit("Too many command-line arguments") 
else: 
    try: 
        with open(sys.argv[1]) as file: 
            reader = csv.DictReader(file) 
            for row in reader: 
                nameSplit = row["name"].split(",")
                output.append({'firstName': nameSplit[1].lstrip(), "lastName": nameSplit[0], "house": row["house"]})
        with open(sys.argv[2], "w") as file: 
            writer = csv.DictWriter(file, fieldnames=["firstName", "lastName", "house"]) 
            writer.writerow({"firstName": "firstName", "lastName": "lastName", "house": "house"})
            for row in output: 
                writer.writerow({"firstName": row["firstName"], "lastName": row["lastName"], "house": row["house"]})
    except FileNotFoundError: 
        sys.exit(f"Could not read {sys.argv[1]}") 
    