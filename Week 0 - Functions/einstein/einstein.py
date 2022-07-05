# Ask user for mass input as an integer (in kg) 
mass = int(input("What's the mass? "))

# Value of c^2 
csquared = 300000000 * 300000000 

# Energy in Joules 
energy = mass * csquared 

# Print equivalent number of Joules as an integer 
print(energy)