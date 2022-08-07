string = 'pythonexamples'
findE = string.index("e")
findx = string.index("x")
for position in range(len(string)):
    if position == findE:
        string = string[:position] + "o" + string[position+1:]
string = " ".join(string)
print(string)