import random

def quicksort(nums,fst,lst):
    '''Сортирует заданный массив по второму элементу подмассива

    nums - массив для сортировки
    fst - начальный индекс массива
    lst - конечный индекс массива:
    '''
    if fst>=lst: return
    el_op=nums[random.randint(fst,lst)][2]
    i,j=fst,lst
    while nums[i][2] < el_op: i += 1
    while nums[j][2] > el_op: j -= 1
    if i<j:
        nums[i],nums[j]=nums[j],nums[i]
    i+=1
    j-=1

    quicksort(nums,fst,j)
    quicksort(nums,i,lst)

def binary_search(nums,fst,lst,n):
    '''Осуществляет бинайрный поиск

    nums - сортированный массив, в котором осуществляется поиск
    fst - начальный эллемент массива для поиска
    lst - конечный элемент массива для поиска
    n - искомый элемент
    '''
    mid=(fst+lst)//2
    if lst-fst<=0: return -1
    if nums[mid][2]<n: return binary_search(nums,mid+1,lst,n)
    if nums[mid][2]>n: return binary_search(nums,fst,mid-1,n)
    if nums[mid][2]==n:return mid
    return -1

with open('scientist.txt',encoding='utf8') as file:
    a=file.readline()
    data=[x.split('#') for x in file.read().split('\n') if x!='']
    quicksort(data,0,len(data)-1)

s_inp=input()
while s_inp != 'эксперимент':
    need_data=f"{s_inp[6:10]}-{s_inp[3:5]}-{s_inp[0:2]}"
    f_index=binary_search(data,0,len(data)-1,need_data)
    if f_index==(-1):
        print('В этот день ученые отдыхали')
        s_inp = input()
        continue
    res = [f"Ученый {data[f_index][0]} создал препарат: {data[f_index][1]} - {data[f_index][2]}"]
    i=f_index-1
    while i>=0:
        if data[i][2]==need_data:
            res.append(f"Ученый {data[i][0]} создал препарат: {data[i][1]} - {data[i][2]}")
        else:
            break
        i-=1
    i = f_index +1
    while i<len(data):
        if data[i][2]==need_data:
            res.append(f"Ученый {data[i][0]} создал препарат: {data[i][1]} - {data[i][2]}")
        else:
            break
        i+=1
    for z in res:
        print(z)
    s_inp=input()
