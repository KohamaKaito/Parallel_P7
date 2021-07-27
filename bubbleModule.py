import math
import multiprocessing

# バブルソート（並列化無）
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    return list

# バブルソート（並列化有り）
def swap(list):
    if len(list) == 1:
        new_list.append(list[0])
    elif list[0] > list[1]:
        list[0], list[1] = list[1], list[0]
        new_list.append(list[0])
        new_list.append(list[1])
        swap_number += 1
    elif list[0] < list[1]:
        new_list.append(list[0])
        new_list.append(list[1])
    
    return new_list

def odd_devide_data(list):
    all_devide_list = []

    for i in range(0, len(list), 2):
        devide_list = []
        devide_list.append(list[i])
        devide_list.append(list[i+1])
        all_devide_list.append(devide_list)
    
    return all_devide_list

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

#def mix_data():



def parallel_bubble_sort(list):
    new_list = []
    swap_number = 0

    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    devide_list = odd_devide_data(list)
    size = int(math.ceil(float(len(devide_list)) / processes))
    devide_list = [devide_list[i * size:(i + 1) * size] for i in range(processes)]

    new_list = pool.map(swap, devide_list)

    return new_list

list1=[8, 4, 3, 7, 6, 5, 2, 1]
test = parallel_bubble_sort(list1)
print(test)