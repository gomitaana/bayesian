import fileinput
import sys
import itertools
#./run < testcases/alarm.in

if __name__ == '__main__':
    input   =   []
    flag    =   0
    nodes   =   []
    queries = []
    dict = {}
    
    # Read each input line
    for line in sys.stdin:
        # sys.stdout.write(line)
        if line[0] != "#":
            line = line.strip("\n")
            input.append(line)
    
    for idx, line in enumerate(input):
        if line.startswith("[Nodes]"):
            nodes = input[idx + 1].split(", ")
        if line.startswith("[Probabilities]"):
            prob_list = list(input)
            for prob in itertools.islice(prob_list, idx+1, None):
                if not prob.startswith("[Queries]"):
                    new = prob.split(" = ")
                    if not new[0]=='':
                        dict.update({new[0]: float(new[1])})
                else:
                    break
        if line.startswith("[Queries]"):
            query_list = list(input)
            for prob in itertools.islice(query_list, idx+1, None):
                queries.append(prob)
    
    # For each of the queries
    if queries[0] in dict:
        print(dict[queries[0]])
    else: 
        #Convert the expression to a division of joint probabilities
        q = (queries[0].split("|"))[0]
        e = (queries[0].split("|"))[1]
        q = q + ","+e
        #find out which variables are “relevant”