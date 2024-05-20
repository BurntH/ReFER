import data, create, name, frame, frame_axioms, algebra

def read_frame():
    x = open_file()
    if x == "-E": return None
    filename = x[0]
    lines = x[1]
    
    read_names = []
    read_frames = []
    
    while len(lines):
        try:
            name = lines.pop(0)
            if name == '': break
            
            K = lines.pop(0)
            K = [i for i in K if create.legal(i)]
        
            N = lines.pop(0)
            N = [i for i in K if i in N]
            
            star = lines.pop(0)
            star = [i for i in star if i in K]
        
        
            R = []
            for _ in range(len(K)):
                line = lines.pop(0)
                row = line.split(",")
                row = [create.nub([i for i in K if i in cell]) for cell in row]
                R.append(row)
            lines.pop(0)
            
            F = frame.frame(K, N, R, star)
            check = wrong(name, F)
            if check == "-E": return None
            
            read_names.append(name)
            read_frames.append(F)
        
        except Exception:
            print("Format error, please check again.")
            input("Type anything to continue.\n")
            return None
        
    rename_read(read_names, read_frames, filename)   
     
    return None

def read_MaGIC():
    x = open_file()
    if x == "-E": return None
    filename = x[0]
    lines = x[1]
    read_names = []
    read_frames = []
    
    try: 
        xx = algebra.MaGIC_to_frames(lines)
        if xx == "-E": return None
        read_names = xx[0]
        read_frames = xx[1]
        
    except Exception:
        print("Format error, please check again.")
        input("Type anything to continue.\n")
        return None
    
    count = len(read_names)
    for i in range(count):
        check = wrong(read_names[i], read_frames[i])
        if check == "-E": return None
        
    rename_read(read_names, read_frames, filename) 
    return None


def open_file():
    try: 
        filename = input("Enter filename: \n")
        if filename == "-E":
            return "-E"
        file = open(filename, "r")
        print("Reading from " + filename + "...")
        lines = [line.rstrip() for line in file.readlines()]
        file.close()
        return [filename, lines]
    except Exception:
        print("File not found.\n")
        return open_file() 
    
def wrong(name, F):
    if not frame_axioms.check_frame(F):
        choice = ""
        while choice not in ["-E", "y", "n"]:
            choice = input("Something's wrong with frame '{0}'. Continue anyway? (y/n) \n".format(name))
        if choice != "y":
            return "-E"
    return None

def rename_read(read_names, read_frames, filename):
    count = len(read_names)
    choice = ""
    while choice not in ["-E", "y", "n"]:
        if count == 1:
            choice = input("{0} frame read from {1}. Would you like to rename it? (y/n)\n".format(count, filename))
        else:
            choice = input("{0} frames read from {1}. Would you like to rename them? (y/n)\n".format(count, filename))
    if choice == "-E": return "-E"
    if choice == "n":
        seen = []
        for i in range(count):
            if read_names[i] in data.F or read_names[i] in seen:
                    repeat_count = 1
                    new = read_names[i] + "({0})".format(str(repeat_count)) 
                    while new in data.F or new in seen:
                        repeat_count += 1
                    read_names[i] = new
            seen.append(read_names[i]) 
        for i in range(count):  
            data.F[read_names[i]] = read_frames[i]
        return None
        
    if choice == "y":
        for i in range(count):
            print("Rename frame '{0}':".format(read_names[i]))
            name.name(read_frames[i])
            
        return None

