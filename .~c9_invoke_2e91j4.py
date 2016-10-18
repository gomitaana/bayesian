import fileinput
import sys
#./run < testcases/alarm.in

if __name__ == '__main__':
    input   =   []
    flag    =   0
    nodes   =   []
    
    # Read each input line
    for line in sys.stdin:
        # sys.stdout.write(line)
        line = line.strip("\n")
        #Aqui hay que hacer split d

    for idx, line in enumerate(input):
    if line.startswith("[Nodes]"):
        nodes = input[idx + 1].split(", ")
    if line.startswith("[Probabilities]"):
        new_list = list(input)
        for prob in itertools.islice(new_list, idx+1, None):
            if not prob.startswith("[Queries]"):
                new = prob.split(" = ")
                if not new[0]=='':
                    print(new[1])
                    dict.update({new[0]: float(new[1])})
            else:
                break