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
            for node in layer.nodes:
                print(node.print_node())

    def make_random_connections(self):
        # like a zero reset
        for layer in self.net:
            for nlayer in self.net:
                if (nlayer.lnum - layer.lnum) == 1:
                    for node in layer.nodes:
                        for nnode in nlayer.nodes:
                            node.make_connection(nnode)
                            
    
    def load_first(self, inputs):
        for i in range(0, len(inputs)):
            if len(inputs) != len(self.net[0].nodes):
                print('invalid size ')
                break
            self.net[0].nodes[i].val = inputs[i]


    def propagate_forward(self):
        for layer in self.net:
            if layer.lnum == len(self.net ) - 1:
                print(layer.lnum)
                for lnode in self.net.pop().nodes:
                    print('Output :', lnode.val)

            for node in layer.nodes:
                for connection in node.connections:
                    connection.print_connection()
                    # connection.print_connection()
                    # print(connection)
                    connection.to_whomst.set_val(connection.from_whome.val * connection.weight)

                    print('Node value ' ,node.val, ' , ', connection.to_whomst.val , ' = ', connection.from_whome.val, ' * ', connection.weight, ' + ', connection.to_whomst.bias)
            

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
        self.val = 0

        if lnum == 0:
            self.bias = 1
        else:
        # random.uniform(-1.0, 1.0)
            self.bias = 1
        # print("layer ", lnum, " node ", nnum)

    def make_connection(self, next_layer_node): # the connection will take the current node and another node that is passed in

        # random.uniform(-1.0, 1.0)
        self.connections.append(Connection(1, self , next_layer_node))
        # for print testing 
        # print(   "connection between ", self.whoami(), next_layer_node.whoami()   )
        # self.connections.pop().print_connection()

    def set_val(self, val):
        self.val += val

    def whoami(self):
        return self.lnum, self.nnum

    def print_node(self):
        #print('layer num: ', self.lnum, ' node number: ', self.nnum)
        for connection in self.connections:
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
# nnet.print_net()
nnet.make_random_connections()

nnet.load_first([2 ,6])
nnet.propagate_forward()

#nnet.print_net()
