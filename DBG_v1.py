# encoding: utf8


# date: 2022/11/04
import os

import numpy as np

from utils.fake_random import fake_random
from utils.huffdecoder import huffdecode, base2code
from utils.huffencoder import huffencode, code2base, bin2dec


def generate_base(seq):
    """
    生成碱基
    :param seq: 二进制序列
    :return:
    """
    base_map = {
        '00': 'A',
        '01': 'T',
        '10': 'G',
        '11': 'C',
    }
    base_seq = ""
    #print('seq长度：', len(seq))
    # 如果序列长度不是2的倍数，报错
    assert len(seq) % 2 == 0
    base_key = ""
    base_compress = ""
    base_seq_length = 0
    for index, val in enumerate(seq):
        if type(val) == int:
            val = str(val)
        if index % 2 == 0:
            base_key = val
        else:
            base_seq += base_map[base_key + val]
            base_seq_length += 1
            if base_seq_length < 3 or base_seq_length % 3 == 0:
                base_compress += base_map[base_key + val]

        if index > 0 and index % 6 == 0:
            base_seq += ","
    # 如果碱基长度不是3的倍数，报错
    if base_seq_length % 3 != 0:
        print("当前碱基length不符合要求，长度：", base_seq_length, base_seq_length % 3)
    assert base_seq_length % 3 == 0
    return base_seq, base_compress


def generate_base_normal(seq):
    """
    生成碱基
    :param seq: 二进制序列
    :return:
    """
    base_map = {
        '00': 'A',
        '01': 'T',
        '10': 'G',
        '11': 'C',
    }
    base_seq = ""
    # 如果序列长度不是2的倍数，报错
    assert len(seq) % 2 == 0
    base_key = ""
    for index, val in enumerate(seq):
        if type(val) == int:
            val = str(val)
        if index % 2 == 0:
            base_key = val
        else:
            base_seq += base_map[base_key + val]

    return base_seq


def base2bin(seq):
    """
    碱基转二进制
    :param seq: 碱基序列
    :return:
    """
    base_map = {
        'A': '00',
        'T': '01',
        'G': '10',
        'C': '11',
    }
    bin_seq = ""
    # 如果序列长度不是2的倍数，报错
    assert len(seq) % 2 == 0
    for index, val in enumerate(seq):
        bin_seq += base_map[val]
    return bin_seq

global test_o2


def encoder(origin_bin, origin_short_length, short_seq_len, img_size):
    global test_o2
    #print("current 原始序列长度:", len(origin_bin), f'对{origin_short_length}取余后:', len(origin_bin) % origin_short_length)
    assert len(origin_bin) % origin_short_length == 0

    split_len = len(origin_bin) // 2
    o1 = origin_bin[:split_len]
    o2 = origin_bin[split_len:]
    test_o2 = o2
    #print("原始序列拆分 O1、O2：", o1, o2)
    #print("原始序列拆分  O2：",   o2)
    m = ''
    for i in range(split_len):
        m += str(int(o1[i]) ^ int(o2[i]))
    #print("O1、O2异或后 M：", m)
    #print('获取伪随机-----------')
    n = fake_random(m)[0]
    #print("M的伪随机序列 N：", n)
    A = ''
    for i in range(len(n)):
        A += str(int(n[i]) ^ int(m[i]))
    #print("M、N异或后 A：", A)
    base_A = generate_base(A)[1]
    #print("A压缩后碱基：", base_A)

    # 计算编码率

    # base_N = generate_base_normal(n)
    # print("N压缩后碱基：", base_N)
    # base_O1 = generate_base_normal(o1)
    # print("O1压缩后碱基：", base_O1)

    # ==============N、O1利用12元霍夫曼转碱基↓↓====================

    dec_list = bin2dec(n, short_seq_len)
    #print('转换十进制：', dec_list)
    codewords, char_freq_N = huffencode(dec_list)
    #print('Huffman code：', codewords, char_freq_N)
    base_N = code2base(codewords)
    #print('N-->碱基序列：', base_N)
    # print('解码结果：', huffdecode(codewords, char_freq))
    #print(len(dec_list), len(codewords))

    dec_list = bin2dec(o1, short_seq_len)
    #print('转换十进制：', dec_list)
    codewords, char_freq_o1 = huffencode(dec_list)
    #print('Huffman code：', codewords, char_freq_o1)
    base_O1 = code2base(codewords)
    #print('O1-->碱基序列：', base_O1)


    print(f"编码率：{img_size}/({len(base_A)}+{len(base_N) + len(base_O1)}) =",
          img_size / (len(base_A) + len(base_N) + len(base_O1)))
    base_sequence = base_O1 + base_N + base_A
    print('GC占比：', (base_sequence.count("C") + base_sequence.count("G")) / len(base_sequence))

    return base_O1, char_freq_o1, base_N, char_freq_N, base_A

def decoder(base_o1, char_freq_o1, base_N, char_freq_N, base_A, hand_0):
    """
    解码
    :param base_o1:
    :param base_N:
    :param baseA: 碱基数据
    :return:
    """
    global test_o2
    # 获取压缩前原始碱基
    base_A1 = ""
    for index, base in enumerate(base_A):
        if index >= 3:
            base_A1 += base_A[index - 2]
            base_A1 += base_A[index - 1]
        base_A1 += base
    #print('base_A1', base_A1)

    bin_A = base2bin(base_A1)
    #print('bin_A', bin_A)

    #print('base_N', base_N)
    #print('base_o1', base_o1)
    bin_N = huffdecode(base2code(base_N), char_freq_N)
    bin_o1 = huffdecode(base2code(base_o1), char_freq_o1)

    # 列表转字符串
    bin_N = ''.join(bin_N)
    bin_o1 = ''.join(bin_o1)

    # print('bin_N', bin_N)
    # print('bin_o1', bin_o1)

    bin_M = ''
    for index in range(len(bin_A)):
        bin_M += str(int(bin_A[index]) ^ int(bin_N[index]))

    bin_o2 = ''
    for index in range(len(bin_M)):
        bin_o2 += str(int(bin_M[index]) ^ int(bin_o1[index]))

    #print('bin_o2', bin_o2)
    #print('test_o2', test_o2)
    assert test_o2 == bin_o2

    bin_o = bin_o1 + bin_o2

    decode1 = bin_o[:len(bin_o) - hand_0]

    #print(decode1)
    return decode1


def encode_test(origin_bin):
    # 图片文件比特大小
    img_size = os.path.getsize("bin_data/1.jpg") * 8

    # 1，2和4和6，7:24
    # 原始序列to伪随机序列 切分短序列长度
    origin_short_length = 12  # 序列长度要求是6的整数倍(三个碱基一组）,由于序列折半分割后要求是2的倍数，所以同时要求原始序列长度是4的倍数
    # 序列to碱基 每段短序列长度
    short_seq_len = 24
    return encoder(origin_bin, origin_short_length, short_seq_len, img_size)


if __name__ == "__main__":

    hand_0 = 0

    # 原始二进制序列
    # origin_bin = "101011100101000101101011100101000101100001111001010001111001010111001010001010101101101100010101"

    with open("bin_data/1.txt") as f:
        origin_bin = f.read().strip()
        origin_bin = origin_bin.replace(" ", "").replace("\n", "")

    base_O1, char_freq_o1, base_N, char_freq_N, base_A = encode_test(origin_bin)
    # 保存编码baseA
    with open("bin_data/encode_1.txt", 'w') as f:
        f.write(base_A)
    print('编码结果保存完成！')



    decode = decoder(base_O1, char_freq_o1, base_N, char_freq_N, base_A, hand_0)

    #保存解码结果
    with open("bin_data/decode_1.txt", 'w') as f:
       f.write(decode)
    print('解码结果保存完成！')



    # 原始序列to伪随机序列 切分短序列长度
    origin_short_length = 12  # 序列长度要求是6的整数倍(三个碱基一组）,由于序列折半分割后要求是2的倍数，所以同时要求原始序列长度是4的倍数
    # 序列to碱基 每段短序列长度
    short_seq_len = 24
    img_size = os.path.getsize("bin_data/1.jpg") * 8
    #encoder(origin_bin, origin_short_length, short_seq_len,img_size)