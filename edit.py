import data, frame, name, pretty, create, conditions


def rename_frame():
    F = data.F[data.Selected]
    new = name.name(F)
    if new != data.Selected:
        del data.F[data.Selected]
    data.Selected = new
    return None

def rename_points(F, l):
    K = l
    N = [l[F.index(i)] for i in F.N]
    star = [l[F.index(i)] for i in F.star_table]
    R = [[[l[F.index(k)] for k in F.R_table[i][j]] for j in range(F.size)] for i in range(F.size)]
    return frame.frame(K, N, R, star)
    
def permute_points(F, l):
    K = l
    N = [i for i in l if i in F.N]
    star = [F.star(i) for i in l]
    R = [[[k for k in l if F.R(i, j, k)] for j in l] for i in l]
    return frame.frame(K, N, R, star)
    
def sort_points(F):
    l = F.K[:]
    l.sort(key = (lambda x: len([i for i in F.K if F.leq(i, x)])))
    return permute_points(F, l)


def edit_frame():
    data.clear()
    print("Selected frame: " + data.Selected)
    print(pretty.pretty_frame(data.F[data.Selected]))
    print()
    edit_menu = """What do you not like about this frame?
    \t-n: Rename frame
    \t-k: Rename points
    \t-p: Permute points
    \t-s: Sort points
    \t-E: Exit edit
    """
    print(edit_menu)
    edit = input()
    if edit not in ["-E", "-n", "-k", "-p", "-s"]:
        return edit_frame()
    
    if edit == "-E":
        return None
    
    if edit == "-n":
        rename_frame()
        
    if edit == "-k":
        F = data.F[data.Selected]
        
        line = ""
        while len(line) != F.size:
            print("There are {0} points to be renamed.".format(str(F.size)))
            line = input("Enter the points of your frame: \n")
            if line == "-E": 
                return edit_frame()
            line = [i for i in line if create.legal(i)]
            
        F_new = rename_points(F, line)
        data.F[data.Selected] = F_new
            
    if edit == "-p":
        F = data.F[data.Selected]
        
        line = ""
        while len(line) != F.size or set(line) != set(F.K):
            line = input("Enter a permutation of {0}:\n".format(", ".join(F.K)))
            if line == "-E":
                return edit_frame()
            line = [i for i in line if create.legal(i)]
            
        F_new = permute_points(F, line)
        data.F[data.Selected] = F_new
        
    if edit == "-s":
        data.F[data.Selected] = sort_points(data.F[data.Selected])    
    
    data.clear()
    print("Selected frame: " + data.Selected)
    print(pretty.pretty_frame(data.F[data.Selected]))
    print()  
      
    conti = ""
    while conti not in ["-E", "y", "n"]:
        conti = input("Edit successful. Continue editing? (y/n)\n")
    if conti == "y":
        return edit_frame()
    return None



def delete_frame():
    choice = ""
    while choice not in ["-E", "y", "n"]:
        choice = input("Delete frame: {0}? (y/n)\n".format(data.Selected))
    if choice == "y":
        data.Sel = False
        del data.F[data.Selected]
        input("Frame '{0}' deleted. Type anything to continue.\n".format(data.Selected))
        data.Selected = ""
    return None
    
def delete_all():
    choice = ""
    while choice not in ["-E", "y", "n"]:
        choice = input("Delete all frames? (y/n)\n")
    if choice == "y":
        data.Selected = ""
        data.F = {}
        input("All frames deleted. Type anything to continue.\n")
    return None
    
    
def inspect():
    data.clear()
    print("Selected frame: " + data.Selected)
    print(pretty.pretty_frame(data.F[data.Selected]))
    print()
    print("Enter one of the following commands:")
    print("\t-f: Check frame conditions")
    print("\t-E: Exit inspect mode")
    choice = input()
    if choice == "-E": return None
    if choice == "-f":
        frame_conditions()
        input("Type anything to continue.")
    return inspect()

def frame_conditions():
    F = data.F[data.Selected]
    print(" I1: A & (A -> B) -> B")
    print("FI1: Raaa")
    print("Holds on this frame: {0}\n".format(str(conditions.FI1(F))))
    
    print(" I2: (A -> B) & (B -> C) -> (A -> C)")
    print("FI2: Rabc => Ra(ab)c")
    print("Holds on this frame: {0}\n".format(str(conditions.FI2(F))))
    
    print(" I3: (A -> B) -> ((C -> A) -> (C -> B))")
    print("FI3: Rabcd -> Ra(bc)d")
    print("Holds on this frame: {0}\n".format(str(conditions.FI3(F))))
    
    print(" I4: (A -> B) -> ((B -> C) -> (A -> C))")
    print("FI4: Rabcd => Rb(ac)d")
    print("Holds on this frame: {0}\n".format(str(conditions.FI4(F))))
    
    print(" I5: A -> ((A -> B) -> B)")
    print("FI5: Rabc => Rbac")
    print("Holds on this frame: {0}\n".format(str(conditions.FI5(F))))
    
    print(" I6: (A -> (B -> C)) -> (B -> (A -> C))")
    print("FI6: Rabcd => Racbd")
    print("Holds on this frame: {0}\n".format(str(conditions.FI6(F))))
    
    print(" I7: (A -> (A -> B)) -> (A -> B)")
    print("FI7: Rabc => Rabbc")
    print("Holds on this frame: {0}\n".format(str(conditions.FI7(F))))
    
    print(" I8: (t -> A) -> A")
    print("FI8: \\exists x \\in N, Raxa")
    print("Holds on this frame: {0}\n".format(str(conditions.FI8(F))))
    
    print(" I9: A -> (A -> A)")
    print("FI9: Rabc => a \\leq c or b \\leq c")
    print("Holds on this frame: {0}\n".format(str(conditions.FI9(F))))
    
    print(" N1: (A -> ~B) -> (B -> ~A)")
    print("FN1: Rabc => Ra(c*)(b*)")
    print("Holds on this frame: {0}\n".format(str(conditions.FN1(F))))
    
    print(" N2: (A -> ~A) -> ~A")
    print("FN2: Ra(a*)a")
    print("Holds on this frame: {0}\n".format(str(conditions.FN2(F))))
    
    print(" N3: A v ~A")
    print("FN3: \\forall a \\in N, a* \\leq a")
    print("Holds on this frame: {0}\n".format(str(conditions.FN3(F))))
    
    return None
    
    
    
    
    