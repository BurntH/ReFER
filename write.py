import data, pretty

def write_file():
    filename = input("Enter a filename: \n")
    try:
        f = open(filename, "x")
    except Exception:
        choice = ""
        while choice not in ["-E", "y", "n"]:
            choice = input("File already exists. Overwrite? (y/n)\n")
        if choice == "-E":
            return None
        if choice == "y":
            f = open(filename, "w")
        if choice == "n":
            return write_file()
    
    choice = ""
    while choice not in ["-E", "-p", "-u"]:
        choice = input("How would you like your frame(s) written?\n\t-p: in pretty format\n\t-u: in ugly format\n")
    if choice == "-E":
        f.close()
        return None
    if choice == "-p":
        write_pretty_frames(f)
        input("{0} frame(s) written to {1} in pretty format. Type anything to continue.\n".format(str(1 if data.Sel else len(data.F)), filename))
        return None
    if choice == "-u":
        write_ugly_frames(f)
        input("{0} frame(s) written to {1} in ugly format. Type anything to continue.\n".format(str(1 if data.Sel else len(data.F)), filename))
        return None
        

def write_ugly_frames(f):
    if not data.Sel:
        for frame in data.F:
            f.write(frame + "\n")
            f.write(pretty.ugly_frame(data.F[frame]))
            f.write("\n")
        f.close()
        return None
    else:
        f.write(data.Selected + "\n")
        f.write(pretty.ugly_frame(data.F[data.Selected]))
        f.write("\n")
        f.close()
        return None

def write_pretty_frames(f):
    if not data.Sel:
        for frame in data.F:
            f.write("Frame name: " + frame + "\n")
            f.write(pretty.pretty_frame(data.F[frame]))
        f.close()
        return None
    else:
        f.write("Frame name: " + data.Selected + "\n")
        f.write(pretty.pretty_frame(data.F[data.Selected]))
        f.close()
        return None