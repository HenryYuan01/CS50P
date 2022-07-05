expression = input("Expression: ")

x, y, z = expression.split(" ")

xFloat = float(x)
zFloat = float(z)

if y == "+": 
    answer = xFloat + zFloat 
elif y == "-": 
    answer = xFloat - zFloat 
elif y == "*": 
    answer = xFloat * zFloat 
elif y == "/": 
    answer = xFloat / zFloat

print(f"{answer:.1f}")