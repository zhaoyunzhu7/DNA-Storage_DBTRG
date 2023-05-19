# encoding=utf-8
"""
author:renyubin
date:20201210
function:huffman encoding

"""
import re

from tqdm import tqdm

import copy

from utils.huffman import HuffTree, build_huff_tree


def huffencode(bytefragment):
    """
    function:huffman encode
    :param bytefragment_list
    :return:
    """
    # Count the frequency of ASCII value of byte
    if bytefragment == []:
        return [], {}

    char_freq = {}
    bytes = []
    for i in tqdm(range(len(bytefragment))):
        byte = bytefragment[i]
        bytes.append(byte)
        if byte in char_freq.keys():
            char_freq[byte] += 1
        else:
            char_freq[byte] = 1
    # print("bytes:{}".format(bytes))
    # print the statistics result
    # for byte in char_freq.keys():
    #     print("{}:{}".format(byte,char_freq[byte]))

    char_weight = copy.deepcopy(char_freq)
    # print("char_weight:{}".format(char_weight))
    # build the array of huffman tree for the huffman encode
    hufftrees_list = []  # huffman trees list
    for symbol in tqdm(char_weight.keys()):
        tem_tree = HuffTree(0, symbol, char_weight[symbol], None, None, None
                            , None, None, None, None, None, None, None, None)
        hufftrees_list.append(tem_tree)
    # start the huffman encode and count the leaf node number
    leaf_node_num = len(char_weight.keys())
    # build the huffman tree,and acquire the huffman code for source symbol
    hufftree = build_huff_tree(hufftrees_list, len(char_weight.keys()))
    # print(hufftree)
    hufftree.recursive_trav_tree(hufftree.get_root(), char_weight, [])

    # huffman encode
    codewords = []
    for i in tqdm(range(len(bytefragment))):
        key = bytefragment[i]
        codewords += char_weight[key]

    return codewords, char_freq


def bin2dec(bin, short_seq_len):
    """
    二进制转十进制（每八位）
    :param bin: 二进制字符串
    :param short_seq_len: 每段短序列长度
    :return: 十进制列表
    """
    # 二进制长度要求是[short_seq_len]的倍数
    assert len(bin) % short_seq_len == 0
    bin_list = re.findall(r'.{' + str(short_seq_len) + '}', bin)
    dec_list = bin_list
    # dec_list = []
    # for b in bin_list:
    #     dec_list.append(long(b, 2))
    return dec_list


def code2base(huffman_code):
    """
    huffumanCode转换成碱基序列
    :param huffman_code: huffumancode列表
    :return: 碱基序列
    """
    rotation_map = {
        0: 'AC',
        1: 'AG',
        2: 'AT',
        3: 'CA',
        4: 'CG',
        5: 'CT',
        6: 'GA',
        7: 'GC',
        8: 'GT',
        9: 'TA',
        10: 'TC',
        11: 'TG',
    }
    base_squence = ""
    last_code = 0
    for index, code in enumerate(huffman_code):
        map_index = (last_code + code) % 12
        base_squence += rotation_map[map_index]
        last_code = map_index + 1
    return base_squence
