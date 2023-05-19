import random

def fake_random(origin_seq, short_length=6, reuse_length=4):
    """
    获取伪随机序列 2022.07.31
    :param origin_seq: 原始序列
    :param short_length: 每个短序列长度，默认6
    :param reuse_length: 要求重复的序列长度，默认4
    :return: 伪随机序列、按位组合运算后的新序列
    """
    # 伪随机序列
    random_sequence = ""
    # 运算后的新序列
    new_sequence = ""
    # 短序列中从第几位开始需要和下一条序列重复
    margin_length = short_length - reuse_length
    # 前一段新生成的序列
    reuse_base = [None for i in range(short_length)]
    origin_seq_list = list(origin_seq)
    # 标识，上一组碱基中GC是否超过一半
    last_gc_half = -1
    for index, value in enumerate(origin_seq):
        random_val = None
        # 如果上一个短碱基中gc个数大于等于2，则本组第三个碱基随机成AT,否则GC
        if index > 0 and index % short_length == 0:
            # print(index, reuse_base)
            last_base = generate_base(reuse_base)[0]
            gc_count = last_base.count("G") + last_base.count("C")
            # print(reuse_base, last_base, gc_count)
            if gc_count >= 2:
                last_gc_half = 1
            else:
                last_gc_half = 0
            # print(index, last_gc_half)
        # 前shortLength个序列和后续每个序列尾部-->随机生成
        if index < short_length or index % short_length >= reuse_length:
            # 从第二组开始调控GC，last_gc_half >= 0时即非第一组。且二进制序列是每组的倒数第二位（因为一个碱基由两个二进制位确定，
            # 第2个二进制位随机即可。又因为index从0开始，所有最后一个应该是奇数，倒数第二位偶数）
            if last_gc_half >= 0 and index % 2 == 0:
                random_val = ((last_gc_half + 1) % 2) ^ int(origin_seq_list[index])
                # print(index, int(new_sequence[-1]), last_gc_half, random_val)
            else:
                random_val = random.randint(0, 1)
        else:
            random_val = reuse_base[index % short_length + margin_length] ^ int(origin_seq_list[index])

        random_sequence += str(random_val)
        new_val = int(origin_seq_list[index]) ^ random_val
        new_sequence += str(new_val)
        reuse_base[index % short_length] = new_val
    return random_sequence, new_sequence

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
    assert base_seq_length % 3 == 0
    return base_seq, base_compress


