import data, edit, create, read, write


def select_frame():
    print("Created frames: " + ", ".join([i for i in data.F]))
    name = input("Enter a frame name:\n")
    if name == "-E":
        return None
    if name not in data.F:
        print("Frame not found.")
        return select_frame()
    data.Sel = True
    data.Selected = name
    return None

def menu():
    data.clear()
    if data.F == {}:
        print("Enter one of the following commands:")
        print("\t-n: New frame")
        print("\t-r: Read frame(s) from file")
        print("\t-M: Convert MaGIC algebras to frames")
        print("\t-E: Exit")
        print()
    
    elif not data.Sel:
        print("Created frames: " + ", ".join([i for i in data.F]))
        print("Enter one of the following commands:")
        print("\t-n: New frame")
        print("\t-s: Select frame")
        print("\t-r: Read frames from file")
        print("\t-M: Convert MaGIC algebras to frames")
        print("\t-w: Write frames to file")
        print("\t-D: Delete all frames")
        print("\t-E: Exit")
        print()
    
    if data.Sel:
        print("Selected frame: " + data.Selected)     
        print("\t-s: Reselect frame")
        print("\t-i: Inspect selected frame")
        print("\t-e: Edit frame")
        print("\t-d: Delete frame")
        print("\t-w: Write selected frame to file")
        print("\t-E: Unselect frame")
        print()
    
    try:    
        choice = input()
        if choice == "-n":
            create.create_frame()
            
        if choice == "-r":
            read.read_frame()
        
        if choice == "-s":
            if data.F == {}:
                print("Create a frame first.")
                input("Type anything to continue.\n")
                return menu()
            select_frame()
    
        if choice == "-e":
            if not data.Sel:
                print("Select a frame first.")
                input("Type anything to continue.\n")
                return menu()
            edit.edit_frame()
            
        if choice == "-i":
            if not data.Sel:
                print("Select a frame first.")
                input("Type anything to continue.\n")
                return menu()
            edit.inspect()
    
        if choice == "-d":
            if not data.Sel:
                print("Select a frame first.")
                input("Type anything to continue.\n")
                return menu()
            edit.delete_frame()
            
        if choice == "-D":
            if not data.Sel:
                edit.delete_all()
    
        if choice == "-w":
            if data.F == {}:
                print("Create a frame first.")
                input("Type anything to continue.\n")
                return menu()
            write.write_file()
    
        if choice == "-M":
            read.read_MaGIC()
            
        if choice == "-E": 
            if data.Sel:
                data.Sel = False
                return menu()
            else: 
                return None
                
        else: return menu()
               
    except Exception:
        input("An error occurred. Type anything to return to menu.\n")
        
    return menu()



menu()
