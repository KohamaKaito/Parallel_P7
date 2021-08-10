'''
挿入ソートの、だいたいソートされていたら計算量が少ないという性質を利用
'''
import copy
import multiprocessing 

def merge(list):
    #２つのリストを一つにまとめる
    merged=[]
    zero_count=0
    one_count=0
    while len(list[0])>zero_count and len(list[1])>one_count:
        if(list[0][zero_count]<list[1][one_count]):
            merged.append(list[0][zero_count])
            zero_count+=1
        else:
            merged.append(list[1][one_count])
            one_count+=1
    if(len(list[0])>zero_count):
        merged.extend(list[0][zero_count:])
    else:
        merged.extend(list[1][one_count:])
    return merged

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

    space=thread
    two_dimensions_list=[]
    for start in range(space):
        modulus=0
        tmp_list=[]
        while (start+space*modulus)<length:#挿入ソートでソートする配列を作成
            tmp_list.append(sorted_List[start+space*modulus])
            modulus+=1
        two_dimensions_list.append(tmp_list)
    pool=multiprocessing.Pool(space)
    tmp_list=pool.map(shell_sort,two_dimensions_list)

    #並列シェルソートである程度並び替えたものをマージ
    while len(tmp_list)>1:
        surplus=[]
        if(len(tmp_list)%2==1):
            surplus=tmp_list.pop()
        merge_list=[]
        for count in range(0,len(tmp_list),2):
            merge_list.append([tmp_list[count],tmp_list[count+1]])
        
        tmp_list=pool.map(merge,merge_list)
        if(len(surplus)>0):
            tmp_list.append(surplus)
    return tmp_list[0]



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