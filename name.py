import data

def illegal(s):
    return (s[:8] == "Untitled") or ("-" in s) or ("," in s) or (s == "") or ("'" in s) or ('"' in s)

def name(frame):
    x = input("How would you like to name your frame?\n")
    if x == "-e": 
        return "-e"
    if illegal(x):
        print("Illegal name. Come up with something else.\n")
        return name(frame)
    elif x in data.F:
        return name_in_use(x, frame) 
    data.F[x] = frame
    return x

def name_in_use(x, frame):
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Name '{0}' already in use. Overwrite? (y/n)\n".format(x))
    if choice == "-e": 
        return "-e"
    if choice == "y": 
        data.F[x] = frame
        return x
    return name(frame)

def autoname(frame):
    x = "Untitled" + str(len(data.F))
    data.F[x] = frame
    return x




