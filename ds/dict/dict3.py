data = {"csk":["ms","jadeja","raina"],"mi":["rohit","bumrah","pollard"]}
print(data)

print(data["csk"])

print(data.get("csk"))
data["mi"].append("surya")
print(data)

data["csk"].remove("jadeja")
print(data)
