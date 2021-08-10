import random
import time
import multiprocessing
import math
from typing import NewType


#バケットソート(並列化なし)
def bucket_sort(list):
    new_list = counting_sort(list,10)
    return new_list


#バケットソート(並列化あり)
def parallel_bucket_sort(list):
    #CPUの数だけプールを作成
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    # 均等にリストを配分
    size = int(math.ceil(float(len(list)) / processes))
    new_list = [list[i * size:(i + 1) * size] for i in range(processes)]
    # 並列処理（それぞれのプロセスでバケットソートを実行）
    new_list = pool.map(parallel_counting_sort,new_list)

    count_list = []

    for i in range(len(new_list[0])):
        count_list.append(new_list[0][i]+new_list[1][i]+new_list[2][i]+new_list[3][i])

    i = 0
    for num in range(len(count_list)):
        for c in range(count_list[num]):
            list[i] = num
            i += 1

    return list



#バケットソートによる並び替え
def counting_sort(list,max_num):
    count_list = [0]*(max_num+1)

    for i in list:
        count_list[i] += 1

    i = 0
    for num in range(len(count_list)):
        for c in range(count_list[num]):
            list[i] = num
            i += 1
    return list




# 各プロセスで実行する処理
def parallel_counting_sort(list):

    count_list = [0]*(10+1)

    for i in list:
        count_list[i] += 1
    
    return count_list





if __name__ == "__main__":
    array_bucket = [random.randint(1, 10) for _ in range(40000000)]

    print("元の配列")
    #print(array_bucket)

    print("バケットソート（並列化無し）後の配列↓")
    start = time.time()
    sorted = bucket_sort(array_bucket)
    stop = time.time()
    #print(sorted)
    print('⏰%.3f seconds'% (stop - start))

    print("並列バケットソート後")
    start = time.time()
    soted_parallel = parallel_bucket_sort(array_bucket)
    stop = time.time()
    #print(soted_parallel)
    print('⏰%.3f seconds'% (stop - start))
