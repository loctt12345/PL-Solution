def negative_each_other(c1, c2):
    nega_c1 = c1[0] == '-'
    nega_c2 = c2[0] == '-'
    x1 = "".join(c1.split('-'))
    x2 = "".join(c2.split('-'))
    if (x1 == x2 and nega_c1 != nega_c2):
        return True
    return False

def order(c):
    if (len(c)==2):
        return c[1]
    return c

def read_input():
    f = open("input.txt", "r")
    alpha = "".join(f.readline().strip().split())
    n = int(f.readline())
    KB = []
    for i in range(n):
        tmp = "".join(f.readline().strip().split())
        KB.append(tmp)
    f.close()
    return alpha, n, KB

def unuseful_clause(c):
    if c == "":
        return False
    c_split = c.split("OR")
    #print(c_split)
    for x in c_split:
        for y in c_split:
            if (negative_each_other(x, y)):
                return True
    return False;


def PL_resolve(c1, c2):
    c1_split = c1.split("OR")
    c2_split = c2.split("OR")
    new_clause = []
    for x in c1_split:
        for y in c2_split:
            if (negative_each_other(x, y)):
                c1_new = c1.split("OR")
                c2_new = c2.split("OR")
                c1_new.remove(x)
                c2_new.remove(y)
                clause = c1_new + c2_new
                clause = list(set(clause))
                clause.sort(key=order)
                clause = "OR".join(clause)
                if (not unuseful_clause(clause)):
                    new_clause.append(clause)
    return new_clause

def negative_of_literal(literal):
    if literal[0] == '-':
        return literal[1]
    return '-' + literal

def negative_of_clause(c):
    c_split = c.split("OR")
    new_clause = []
    for x in c_split:
        new_clause.append(negative_of_literal(x))
    return new_clause

def PL_resolution(alpha, KB):
    negative_of_alpha = negative_of_clause(alpha)
    for x in negative_of_alpha:
        KB.append(x)
    #print(KB)
    trace = []
    new = []
    while True:
        new_resolvents = []
        for i in range(len(KB)):
            for j in range(i + 1, len(KB)):
                resolvents = PL_resolve(KB[i], KB[j])
                #print(resolvents)
                for x in resolvents:
                    if (not x in KB and not x in new):
                        new_resolvents.append(x)
                        new.append(x)
        trace.append(str(len(new_resolvents)))
        for x in new_resolvents:
            if x == "":
                trace.append("{}")
            else:
                trace.append(" OR ".join(x.split("OR")))
        if ("" in new_resolvents):
            return trace, True
        if set(new).issubset(set(KB)):
            return trace, False

        for x in new:
            KB.append(x)

def write_output(trace, result):
    f = open("output.txt", "w")
    f.write("\n".join(trace))
    if (result):
        f.write("\nYES")
    else:
        f.write("\nNO")
    f.close()

def main():
    alpha, _, KB = read_input()
    trace, result = PL_resolution(alpha, KB)
    write_output(trace, result)
    #print(KB[2].split("OR"))
    #print(negative_of_literal('A'))

if __name__=="__main__":
    main()  
