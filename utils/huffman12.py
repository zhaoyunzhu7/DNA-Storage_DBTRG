# -*- coding：utf-8 -*-
import os.path
from huffencoder import *
from utils.fake_random import *


def getFakeRandom(origin_seq):
    """
    生成伪随机序列
    return 伪随机序列，压缩后碱基长度
    """
    origin_len = len(origin_seq)
    # print('原始的序列；', origin_seq)
    random_sequence, new_sequence = fake_random(origin_seq)
    print("伪随机序列：", random_sequence)
    # print("异或后序列：", new_sequence)
    base_seq, base_compress = generate_base(new_sequence)
    # print("对应的碱基：", base_seq)

    # print("GC占比：{}/{} = {}".format(base_seq.count("C") + base_seq.count("G"), len(base_seq) - base_seq.count(","),
    #                                (base_seq.count("C") + base_seq.count("G")) / (len(base_seq) - base_seq.count(","))))

    print("原始压缩后碱基：", base_compress)


    # encode_rate = origin_len, int(len(random_sequence)/2 + len(base_compress))
    # print("伪随机序列长度：{}，压缩后碱基长度：{}， 原始序列长度：{}".format(len(random_sequence), len(base_compress), origin_len))
    # print(f"编码率：{encode_rate[0]}/{encode_rate[1]} = {encode_rate[0]/encode_rate[1]}", )

    return random_sequence, len(base_compress)

if __name__ == '__main__':

    # 原始二进制序列文件
    img_file = "../bin_data/4.txt"
    # 原始序列to伪随机序列 切分短序列长度
    origin_short_length = 6  # 序列长度要求是6的整数倍(三个碱基一组）
    # 伪随机序列to碱基 每段短序列长度（自行调整，不同数值对编码率有影响）
    short_seq_len = 8

    # 图片文件比特大小
    img_size = os.path.getsize(img_file) * 8
    with open(img_file) as f:
        origin_bin_str = f.read()
    origin_bin_str = origin_bin_str.replace("\n", "").replace(" ", "")
    # origin_bin_str = "01010101010001011010101010"
    remainder = len(origin_bin_str) % origin_short_length
    origin_len = len(origin_bin_str)
    print('原始序列长度：', origin_len, "余数：", remainder)
    # 序列长度要求同时是6和8的整数倍 -- 即24的倍数
    # 如果长度不满足则在末尾补零
    if remainder != 0:
        print("序列长度不符合要求，在结尾补零...")
        for i in tqdm(range(origin_short_length - remainder)):
            origin_bin_str += "0"
            # pass
    with open('../bin_data/img.txt', 'w') as f:
        f.write(origin_bin_str)
    assert len(origin_bin_str) % origin_short_length == 0
    bin_str, base_compress_len = getFakeRandom(origin_bin_str)
    # ==============伪随机序列转碱基↓↓====================
    if len(bin_str) % short_seq_len != 0:
        print(f'当前序列长度不满足要求：是{short_seq_len}的整数倍！当前余数为{len(bin_str) % short_seq_len}')
        print('已经自动完成填充操作（结尾补0）')
        bin_str += ''.join(['0' for i in range(short_seq_len - len(bin_str) % short_seq_len)])
        print(bin_str)
    dec_list = bin2dec(bin_str, short_seq_len)
    print('二进制字串：', bin_str)
    # print('转换十进制：', dec_list)
    codewords, char_freq = huffencode(dec_list)
    print('Huffman code：', codewords, char_freq)
    base_squence = code2base(codewords)
    print('伪随机序列-->碱基序列：', base_squence)
    # print('解码结果：', huffdecode(codewords, char_freq))
    print(len(dec_list), len(codewords))

    # print(
    #     f'图片文件大小（比特）：{img_size}，原始二进制序列长度&伪随机序列：{origin_len}，伪随机序列碱基长度：{len(base_squence)}，原始序列碱基长度：{base_compress_len}\n'
    #     f'编码率：{origin_len}/（{len(base_squence)}+{base_compress_len}）={origin_len / (len(base_squence)+base_compress_len)}')
    print(
        f'伪随机序列：{origin_len}，伪随机序列碱基长度：{len(base_squence)}\n'
        f'编码率：{origin_len}/（{len(base_squence)}）={origin_len / (len(base_squence))}')
    print('GC占比：', (base_squence.count("C") + base_squence.count("G")) / len(base_squence))

#     这才是程序的主入口