
expresion = [['!p'],['p', 'q'], ['p' , '!q', '!x', '!z'], ['p']]
tested_info = {}



def bruteforceSAT(exp, k = 0):
    global tested_info
    if (len(expresion) == 0):
        return True
    if len(tested_info) == 0:
        access = 0
        for i in range(len(expresion)):
                for j in range(len(expresion[i])):
                    var = expresion[i][j]
                    if var[0] == '!':
                        var = var[1:]
                    exp[i][j] = [expresion[i][j], True]
                    if not(var in tested_info.keys()):
                        tested_info[var] = access
                        access += 1
        print(tested_info)
    if k == len(tested_info.keys()):
        print(exp)
        
        for disjunction in expresion:
            test = False
            for var in disjunction:
                if var[1]:
                    test = var
            if not(test):
                return False
        return True
    for var in tested_info.keys():
        if tested_info[var] != k:
            continue
        tested_info[var] = k
        #if var:
        #    print(var)
        #    print(k)

        for i in range(len(exp)):
            for j in range(len(exp[i])):
                if var == exp[i][j][0]:
                    exp[i][j][1] =  True
                    
                if var == exp[i][j][0][1:]:
                    exp[i][j][1] =  False


        if bruteforceSAT(exp, k+1):
            return True

        for i in range(len(expresion)):
            for j in range(len(exp[i])):
                    
                if var == exp[i][j][0]:
                    exp[i][j][1] = False
                    
                if var == exp[i][j][0][1:]:
                    exp[i][j][1] =  True
                   

        if bruteforceSAT(exp, k+1):
            return True
    return False

print(bruteforceSAT(expresion))