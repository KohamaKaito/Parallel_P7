import time
from concurrent.futures import ProcessPoolExecutor

#自作モジュール
import myModule
import mergeModule
import bubbleModule
import shellModule
import quicksort
import bucket_sort

if __name__ == "__main__":

    # ソート対象の配列を準備する
    target_list = myModule.create_list(10)

    # ソート対象の配列を出力
    print("ソート前の配列↓")
    print(target_list)



    # マージソート（並列化無し）
    print("マージソート（並列化無し）後の配列↓")
    start = time.time()
    sorted_list01 = mergeModule.merge_sort(target_list)
    stop = time.time()
    print(sorted_list01)
    print('⏱%.3f seconds' % (stop - start))

    # マージソート（並列化有り）
    print("マージソート（並列化有り）後の配列↓")
    start = time.time()
    sorted_list02 = mergeModule.parallel_merge_sort(target_list)
    stop = time.time()
    print(sorted_list02)
    print('⏱%.3f seconds' % (stop - start))



    # バブルソート（並列化無し）
    print("バブルソート（並列化無し）後の配列↓")
    start = time.time()
    sorted_list03 = bubbleModule.bubble_sort(target_list)
    stop = time.time()
    print(sorted_list03)
    print('⏱%.3f seconds' % (stop - start))

    # バブルソート（並列化有り）
    print("バブルソート（並列化有り）後の配列↓")
    start = time.time()
    sorted_list04 = bubbleModule.parallel_bubble_sort(target_list)
    stop = time.time()
    print(sorted_list04)
    print('⏱%.3f seconds' % (stop - start))



    # シェルソート（並列化無し）
    print("シェルソート（並列化無し）後の配列↓")
    start = time.time()
    sorted_list05 = shellModule.shell_sort(target_list)
    stop = time.time()
    print(sorted_list05)
    print('⏱%.3f seconds' % (stop - start))

    # シェルソート（並列化有り）
    print("シェルソート（並列化有り）後の配列↓")
    start = time.time()
    sorted_list06 = shellModule.parallel_shell_sort(target_list)
    stop = time.time()
    print(sorted_list06)
    print('⏱%.3f seconds' % (stop - start))

    

    # クイックソート（並列化無し）
    # クイックソートソート（並列化有り）
    quicksort.main()

    

    # バケットソート（並列化無し）
    print("バケットソートソート（並列化無し）後の配列↓")
    start = time.time()
    sorted_list07 = bucket_sort.bucket_sort(target_list)
    stop = time.time()
    print(sorted_list07)
    print('⏱%.3f seconds' % (stop - start))

    # バケットソートソートソート（並列化有り）
    print("バケットソートソート（並列化有り）後の配列↓")
    start = time.time()
    sorted_list08 = bucket_sort.parallel_bucket_sort(target_list)
    stop = time.time()
    print(sorted_list08)
    print('⏱%.3f seconds' % (stop - start))
    