'''
挿入ソートの、だいたいソートされていたら計算量が少ないという性質を利用
'''
import copy
import multiprocessing 
import concurrent.futures
# シェルソート（並列化無し）
def shell_sort(list):
    sorted_List=copy.copy(list)
    space=1
    length=len(sorted_List)
    while True:
        next_space=3*space+1
        if(next_space<length):
            space=next_space
        else:
            break
    while space>0:
        for start in range(space):
            modulus=0
            tmp_list=[]
            while (start+space*modulus)<length:#挿入ソートでソートする配列を作成
                tmp_list.append(sorted_List[start+space*modulus])
                modulus+=1
            tmp_list=insertion_sort(tmp_list)#挿入ソート
            modulus=0
            while (start+space*modulus)<length:#ソートした配列を元の位置に戻す
                sorted_List[start+space*modulus]=tmp_list[modulus]
                modulus+=1
        space=int((space-1)/3)#数列を逆算
    return sorted_List


# シェルソート（並列化有り）
def parallel_shell_sort(list): 
    sorted_List=copy.copy(list)
    thread=multiprocessing.cpu_count()#コア数ではなくスレッド数
    pool = multiprocessing.Pool(processes=thread)
    length=len(sorted_List)

    #配列をthread間隔で分割する
    #スレッドの数の範囲内で間隔を決める。
    space=thread
    #割り振る配列を作成
    while space>0:
        two_dimensions_list=[]
        for start in range(space):
            modulus=0
            tmp_list=[]
            while (start+space*modulus)<length:#挿入ソートでソートする配列を作成
                tmp_list.append(sorted_List[start+space*modulus])
                #[[0, 4, 8, 12, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
                modulus+=1
            two_dimensions_list.append(tmp_list)
        #それぞれにshell_sortを実行させる
        p=multiprocessing.Pool(space)
        tmp_list=p.map(shell_sort,two_dimensions_list)

        for count in range(len(tmp_list)):
            #print(tmp_list[count])
            for data in range(len(tmp_list[count])):
                sorted_List[count+space*data]=tmp_list[count][data]

        space=int(space/2)

    '''
    #space=1
    #スレッドの数の範囲内で間隔を決める。
    space=thread
    if(space>length/2):
        space=int(length/2)
    #各スレッド用の配列を作る
    while space>0:
        two_dimensions_list=[]
        for start in range(space):
            modulus=0
            tmp_list=[]
            while (start+space*modulus)<length:#挿入ソートでソートする配列を作成
                tmp_list.append(sorted_List[start+space*modulus])
                modulus+=1
            two_dimensions_list.append(tmp_list)
        p=multiprocessing.Pool(space)
        tmp_list=p.map(insertion_sort,two_dimensions_list)


        for count in range(len(tmp_list)):
            #print(tmp_list[count])
            for data in range(len(tmp_list[count])):
                sorted_List[count+space*data]=tmp_list[count][data]
    '''

    return sorted_List



def insertion_sort(list):#挿入ソート
    sorted_List=copy.copy(list)
    for i in range(1,len(sorted_List)):#sortedListの二番目から最後までループ
        tmp=sorted_List[i]
        if(tmp<sorted_List[i-1]):#降順ではなかったら
            j=i
            while True:
                sorted_List[j]=sorted_List[j-1]
                j-=1
                if j==0 or tmp>=sorted_List[j-1]:
                    break
            sorted_List[j]=tmp
    return sorted_List


'''
参考
https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/shell_sort


一定間隔おきにグループ化する。
4 3 5 7 1 8 6 2 で4置きにグループ化するなら
グループ1:4 1
グループ2:3 8
グループ3:5 6
グループ4:7 2
グループごとに並び替えを行う（並列）
小さい順に並び替えるとグループ4だけで並び替えが発生し、
1 3 5 2 4 8 6 7 (2と7が逆転)
間隔を縮めて再度グループ化 間隔2
グループ1:1 5 4 6
グループ2:3 2 8 7
再度グループ内で並び変え
1 2 4 3 5 7 6 8
間隔1になったら残りの要素で並び変えする。


'''