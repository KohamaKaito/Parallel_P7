import math
import multiprocessing


# マージソート（並列化無し）
def merge_sort(list):
    length = len(list)
    if length <= 1:
        return list
    middle = length // 2
    # 再起的に分割を行う
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    # 結合を行う
    new_list = merge(left, right)
    return new_list


# マージソート（並列化有り）
def parallel_merge_sort(list):
    # CPUの数だけプールを作成
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    # 均等にリストを配分
    size = int(math.ceil(float(len(list)) / processes))
    list = [list[i * size:(i + 1) * size] for i in range(processes)]
    # 並列処理（それぞれのプロセスでマージソートを実行）
    list = pool.map(merge_sort, list)
    # それぞれのプロセスでソートした配列を結合する
    while len(list) > 1:
        extra = list.pop() if len(list) % 2 == 1 else None
        list = [(list[i], list[i + 1]) for i in range(0, len(list), 2)]
        list = pool.map(merge, list) + ([extra] if extra else [])
    return list[0]


# 配列同士を結合する関数
def merge(*args):
    if len(args) == 1:
        left,right = args[0]
    else:
        left,right = args
    merged = []
    l_i, r_i = 0, 0
    # 左の数字を比較→小さい方をappend
    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1
    # あまりをextend        
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged