import random


# ソート対象の配列を準備する関数
def create_list(value):
    num_list = []
    for i in range(value):
        num_list.append(random.randint(1,1000))
    return num_list