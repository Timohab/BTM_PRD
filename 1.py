import csv,random

def quicksort(nums,fst,lst):
    '''Сортирует заданный массив

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


with open('scientist.txt',encoding='utf8') as file:
    a=file.readline()
    data=[x.split('#') for x in file.read().split('\n') if x!='']
    quicksort(data,0,len(data)-1)

origin=''
print('Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):\n')
for x in data:
    if x[1]=='Аллопуринол':
        print(f"{x[0]} - {x[2]}")
        if origin == '':
            origin=x[0]
print(f"Оригинальный рецепт принадлежит: {origin}")

with open('scientist_origin.txt','w',encoding='utf8') as file:
    file.write('ScientistName#preparation#date#components')
    for i in data:
        file.write('#'.join(i)+'\n')
