import fileinput
import sys
import itertools
#./run < testcases/alarm.in

class Node(object):
    def __init__(self, name):
        self.probabilities = {}
        self.ancestors     = []
        self.probability   = -1
        self.name          = name
        
    def updateProbability(self,prob):
        self.probability = prob
    
    def updateAncestors(self,ancestors):
        #Separate
        ancestors= ancestors.split(",")
        new_anc = []
        for an in ancestors:
            #Delete symbols and empty spaces
            new_anc.append(an.replace('+', '').replace('-', ''))
        #Update ancestors
        self.ancestors = new_anc
    
    def updateProbabilities (self,probabilities):
        ancestors_symb = probabilities[0].split(",")
        value = float(probabilities[1])
        name  = '('
        for symbol in ancestors_symb:
            if(symbol.find('+')):
                name += 'True,'
            else:
                name += 'False,'
        name = name[:-1]
        name += ')'
        prob = {name: value}
        self.probabilities.update(prob)
        

if __name__ == '__main__':
    input   = []
    nodes   = {} #dic of nodes to search easy
    queries = []
    
    def getProb(nodeName,sign,bot):
        node = nodes[nodeName]
        botprob = bot
        total = 0.0
        return total

    # Read each input line
    for line in sys.stdin:
        # sys.stdout.write(line)
        if line[0] != "#":
            line = line.strip("\n")
            if line != "":
                input.append(line)
    # Keep info as needed
    for idx, line in enumerate(input):
        if line.startswith("[Nodes]"):
            nodes = {n:Node(n) for n in input[idx + 1].split(", ")}

        if line.startswith("[Probabilities]"):
            prob_list = list(input)
            for prob in itertools.islice(prob_list, idx+1, None):
                if not prob.startswith("[Queries]"):
                    if prob.find('|') == -1:
                        prob = prob.replace(" ", "").split("=")
                        nodes[prob[0].replace(prob[0][:1], '')].updateProbability(prob[1])
                    else:
                        #Guardar antecesores
                        prob = prob.split("|")
                        nodeName=prob[0].replace(prob[0][:1], '')
                        prob = prob[1].replace(" ", "").split("=")
                        if not nodes[nodeName].ancestors:
                            nodes[nodeName].updateAncestors(prob[0])
                        nodes[nodeName].updateProbabilities(prob)
                else:
                    break

        if line.startswith("[Queries]"):
            query_list = list(input)
            for prob in itertools.islice(query_list, idx+1, None):
                queries.append(prob)
    
    #-----------------queries-------------------#
    for query in queries:
        query = query.replace(" ", "")
        if query.find('|') == -1:
            sign = query[0]
            nodeName = query.replace(query[:1], '')
            if nodes[nodeName].probability != -1:
                if sign == '+':
                    print(nodes[nodeName].probability)
                else:
                    aux = float(nodes[nodeName].probability)
                    print((1-aux))
        else:
            top = query.split("|")[0]
            bot = query.split("|")[1]
            if top.find(',') == -1: #top 1
                bot = bot.split(',')
                topNode = top[1:]
                if top[0]=='+':
                    topsign = "True"
                else:
                    topsign = "False"
                #get bottom data
                botData = {}
                for node in bot:
                    if node[0]=='+':
                        aux = "True"
                    else:
                        aux = "False"
                    botData.update({node[1:]:aux})
                print(getProb(topNode,topsign,botData))
            else: #top 2
                top = top.split(',')
                bot = bot.split(',')
                  #get bottom data
                botData = {}
                for node in bot:
                    if node[0]=='+':
                      aux = "True"
                    else:
                      aux = "False"
                    botData.update({node[1:]:aux})
            
                suma = 0
                for t in top:
                    if t[0]=='+':
                      topsign = "True"
                    else:
                      topsign = "False"
                    topNode = t[1:]
                    suma *= getProb(topNode,topsign,botData)
                print(getProb(topNode,topsign,botData))