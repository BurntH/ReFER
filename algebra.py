import frame

def part(l, n):
    return [l[i*n: i*n + n] for i in range(len(l)//n)]

def matrix(l, size):
    return part(part(l, size), size)
    
    
class lattice:
    def __init__(self, size, neg, order):
        self.size = size
        self.neg_table = neg
        self.order = order
        
        self.pfs = ([[j for j in range(self.size) if self.leq(i, j)] for i in range(self.size) if self.JI(i)] + [[]])[-1::-1]
        self.dsize = len(self.pfs)
        
    def neg(self, a):
        return self.neg_table[a]

    def leq(self, a, b):
        return self.order[a][b]
    
    def meet(self, a, b):
        ans = 0
        for i in range(self.size):
            if self.leq(i, a) and self.leq(i, b) and self.leq(ans, i): 
                ans = i
        return ans
    
    def join(self, a, b):
        ans = self.size - 1
        for i in range(self.size):
            if self.leq(a, i) and self.leq(b, i) and self.leq(i, ans): 
                ans = i
        return ans
    
    def JI(self, a):
        for i in range(self.size):
            if self.leq(i, a) and not self.leq(a, i):
                for j in range(self.size):
                    if self.leq(j, a) and not self.leq(a, j):
                        if self.leq(a, self.join(i, j)):
                            return False
        return True
    
    def pfleq(self, p, q):
        if p == []: return 1
        if p[0] in q: return 1
        return 0
    
    def star(self, p):
        return [i for i in range(self.size) if self.neg(i) not in p]
        
        
class algebra(lattice):
    def __init__(self, size, neg, order, t, imp):
        super().__init__(size, neg, order)
        self.t = t
        self.choice_of_t = t.index(1)
        self.matrix = imp
        
        
    def normal(self, p):
        return int(self.choice_of_t in p)
    
    def imp(self, a, b):
        return self.matrix[a][b]
        
    def R(self, p, q, r):
        for i in q:
            for j in range(self.size):
                if (j not in r) and (self.imp(i, j) in p):
                    return 0
        return 1
        
def algFrame(A):
    pfs = A.pfs
    K = [chr(97 + i) for i in range(A.dsize)]
    N = [K[i] for i in range(A.dsize) if A.normal(pfs[i])]
    R = [[[K[k] for k in range(A.dsize) if A.R(pfs[i], pfs[j], pfs[k])] for j in range(A.dsize)] for i in range(A.dsize)]
    star = [K[pfs.index(A.star(pfs[i]))] for i in range(A.dsize)]
    return frame.frame(K, N, R, star)
    
 
def MaGIC_to_frames(f):
    f.pop(0)
    read_names = []
    read_frames = []
    run0 = True
    while run0:
        size = int(f.pop(0)) + 1
        if size == 0: 
            run0 = False
            continue
        negcount = 0
        run1 = True
        while run1:
            negcount += 1
            neg = [int(i) for i in f.pop(0).split(" ")]
            if neg[0] == -1: 
                run1 = False
                continue
            negindex = str(size)+"."+str(negcount)
            ordercount = 0
            run2 = True
            while run2:
                ordercount += 1
                order = part([int(i) for i in f.pop(0).split(" ")], size)
                if order == []: 
                    run2 = False
                    continue
                    
                L = lattice(size, neg, order)
                orderindex = negindex + "." + str(ordercount)

                tcount = 0
                run3 = True
                while run3:
                    tcount += 1
                    t = [int(i) for i in f.pop(0).split(" ")]
                    if t[0] == -1: 
                        run3 = False
                        continue
                    tindex = orderindex + "." + str(tcount)
                    M = matrix([int(i) for i in f.pop(0).split(" ")], size)
                    
                    impcount = 0
                    for imp in M:
                        A = algebra(size, neg, order, t, imp)
                        impcount += 1
                        impindex = tindex + "." + str(impcount)
                        F = algFrame(A)
                        read_names.append(impindex)
                        read_frames.append(F)    
    return [read_names, read_frames]

                    
    
    

    
        