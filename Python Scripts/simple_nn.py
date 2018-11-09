import numpy
import math



class Net():
    def __init__(self, lstruc):
        self.lstruc = lstruc
        self.net = [] # container with 3 slots to hold the struc with nets that hold nodes that have connections 


    def create_net(self):
        for i , Nnodes in enumerate(self.lstruc):
            self.net.append(Lay(Nnodes, i))

    def print_net(self):
        for layer in self.net:
            layer.print_size()
            layer.print_layer()

class Lay:
    def __init__(self, Nnodes, lnum):
        self.Nnodes = Nnodes #number of nodes in this layer
        self.lnum = lnum
        self.nodes = []
        for i in range(0, Nnodes):
            self.nodes.append(Node(lnum, i))

    def print_size(self):
        print(self.lnum, self.Nnodes)

    def print_layer(self):
        for node in self.nodes:
            #print(node.)
            pass
    
class Node:
    def __init__(self, lnum, nnum):
        self.lnum = lnum
        self.nnum = nnum    
        print("NODE layer ", lnum, " node ", nnum)

    
class connection:
    def __init__(self, weight, from_whome, to_whomst):
        self.weight = weight
        self.from_whome = from_whome
        self.to_whomst = to_whomst
    
net = Net([2,3,1])

net.create_net()
net.print_net()