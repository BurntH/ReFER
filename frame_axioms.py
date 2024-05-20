def F1(F): #a \leq a
    for a in F.K:
        if not F.leq(a, a): 
            print("Frame axiom not satisfied: a \leq a.")
            return False
    return True
   
def F2(F): #a \leq b & b \leq c => a \leq c
    for a in F.K:
        for b in F.K:
            if F.leq(a, b):
                for c in F.K:
                    if F.leq(b, c):
                        if not F.leq(a, c):
                            print("Frame axiom not satisfied: a \leq b & b \leq c => a \leq c.")
                            return False
    return True
    
def F3(F): #a \in N & a \leq b => b \in N
    for a in F.N:
        for b in F.K:
            if F.leq(a, b) and b not in F.N:
                print("Frame axiom not satisfied: a \in N & a \leq b => b \in N.")
                return False
    return True
    
def F4(F): #a \leq b => (a*) \leq (b*)
    for a in F.K:
        for b in F.K:
            if F.leq(a, b):
                if not F.leq(F.star(b), F.star(a)):
                    print("Frame axiom not satisfied: a \leq b => (a*) \leq (b*).")
                    return False
    return True
    
def F5(F): #a** = a
    for a in F.K:
        if F.star(F.star(a)) != a:
            print("Frame axiom not satisfied: a** = a.")
            return False
    return True
      
def F6(F): #Rabc, d \leq a, e \leq b, c \leq f => Rdef
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c):
                    for d in F.K:
                        if F.leq(d, a):
                            for e in F.K:
                                if F.leq(e, b):
                                    for f in F.K:
                                        if F.leq(c, f):
                                            if not F.R(d, e, f):
                                                print("Frame axiom not satisfied: Rabc, d \leq a, e \leq b, c \leq f => Rdef.")
                                                return False
    return True            
                    
                    
                    
def check_frame(F):
    test = [F1(F), F2(F), F3(F), F4(F), F5(F), F6(F)]
    for i in range(6):
        if not test[i]:
            return False
    return True
    









    
