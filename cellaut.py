# Basic 1-dimensional Cellular Automaton
# cellular_automaton() takes 3 arguments:
# - initial string of dots and x's
# - seed pattern (0-255)
# - number of generations to print

def pattern_interpret(pattern):
    rules = []
    p = range(0,8)
    p.reverse()
    for e in p:
        if pattern - 2 ** e >= 0:
            rules.append(2 ** e)
            pattern = pattern - 2 ** e
    return rules

def makenextgen(string, rules):
    d = len(string)
    newstring = []
    stringmod = string[-1] + string + string[0]
    for e in range(0, d+1):
        if e == d:
            break
        if stringmod[e] == '.':
            if stringmod[e+1] == '.':
                if stringmod[e+2] == '.':
                    if 1 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
                else:
                    if 2 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
            else:
                if stringmod[e+2] == '.':
                    if 4 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
                else:
                    if 8 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
        else:
            if stringmod[e+1] == '.':
                if stringmod[e+2] == '.':
                    if 16 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
                else:
                    if 32 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
            else:
                if stringmod[e+2] == '.':
                    if 64 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
                else:
                    if 128 in rules:
                        newstring.append('x')
                    else:
                        newstring.append('.')
    output = ''.join(newstring)
    return output
    
def cellular_automaton(string, pattern, n):
    rules = pattern_interpret(pattern)
    result = makenextgen(string, rules)
    if n == 1:
        print result
        return
    else:
        print result
        return cellular_automaton(result, pattern, n-1)