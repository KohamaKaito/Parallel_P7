# バブルソート（並列化無し）
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]

# バブルソート（並列化有り）
def parallel_bubble_sort(list):
    new_list = list
    return new_list