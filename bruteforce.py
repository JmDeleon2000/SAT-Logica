
expresion = [['!p'],['p', 'q'], ['p' , '!q', '!x', '!z'], ['p']]
vars = []



def bruteforceSAT(exp):
    #función wrapper para le recursiva
    global vars
    if (len(exp) == 0):
        # caso trivial
        return [True, exp]
    if len(vars) == 0:
        # hacer setup para la recursión en base a las variables presentes
        for i in range(len(exp)):
                for j in range(len(exp[i])):
                    var = exp[i][j]
                    if var[0] == '!':
                        var = var[1:]
                    exp[i][j] = [exp[i][j], True]
                    if not(var in vars):
                        vars.append(var)
    
    def internal_brute_force(exp, k):
        #subfunción recursiva
        if k == len(vars):
            #print(exp)
        
            for disjunction in exp:
                test = False
                for var in disjunction:
                    if var[1]:
                        test = var
                if not(test):
                    return [False, []]
            return [True, exp]
        var = vars[k]
        
        #cambiar valor por verdadero
        for i in range(len(exp)):
            for j in range(len(exp[i])):
                if var == exp[i][j][0]:
                    exp[i][j][1] =  True
                    
                if var == exp[i][j][0][1:]:
                    exp[i][j][1] =  False
        #probar con verdadero
        t, r = internal_brute_force(exp, k+1)
        if t:
            return [True, r]
        #cambiar valor a falso
        for i in range(len(exp)):
            for j in range(len(exp[i])):
                    
                if var == exp[i][j][0]:
                    exp[i][j][1] = False
                    
                if var == exp[i][j][0][1:]:
                    exp[i][j][1] =  True
        #probar con falso
        t, r = internal_brute_force(exp, k+1)
        if t:
            return [True, r]
        return [False, []]
    return internal_brute_force(exp, 0)


t, r = bruteforceSAT(expresion)
print('Satisfactorio: ')
print(t)
print('Expresión: ')
print(r)