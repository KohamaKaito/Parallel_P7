import math
import multiprocessing


# バブルソート（並列化無）
def bubble_sort(list):
    new_list = list

    # 入れ替えが起こらなくなるまで繰り返す
    while True:
        # 初期状態を記憶
        old_list = new_list

        # [6,5,4,3,2,1] → [[6,5],[4,3],[2,1]]
        new_list = odd_devide_data(new_list)
        # [[6,5],[4,3],[2,1]] → [5,6,3,4,1,2]
        new_list = all_swap(new_list)

        # [5,6,3,4,1,2] → [[5],[6,3],[4,1],[2]]
        new_list = even_devide_data(new_list)
        # [[5],[6,3],[4,1],[2]] → [5,3,6,1,4,2]
        new_list = all_swap(new_list)

        # 入れ替えが発生しなかったら終了
        if(old_list == new_list):
            break

    return(new_list)


# バブルソート（並列化有）
def parallel_bubble_sort(list):   

    # CPUの数だけプールを作成
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes) 

    new_list = list

    # 入れ替えが起こらなくなるまで繰り返す
    while True:
        # 初期状態を記憶
        old_list = new_list

        # [7,6,5,4,3,2,1,0] → [[7,6],[5,4],[3,2],[1,0]]
        new_list = odd_devide_data(new_list)
        # 均等にリストを配分
        # [[7,6],[5,4],[3,2],[1,0]] → [ p1[[7,6],[5,4]] , p2[[3,2],[1,0]] ]
        size = int(math.ceil(float(len(new_list)) / processes))
        new_list = [new_list[i * size:(i + 1) * size] for i in range(processes)]
        # 並列(それぞれのプロセッサでall_swapを実行)
        # p1[[7,6],[5,4]] → p1[6,7,4,5]
        # p2[[3,2],[1,0]] → p2[2,3,0,1]
        new_list = pool.map(all_swap, new_list)
        # 一度１次元配列に戻す
        # [[6,7,4,5],[2,3,0,1]] → [6,7,4,5,2,3,0,1]
        new_list = sum(new_list, [])

        # [6,7,4,5,2,3,0,1] → [[6],[7,4],[5,2],[3,0],[1]]
        new_list = even_devide_data(new_list)
        # 均等にリストを配分
        # [[6],[7,4],[5,2],[3,0],[1]] → [ p1[[6],[7,4]] , p2[[5,2],[3,0],[1]] ]
        size = int(math.ceil(float(len(new_list)) / processes))
        new_list = [new_list[i * size:(i + 1) * size] for i in range(processes)]
        # 並列(それぞれのプロセッサでall_swapを実行)
        # p1[[6],[7,4]] → p1[6,4,7]
        # p2[[5,2],[3,0],[1]] → [2,5,0,3,1]
        new_list = pool.map(all_swap, new_list)
        # 一度１次元配列に戻す
        # [[6,4,7],[2,5,0,3,1]] → [6,4,7,2,5,0,3,1]
        new_list = sum(new_list, [])

        # 入れ替えが発生しなかったら終了
        if(old_list == new_list):
            break

    return new_list


# [1,2,3,4,5,6] → [[1,2],[3,4],[5,6]]
def odd_devide_data(list):
    all_devide_list = []
    for i in range(0, len(list), 2):
        devide_list = []
        devide_list.append(list[i])
        devide_list.append(list[i+1])
        all_devide_list.append(devide_list)
    return all_devide_list


# [1,2,3,4,5,6] → [[1],[2,3],[4,5],[6]]
def even_devide_data(list):
    all_devide_list = []
    for i in range(0, len(list), 2):
        devide_list = []
        if i == 0:
            devide_list.append(list[i])
        else:
            devide_list.append(list[i-1])
            devide_list.append(list[i])
        all_devide_list.append(devide_list)
    if len(list) % 2 == 0:
        devide_list = []
        devide_list.append(list[-1])
        all_devide_list.append(devide_list)
    return all_devide_list


# [2,1] → [1,2]
def swap(list):
    if len(list) == 1:
      return list  
    if list[0] < list[1]:
        return [list[0],list[1]]
    else:
        return [list[1],list[0]]


# [[2,1],[4,3],[6,5]] → [1,2,3,4,5,6]
def all_swap(list):
    new_list = []
    for num in list:
        new_list.append(swap(num))
    # 一次元配列にする
    futures = sum(new_list, [])
    return(futures)


if __name__ == "__main__":
    num_list = [6,4,5,1,3,4,8,0,1,2,5,2,1,4,8,2]

    print("元の配列↓")
    print(num_list)

    print("並列バブル後↓")
    print(parallel_bubble_sort(num_list))