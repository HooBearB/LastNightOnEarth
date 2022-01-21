class format:
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    dim = "\u001b[2m"
    bold = "\u001b[1m"
    end = "\u001b[0m"
    red = "\u001b[31m"
    blue = "\u001b[36m"
    green = "\u001b[32m"

print(format.clear)
print(format.red + "Red" + format.end)
print(format.blue + "Blue" + format.end)
print(format.green + "Green" + format.end)
print(format.bold + "Bold" + format.end)
print(format.dim + "Dim" + format.end)
print(format.italic + "Italics" + format.end)
print(format.blue + format.bold + format.dim + "Combination" + format.end)