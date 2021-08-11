# 目的

これまで講義では、並列分散処理の基本的な概念や実装の手法について学んできた。本演習では、並列プログラミングの理解を深めるため、実際にpythonのライブラリを活用しながらコーディングを行い、逐次処理と並列処理の比較を通して並列プログラムの効果を検証することを目的とする。



# 方法

上記の目的を達成するため、様々なソーティングアルゴリズムを並列化無しの場合と並列化有りの場合で実装し、両方の実行時間を比べることで、並列処理によってどれぐらいの処理速度の向上効果があったのか検証を行う．  
 

#### 扱うアルゴリズム

・バケットソート  
・バブルソート  
・マージソート  
・クイックソート  
・シェルソート  


# 結果

Intel Core i7-8700 スレッド数12

n = ソートを行う数字の数

| Merge Sort           |n=1000       |n=10000      |n=100000     |n=1000000    |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|逐次                   |0.002 seconds|0.039 seconds|0.304 seconds|4.310 seconds|
|並列                   |0.161 seconds|0.184 seconds|0.315 seconds|1.478 seconds|

| Bubble Sort　　         |n=100        |n=1000       |n=2000       |n=3000       |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|逐次                   |0.002 seconds|0.840 seconds|4.352 seconds|15.52 seconds|
|並列                   |0.271 seconds|2.368 seconds|5.249 seconds|8.603 seconds|

| Quick Sort　　          |n=10000      |n=100000     |n=1000000    |n=10000000   |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|逐次                   |0.018 seconds|0.205 seconds|3.118 seconds|47.21 seconds|
|並列                   |0.649 seconds|0.728 seconds|2.433 seconds|20.79 seconds|

| Shell Sort　　          |n=1000       |n=10000      |n=100000     |n=1000000    |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|逐次                   |0.003 seconds|0.054 seconds|0.652 seconds|9.737 seconds|
|並列                   |0.209 seconds|0.260 seconds|0.451 seconds|2.600 seconds|

| Bucket Sort　　         |n=100000     |n=1000000    |n=10000000   |n=100000000  |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|逐次                   |0.008 seconds|0.093 seconds|0.918 seconds|9.339 seconds|
|並列                   |0.164 seconds|0.216 seconds|0.661 seconds|6.110 seconds|




# 考察

n=1000000の時，マージソートの逐次処理の時間が 4.3秒だったのに対して，並列処理は5.6秒でソートを完了させた．同様にクイックソートの時は，逐次処理が 5.5秒だったのに対して並列処理は 1.5秒でソートを完了させた．これらのことから，並列化を行うと大量の数字をソートする際の処理時間が短縮されることが考えられる．

　n=100の時，バブルソートの逐次処理の時間が 0.002秒だったのに対して，並列処理の場合は，0.271秒もソートに時間がかかった．他のアルゴリズムでも同様に nの値が小さい時は，並列処理の方が逐次処理よりもソートに時間がかかるという結果が得られた．これらのことから，ソートを行う数字の数が少ない時に並列化を行うと，オーバーヘッドやデータの受け渡しの時間が発生し，逐次処理よりも処理に時間がかかってしまうと考えられる．

バケットソートは他のソートと比べて処理速度が速くなり、特にn=100万の時は他のソートと比べてかなり速くなった。これは、バケットソートが比較をせずソートを行えるという利点によるものである。その一方で、整数の取りうる範囲が狭い場合に効果を発揮するといった制限があるため用途に合わせて使う必要がある。


# 役割分担

### モジュール

<img width="500" alt="スクリーンショット 2021-07-20 17 33 25" src="https://user-images.githubusercontent.com/57646279/126292017-cb257739-4bd9-4322-a3a9-7983f39034af.png">


### タスク

|  タスク                         | 担当者 |  状況  |
| ---- | ---- | ---- |
|create_list()の実装              |  小浜  | done  |
|merge_sort(list)の実装           |  小浜  | done  |
|parallel_merge_sort(list)の実装  |  小浜  | done  |
|bucket_sort(list)の実装          |  鳩間  | done  |
|parallel_bucket_sort(list)の実装 |  鳩間  | done  |
|bubble_sort(list)の実装          |  宮城  | done  |
|parallel_bubble_sort(list)の実装 |  宮城  | done  |
|quick_sort(list)の実装           |  佐藤  | done  |
|parallel_quick_sort(list)の実装  |  佐藤  | done  |
|shell_sort(list)の実装           |  比嘉  | done  |
|parallel_shell_sort(list)の実装  |  比嘉  | done  |
