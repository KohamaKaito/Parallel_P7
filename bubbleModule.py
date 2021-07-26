# バブルソート（並列化無し）
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    return list

# バブルソート（並列化有り）
from concurrent.futures import ProcessPoolExecutor

def parallel_bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    
    with ProcessPoolExecutor(2) as e:
        ret = e.map(bubble_sort, list)
        multi = [r for r in ret]
