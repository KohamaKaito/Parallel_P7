# マージソート（並列化無し）
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    # ここで分割を行う
    left = list[:mid]
    right = list[mid:]
    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)
    # 結合を行う
    new_list = merge(left, right)
    return new_list


# マージソート（並列化有り）
def parallel_merge_sort(list):
    new_list = list
    return new_list


# 配列同士を結合する関数
def merge(left, right):
    merged = []
    l_i, r_i = 0, 0
    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1
    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged