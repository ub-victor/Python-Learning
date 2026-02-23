# To define formatted strings : prefix your string with an f and then curly braces to dynamically insert value into your strings.
first = "Victoire"
last = "Ushindi"


message = first +" ["+ last + "] is a coder"

msg = f"{first} [{last}] is a coder" # that is what called formatted String 

print(message)
print(msg)