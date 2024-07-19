import enum
import numpy as np




class Node:
    Node1 = None
    Node2 = None
    Value = None
    

    Function = None
    def __init__(self, k):
        self.Value = k


def run(Tests, Network:list[Node]):

    out = np.zeros(len(Tests))
    l = 0
    for k in Tests:
        TmpNet = Network.copy()   
        i = 0
        for j in range(len(TmpNet) - len(k), len(TmpNet) - 1):
            
            p = False
            if(Tests[i] == 1):
                p == True
            
            TmpNet[j].Value = p
            i+=1



        while(True):
            if(TmpNet[0].Value!=None):
                if(TmpNet[0].Value == True):
                    out[l] = 1
                else:
                    out[l] = 0
                break

            for nde in Network:
                if(nde.Node1.Value != None and nde.Node2.Value != None):
                    match nde.Function:
                        case "AND":
                            nde.Value = nde.Node1.Value and nde.Node2.Value
                        case "OR":
                            nde.Value = nde.Node1.Value or nde.Node2.Value
                        case "NAND":
                            nde.Value = not (nde.Node1.Value and nde.Node2.Value)
                        case "NOR":
                            nde.Value = not (nde.Node1.Value or nde.Node2.Value)
        

            
    
