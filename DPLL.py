

def DPLL(B, I):
    if len(B) == 0:
        return True, I

    for i in B:
        if len(i) == 0:
            return False, []

    x = B[0][0]
    if x[0] != '!':
        x = '!' + x

    Bp = [[j for j in i if j != x] for i in B if not(x[1:] in i)]

    Ip = [i for i in I]
    Ip.append('Valor de ' + x[1:] + ': ' + str(True))

    V, I1 = DPLL(Bp, Ip)
    if V:
        return True, I1
    
    Bp = [[j for j in i if j != x[1:]] for i in B if not(x in i)]

    Ip = [i for i in I]
    Ip.append('Valor de ' + x[1:] + ': ' + str(False))

    V, I2 = DPLL(Bp, Ip)
    if V:
        return True, I2

    return False, []



expresion =[['!p', '!r', '!s'], ['!q', '!p', '!s'], ['p'], ['s']]


t,r = DPLL(expresion, [])

print(t)
print(r)