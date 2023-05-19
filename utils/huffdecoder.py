# encoding =utf-8
"""
author:renyubin
date:20201210
function:huffman decoding
"""
from utils.huffman import *


# import six
def huffdecode(codewords, char_weight):
    # 只有空字节的时候
    if codewords == [] and char_weight == {}:
        return []
    # 计算多个字节的个数
    num_non_bytes = 0
    for key in char_weight.values():
        num_non_bytes = int(key)
    # 正常情况
    hufftrees_list = []
    for symbol in char_weight.keys():
        tem_tree = HuffTree(0, symbol, char_weight[symbol], None, None, None
                            , None, None, None, None, None, None, None, None
                            )
        hufftrees_list.append(tem_tree)
    # start the huffman encode and count the leaf node number
    leaf_node_num = len(char_weight.keys())
    # build the huffman tree,and acquire the huffman code for source symbol
    hufftree = build_huff_tree(hufftrees_list, len(char_weight.keys()))
    # char_weight final format is [symbo:codewords]
    hufftree.recursive_trav_tree(hufftree.get_root(), char_weight, [])

    # use the huffman tree build in the previous step
    symbols = []
    currnode = hufftree.get_root()
    if codewords == []:  # 当原序列任意空字节时
        for key in char_weight.keys():
            # 原始自己有多个自己是就增加几个空字节
            for i in range(num_non_bytes):
                symbols.append(key)

    for code in codewords:
        if currnode.isleaf():
            symbol = currnode.get_value()
            currnode = hufftree.get_root()
            symbols.append(symbol)
        if code == 0:
            currnode = currnode.get_child0()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 1:
            currnode = currnode.get_child1()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 2:
            currnode = currnode.get_child2()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 3:
            currnode = currnode.get_child3()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 4:
            currnode = currnode.get_child4()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 5:
            currnode = currnode.get_child5()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 6:
            currnode = currnode.get_child6()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 7:
            currnode = currnode.get_child7()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 8:
            currnode = currnode.get_child8()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 9:
            currnode = currnode.get_child9()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        elif code == 10:
            currnode = currnode.get_child10()
            if currnode.isleaf():
                symbol = currnode.get_value()
                currnode = hufftree.get_root()
                symbols.append(symbol)
        # elif code == 11:
        #     currnode = currnode.get_child11()
        #     if currnode.isleaf():
        #         symbol = currnode.get_value()
        #         currnode = hufftree.get_root()
        #         symbols.append(symbol)
        # elif code == 12:
        #     currnode = currnode.get_child12()
        #     if currnode.isleaf():
        #         symbol = currnode.get_value()
        #         currnode = hufftree.get_root()
        #         symbols.append(symbol)
        # elif code == 13:
        #     currnode = currnode.get_child13()
        #     if currnode.isleaf():
        #         symbol = currnode.get_value()
        #         currnode = hufftree.get_root()
        #         symbols.append(symbol)
        # elif code == 14:
        #     currnode = currnode.get_child14()
        #     if currnode.isleaf():
        #         symbol = currnode.get_value()
        #         currnode = hufftree.get_root()
        #         symbols.append(symbol)
            else:
                continue

    bytefragment = []
    for symbol in symbols:
        # bytefragment.append((six.int2byte(symbol)))
        bytefragment.append(symbol)
    return bytefragment


def base2code(base):
    """
    碱基序列转换成huffumanCode
    :param base: 碱基序列
    :return: huffumancode列表
    """
    rotation_map = {
        'AC': 0,
        'AG': 1,
        'AT': 2,
        'CA': 3,
        'CG': 4,
        'CT': 5,
        'GA': 6,
        'GC': 7,
        'GT': 8,
        'TA': 9,
        'TC': 10,
        'TG': 11,
    }
    code = []
    last_index = 0
    for index, s in enumerate(base):
        if index % 2 == 1:
            current_index = rotation_map[base[index - 1] + s]
            current_code = current_index - last_index
            if current_index < last_index:
                current_code = 12 - last_index + current_index
            code.append(current_code)
            last_index = (current_index + 1) % 12
    return code

