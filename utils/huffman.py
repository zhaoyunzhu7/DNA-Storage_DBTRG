# encoding=utf-8
"""
author:renyubin
date:20201210
function:build huffman tree by treelib
license:Redistributed under Apache License (2.0) since version 1.3.0
"""

from treelib import Tree, Node
import math
import copy


class LeafNode(Node):
    """
    function:the leafnode of huffman trees is mapping to [0-255]
    """

    def __init__(self, value=0, weight=0):
        super(LeafNode, self).__init__()
        # the value of node
        self.value = value
        self.weight = weight

    def isleaf(self):
        return True

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value


class InterNode(Node):

    def __init__(self, child_node0=None, child_node1=None, child_node2=None,
                 child_node3=None, child_node4=None, child_node5=None,
                 child_node6=None, child_node7=None, child_node8=None,
                 child_node9=None, child_node10=None, child_node11=None,
                 # child_node12=None, child_node13=None, child_node14=None
                 ):
        super(InterNode, self).__init__()
        # 节点的权重
        if child_node0 == None:
            self.weight = self.get_weight()
            self.child_node_num=0
        elif child_node1 == None:
            self.weight = child_node0.get_weight()
            self.child_node_num = 1
        elif child_node2 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight()
            self.child_node_num = 2
        elif child_node3 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            self.child_node_num = 3
        elif child_node4 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight() \
                          + child_node3.get_weight()
            self.child_node_num = 4
        elif child_node5 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight()
            self.child_node_num = 5
        elif child_node6 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
            self.child_node_num = 6
        elif child_node7 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight() \
            + child_node6.get_weight()
            self.child_node_num = 7
        elif child_node8 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
            +child_node6.get_weight() + child_node7.get_weight()
            self.child_node_num = 8
        elif child_node9 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
            +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
            self.child_node_num = 9
        elif child_node10 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
            +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight() \
            + child_node9.get_weight()
            self.child_node_num = 10
        elif child_node11 == None:
            self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
            +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
            +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
            +child_node9.get_weight() + child_node10.get_weight()
            self.child_node_num = 11
        # elif child_node12 == None:
        #     self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
        #     +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
        #     +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
        #     +child_node9.get_weight() + child_node10.get_weight() + child_node11.get_weight()
        #     self.child_node_num = 12
        # elif child_node13 == None:
        #     self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
        #     +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
        #     +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
        #     +child_node9.get_weight() + child_node10.get_weight() + child_node11.get_weight() \
        #     + child_node12.get_weight()
        #     self.child_node_num = 13
        # elif child_node14 == None:
        #     self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
        #     +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
        #     +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
        #     +child_node9.get_weight() + child_node10.get_weight() + child_node11.get_weight()
        #     +child_node12.get_weight() + child_node13.get_weight()
        #     self.child_node_num = 14
        # else:
        #     self.weight = child_node0.get_weight() + child_node1.get_weight() + child_node2.get_weight()
        #     +child_node3.get_weight() + child_node4.get_weight() + child_node5.get_weight()
        #     +child_node6.get_weight() + child_node7.get_weight() + child_node8.get_weight()
        #     +child_node9.get_weight() + child_node10.get_weight() + child_node11.get_weight()
        #     +child_node12.get_weight() + child_node13.get_weight()+ child_node14.get_weight()
        #     self.child_node_num = 15
        self.child_node0 = child_node0
        self.child_node1 = child_node1
        self.child_node2 = child_node2
        self.child_node3 = child_node3
        self.child_node4 = child_node4
        self.child_node5 = child_node5
        self.child_node6 = child_node6
        self.child_node7 = child_node7
        self.child_node8 = child_node8
        self.child_node9 = child_node9
        self.child_node10 = child_node10
        self.child_node11 = child_node11
        # self.child_node12 = child_node12
        # self.child_node13 = child_node13
        # self.child_node14 = child_node14


    def isleaf(self):
        if self.child_node0 == None:  # have no child node
            return True
        else:
            return False

    def get_weight(self):
        return self.weight

    def get_child0(self):
        return self.child_node0

    def get_child1(self):
        return self.child_node1

    def get_child2(self):
        return self.child_node2

    def get_child3(self):
        return self.child_node3

    def get_child4(self):
        return self.child_node4

    def get_child5(self):
        return self.child_node5

    def get_child6(self):
        return self.child_node6

    def get_child7(self):
        return self.child_node7

    def get_child8(self):
        return self.child_node8

    def get_child9(self):
        return self.child_node9

    def get_child10(self):
        return self.child_node10

    def get_child11(self):
        return self.child_node11

    # def get_child12(self):
    #     return self.child_node12
    #
    # def get_child13(self):
    #     return self.child_node13
    #
    # def get_child14(self):
    #     return self.child_node14


    def get_root(self):
        return self.get_root()

    def get_child_node_num(self):
        return self.child_node_num

    def get_child_node(self,i):
        if i==0:
            return self.child_node0
        elif i==1:
            return self.child_node1
        elif i==2:
            return self.child_node2
        elif i==3:
            return self.child_node3
        elif i==4:
            return self.child_node4
        elif i==5:
            return self.child_node5
        elif i==6:
            return self.child_node6
        elif i==7:
            return self.child_node7
        elif i==8:
            return self.child_node8
        elif i==9:
            return self.child_node9
        elif i==10:
            return self.child_node10
        elif i==11:
            return self.child_node11
        # elif i==12:
        #     return self.child_node12
        # elif i==13:
        #     return self.child_node13
        # elif i==14:
        #     return self.child_node14




class HuffTree(Tree):
    def __init__(self, flag, value=0, freq=0, child_tree0=None, child_tree1=None,
                 child_tree2=None, child_tree3=None, child_tree4=None,
                 child_tree5=None, child_tree6=None, child_tree7=None,
                 child_tree8=None, child_tree9=None, child_tree10=None):
        super(HuffTree, self).__init__()
        assert flag < 12
        if flag == 0:
            self.root = LeafNode(value, freq)
        elif flag == 1:
            self.root = InterNode(child_tree0.get_root())
        elif flag == 2:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root())
        elif flag == 3:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root())
        elif flag == 4:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root())
        elif flag == 5:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root())
        elif flag == 6:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root())
        elif flag == 7:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
                                  child_tree6.get_root())
        elif flag == 8:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
                                  child_tree6.get_root(), child_tree7.get_root())
        elif flag == 9:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
                                  child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root())
        elif flag == 10:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
                                  child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
                                  child_tree9.get_root())
        elif flag == 11:
            self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
                                  child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
                                  child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
                                  child_tree9.get_root(), child_tree10.get_root())
        # elif flag == 12:
        #     self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
        #                           child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
        #                           child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
        #                           child_tree9.get_root(), child_tree10.get_root(), child_tree11.get_root())
        # elif flag == 13:
        #     self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
        #                           child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
        #                           child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
        #                           child_tree9.get_root(), child_tree10.get_root(), child_tree11.get_root(),
        #                           child_tree12.get_root())
        # elif flag == 14:
        #     self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
        #                           child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
        #                           child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
        #                           child_tree9.get_root(), child_tree10.get_root(), child_tree11.get_root(),
        #                           child_tree12.get_root(), child_tree13.get_root())
        # elif flag == 15:
        #     self.root = InterNode(child_tree0.get_root(), child_tree1.get_root(), child_tree2.get_root(),
        #                           child_tree3.get_root(), child_tree4.get_root(), child_tree5.get_root(),
        #                           child_tree6.get_root(), child_tree7.get_root(), child_tree8.get_root(),
        #                           child_tree9.get_root(), child_tree10.get_root(), child_tree11.get_root(),
        #                           child_tree12.get_root(), child_tree13.get_root(), child_tree14.get_root())


    def get_root(self):
        return self.root

    def get_weight(self):
        return self.root.get_weight()


    def recursive_trav_tree(self, root, char_weight, code):
        """
         Use the recursive method to traverse the huffman_tree, and in this way
         get the huffman code corresponding to each character and save it in the dictionary char_freq.
        """
        if root.isleaf():
            char_weight[root.get_value()] = code
            # print("it = %c  and  freq = %d  code = %s".format(chr(root.get_value()), root.get_weight(), code))
            return None
        for i in range(root.get_child_node_num()):
            child_node=root.get_child_node(i)
            child_code=list()
            child_code.extend(code)
            child_code.append(i)
            self.recursive_trav_tree(child_node,char_weight,child_code)



def build_huff_tree(hufftrees_list, N):
    """
    funtion:build huffman tree
    :param hufftrees_list:
    :parm N:source symbol number,Determine the number of nodes to merge for the first time
    :return:huffman tree
    """
    times = 1  # identify the first times of merging nodes
    re_num = int(math.fmod(N, (11-1))) #15 branchs huffman tree
    #when int(math.fmod(m,(15-1)))==re_num,select the m
    if len(hufftrees_list)==1 and times==1:
        times+=1
        return hufftrees_list[0]

    while len(hufftrees_list) >1:
        # sort the huffman tree of the hufftrees_list by weight
        hufftrees_list.sort(key=lambda tree: tree.get_weight())
        # select the fourteen  least  hufftree based the weights
        trees_selected = []  # select the trees
        if re_num >1 and times == 1:
            times += 1
            for i in range(re_num):
                trees_selected.append(hufftrees_list[i])

            hufftrees_list = hufftrees_list[re_num:]  # update the hufftrees_list
            # build a new huffman tree
            if re_num == 2:
                hufftree_new = HuffTree(2, 0, 0, trees_selected[0], trees_selected[1])
                hufftrees_list.append(hufftree_new)
            elif re_num == 3:
                hufftree_new = HuffTree(3, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2])
                hufftrees_list.append(hufftree_new)
            elif re_num == 4:
                hufftree_new = HuffTree(4, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3])
                hufftrees_list.append(hufftree_new)
            elif re_num == 5:
                hufftree_new = HuffTree(5, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3], trees_selected[4])
                hufftrees_list.append(hufftree_new)
            elif re_num == 6:
                hufftree_new = HuffTree(6, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3], trees_selected[4], trees_selected[5])
                hufftrees_list.append(hufftree_new)
            elif re_num == 7:
                hufftree_new = HuffTree(7, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3], trees_selected[4], trees_selected[5], trees_selected[6])
                hufftrees_list.append(hufftree_new)
            elif re_num == 8:
                hufftree_new = HuffTree(8, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3],
                                        trees_selected[4], trees_selected[5], trees_selected[6], trees_selected[7])
                hufftrees_list.append(hufftree_new)
            elif re_num == 9:
                hufftree_new = HuffTree(9, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3],
                                        trees_selected[4], trees_selected[5], trees_selected[6], trees_selected[7],
                                        trees_selected[8])
                hufftrees_list.append(hufftree_new)
            elif re_num == 10:
                hufftree_new = HuffTree(10, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3]
                                        , trees_selected[4], trees_selected[5], trees_selected[6], trees_selected[7],
                                        trees_selected[8], trees_selected[9])
                hufftrees_list.append(hufftree_new)
            elif re_num == 11:
                hufftree_new = HuffTree(11, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2],
                                        trees_selected[3]
                                        , trees_selected[4], trees_selected[5], trees_selected[6], trees_selected[7],
                                        trees_selected[8], trees_selected[9], trees_selected[10])
                hufftrees_list.append(hufftree_new)


        else:
            for i in range(11):
                trees_selected.append(hufftrees_list[i])

            hufftrees_list = hufftrees_list[11:]
            # build a new huffman tree
            hufftree_new = HuffTree(11, 0, 0, trees_selected[0], trees_selected[1], trees_selected[2], trees_selected[3],
                                    trees_selected[4], trees_selected[5], trees_selected[6], trees_selected[7],
                                    trees_selected[8], trees_selected[9], trees_selected[10])#
            hufftrees_list.append(hufftree_new)

    # return the last huffman tree
    return hufftrees_list[0]
