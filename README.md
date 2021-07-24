# はじめに

このリポジトリは，並列処理によるソートプログラムの速度向上効果を実験するため，  
チームメンバー５人のソースコードの共有，バージョン管理を目的として作られました．


# 扱うアルゴリズム

・バケットソート  
・バブルソート  
・マージソート  
・クイックソート  
・シェルソート  


# モジュール

<img width="500" alt="スクリーンショット 2021-07-20 17 33 25" src="https://user-images.githubusercontent.com/57646279/126292017-cb257739-4bd9-4322-a3a9-7983f39034af.png">


# タスク

|  タスク                         | 担当者 |  状況  |
| ---- | ---- | ---- |
|create_list()の実装              |  小浜  | done  |
|merge_sort(list)の実装           |  小浜  | done  |
|parallel_merge_sort(list)の実装  |  小浜  | doing |
|bucket_sort(list)の実装          |  鳩間  | doing |
|parallel_bucket_sort(list)の実装 |  鳩間  |       |
|bubble_sort(list)の実装          |  宮城  | doing |
|parallel_bubble_sort(list)の実装 |  宮城  |       |
|quick_sort(list)の実装           |  佐藤  | doing |
|parallel_quick_sort(list)の実装  |  佐藤  |       |
|shell_sort(list)の実装           |  比嘉  | doing |
|parallel_shell_sort(list)の実装  |  比嘉  |       |


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

