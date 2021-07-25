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

| 関数名                |n=1000       |n=10000      |n=100000     |n=100000     |
| -------------------- | ----------- | ----------- | ----------- | ----------- |
|merge_sort()          |0.005 seconds|0.063 seconds|0.779 seconds|8.991 seconds|
|parallel_merge_sort() |0.036 seconds|0.062 seconds|0.617 seconds|5.629 seconds|
|bucket_sort()         |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|parallel_bucket_sort()|0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|bubble_sort()         |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|parallel_bubble_sort()|0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|quick_sort()          |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|parallel_quick_sort() |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|shell_sort()          |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|
|parallel_shell_sort() |0.000 seconds|0.000 seconds|0.000 seconds|0.000 seconds|


# 考察


・n=100000の時，マージソートの処理時間が9秒だったのに対し，並列マージソートは5.6秒でソートを完了させた．  
→ 並列化を行うと大量の数字のソートが早くなる！  
  
・ソートする配列の要素数が少ないときは並列化しない方が処理時間が短い．  
→ 並列処理を行うとオーバーヘッドやデータの受け渡しの時間が発生するから？  


# 役割分担

### モジュール

<img width="500" alt="スクリーンショット 2021-07-20 17 33 25" src="https://user-images.githubusercontent.com/57646279/126292017-cb257739-4bd9-4322-a3a9-7983f39034af.png">


### タスク

|  タスク                         | 担当者 |  状況  |
| ---- | ---- | ---- |
|create_list()の実装              |  小浜  | done  |
|merge_sort(list)の実装           |  小浜  | done  |
|parallel_merge_sort(list)の実装  |  小浜  | done  |
|bucket_sort(list)の実装          |  鳩間  | doing |
|parallel_bucket_sort(list)の実装 |  鳩間  |       |
|bubble_sort(list)の実装          |  宮城  | doing |
|parallel_bubble_sort(list)の実装 |  宮城  |       |
|quick_sort(list)の実装           |  佐藤  | doing |
|parallel_quick_sort(list)の実装  |  佐藤  |       |
|shell_sort(list)の実装           |  比嘉  | doing |
|parallel_shell_sort(list)の実装  |  比嘉  |       |
