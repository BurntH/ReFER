
def FI1(F):
    for a in F.K:
        if not F.R(a, a, a):
            return False
    return True

def FI2(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c) and not F.R4p(a, a, b, c):
                    return False
    return True

def FI3(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                for d in F.K:
                    if F.R4(a, b, c, d) and not F.R4p(a, b, c, d):
                        return False
    return True

def FI4(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                for d in F.K:
                    if F.R4(a, b, c, d) and not F.R4p(b, a, c, d):
                        return False
    return True

def FI5(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c) and not F.R(b, a, c):
                    return False
    return True

def FI6(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                for d in F.K:
                    if F.R4(a, b, c, d) and not F.R4(a, c, b, d):
                        return False
    return True

def FI7(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c) and not F.R4(a, b, b, c):
                    return False
    return True

def FI8(F):
    for a in F.K:
        hold = False
        for x in F.N:
            if F.R(a, x, a):
                hold = True
        if not hold:
            return False
    return True

def FI9(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c) and not F.leq(a, c) and not F.leq(b, c):
                    return False
    return True

def FN1(F):
    for a in F.K:
        for b in F.K:
            for c in F.K:
                if F.R(a, b, c) and not F.R(a, F.star(c), F.star(b)):
                    return False
    return True

def FN2(F):
    for a in F.K:
        if not F.R(a, F.star(a), a):
            return False
    return True

def FN3(F):
    for a in F.N:
        if not F.leq(F.star(a), a):
            return False
    return True

   