import time

#自作モジュール
import mergeModule
import bucketModule
import bubbleModule
import myModule

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


    # バケットソート（並列化無し）
    print("バケットソート（並列化無し）後の配列↓")
    start = time.time()
    sorted_list03 = bucketModule.bucket_sort(target_list)
    stop = time.time()
    print(sorted_list03)
    print('⏱%.3f seconds' % (stop - start))


    # バケットソート（並列化有り）
    print("バケットソート（並列化有り）後の配列↓")
    start = time.time()
    sorted_list04 = bucketModule.parallel_bucket_sort(target_list)
    stop = time.time()
    print(sorted_list04)
    print('⏱%.3f seconds' % (stop - start))