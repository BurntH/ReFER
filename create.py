import data, name, frame, pretty, frame_axioms


def nub(l):
    seen = []
    for i in range(len(l)):
        if l[i] not in seen: 
            seen.append(l[i])
    return seen

def legal(x):
    return 48 <= ord(x) <= 57 or 63 <= ord(x) <= 122

def check_star(K, star):
    bad = "Frame axiom not satisfied: a** = a. Try again."
    if set(K) != set(star): 
        print(bad)
        return False
    for i in K:
        if star[K.index(star[K.index(i)])] != i: 
            print(bad)
            return False      
    return True

def check_R_format(K, R):
    for row in R:
        if len(row) != len(K):
            print("Incorrect format. Try again.")
            return False
    return True

def create_frame():
    #K
    line = input("Enter the points of your frame: \n")
    if line == "-E": return None
    K = nub([i for i in line if legal(i)])
    data.clear()
    print("K: " + pretty.pretty_set(K))
    
    #N
    line = input("Enter the normal points: \n")
    if line == "-E": return None
    N = nub([i for i in K if i in line])
    data.clear()
    print("K: " + pretty.pretty_set(K))
    print("N: " + pretty.pretty_set(N))
    
    #*
    accept = False
    while not accept:
        line = input("Enter the star table: \n")
        if line == "-E": return None
        star = nub([i for i in line if i in K])
        accept = check_star(K, star)
    data.clear()
    print("K: " + pretty.pretty_set(K))
    print("N: " + pretty.pretty_set(N))
    print("Star table:\n" + pretty.pretty_star(K, star))
      
    #R  
    accept = False
    while not accept:
        #check R format
        print("Enter the R table:")
        R = []
        for _ in range(len(K)):
            line = input()
            if line == "-E": return None
            row = line.split(",")
            row = [nub([i for i in K if i in cell]) for cell in row]
            R.append(row)
        if not check_R_format(K, R): continue
        
        #check frame axioms
        new_frame = frame.frame(K, N, R, star)
        accept = frame_axioms.check_frame(new_frame)
        if not accept:
            choice = ""
            while choice not in ["-E", "y", "n"]:
                choice = input("Proceed anyway? (y/n) \n")
            if choice == "-E": return None
            if choice == "y": accept = True
            if choice == "n": accept = False
            
    data.clear()
    print(pretty.pretty_frame(new_frame))
    
    #name
    choice = ""
    while choice not in ["-E", "y", "n"]:
        choice = input("Would you like to name your frame? (y/n) \n")
    if choice == "-E": return None
    if choice == "y": 
        x = name.name(new_frame)
    if choice == "n": 
        x = name.autoname(new_frame)
    if x == "-E": return None
    
    input("Frame '{0}' successfully created. Type anything to continue.\n".format(x))
    
    return None

