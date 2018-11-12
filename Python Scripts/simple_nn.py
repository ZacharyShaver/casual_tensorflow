import numpy
import math
import random


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

    def make_random_connections(self):
        # like a zero reset
        for layer in self.net:
            for nlayer in self.net:
                if (nlayer.lnum - layer.lnum) == 1:
                    for node in layer.nodes:
                        for nnode in nlayer.nodes:
                            node.make_connection(nnode)
            

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
            node.whoami()
    

class Node:
    def __init__(self, lnum, nnum):
        self.lnum = lnum
        self.nnum = nnum    
        self.connections = []

        if lnum == 0:
            self.bias = 1
        else:
            self.bias = random.uniform(0.0, 1.0)
        print("layer ", lnum, " node ", nnum)

    def make_connection(self, next_layer_node): # the connection will take the current node and another node that is passed in 
        self.connections.append(Connection(random.uniform(0.0, 1.0), self , next_layer_node))
        #print(   "connection between ", self.whoami(), next_layer_node.whoami()   )
        self.connections.pop().print_connection()

    def whoami(self):
        return self.lnum, self.nnum

    def print_node(self):
        #print('layer num: ', self.lnum, ' node number: ', self.nnum)
        for connection in self.connecitons:
            connection.print_connection()


class Connection:
    def __init__(self, weight, from_whome, to_whomst):
        self.weight = weight
        self.from_whome = from_whome
        self.to_whomst = to_whomst

    def whoami(self):
        return self.weight, self.from_whome, self.to_whomst

    def print_connection(self):
        print(self.from_whome.whoami(), ' bias ', self.from_whome.bias , ' ----> ', self.to_whomst.whoami(), ' bias ', self.to_whomst.bias , ' WEIGHT', self.weight)
    

nnet = Net([2,3,2])

nnet.create_net()
nnet.print_net()
nnet.make_random_connections()