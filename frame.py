class frame:
    def __init__(self, K, N, R, star):
        self.K = K
        self.size = len(K)
        self.N = N
        self.R_table = R
        self.star_table = star
        self.order = [[1 if self.lleq(i, j) else 0 for j in K] for i in K]
        
    def index(self, a):
        return self.K.index(a)
        
    def star(self, a):
        return self.star_table[self.index(a)]
        
    def R(self, a, b, c):
        return c in self.R_table[self.index(a)][self.index(b)]
        
    def lleq(self, a, b):
        for x in self.N:
            if self.R(x, a, b):
                return True
        return False
        
    def leq(self, a, b):
        return self.order[self.index(a)][self.index(b)]
        
    def R4(self, a, b, c, d):
        for x in self.K:
            if self.R(a, b, x) and self.R(x, c, d):
                return True
        return False
    
    def R4p(self, a, b, c, d):
        for x in self.K:
            if self.R(b, c, x) and self.R(a, x, d):
                return True
        return False
        
        
        
