
def pretty_set(S):
    return "{" + ", ".join(S) + "}\n"
             
def pretty_star(K, star):
    size = len(star)
    out = ""
    out += " ".join(["\t   |"] + K) + "\n"
    out += "\t" + "---+-" + ("-")*(2 * size) + "\n"
    out += " ".join(["\t * |"] + star) + "\n"
    return out
    
        
def pretty_order(K, order):
    size = len(K)
    out = ""
    out += (" ".join(["\t < |"] + K)) + "\n"
    out += ("\t" + "---+-" + ("-")*(2 * size)) + "\n"
    for i in range(size):
        out += (" ".join(["\t", K[i], "|"] + ["+" if j else "-" for j in order[i]])) + "\n"
    return out
    

        
def pretty_R(K, R):
    size = len(K)
    outt = ""
    outt += (" ".join(["\t R |"] + [i + " "*(size-1) for i in K])) + "\n"
    outt += ("\t" + "---+-" + ("-")*(size * (size+1))) + "\n"
    for i in range(size):
        out = " ".join(["\t", K[i], "| "])
        for j in range(size):
            l = "".join(R[i][j])
            out += (l + " "*(size + 1 - len(l)))
        outt += out + "\n"
    return outt
    

def pretty_frame(F):
    out = ""
    out += "K: " + pretty_set(F.K) + "\n"
    out += "N: " + pretty_set(F.N) + "\n"
    out += "Star table: \n" + pretty_star(F.K, F.star_table) + "\n"
    out += "R table: \n" + pretty_R(F.K, F.R_table) + "\n"
    out += "Order: \n" + pretty_order(F.K, F.order) + "\n"
    return out
    
def ugly_frame(F):
    out = ""
    out += " ".join(F.K) + "\n"
    out += " ".join(F.N) + "\n"
    out += " ".join(F.star_table) + "\n"
    for i in range(F.size):
        out += ", ".join(["".join(F.R_table[i][j]) for j in range(F.size)])
        out += "\n"
    return out
    
    
    
    
    
    
    