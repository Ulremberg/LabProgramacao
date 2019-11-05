from itertools import zip_longest
entrada = int(input())
arr = []

for i in range(entrada):
                arr.append([int(i) for i in input().split()])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] <= 0:
            arr[i][j] = arr[i][j] * 2


#list(zip_longest(*arr))
#print([*zip(*arr)])
#[*zip(*theArray)]
#print(map(list,zip(*arr)))

arr1 = list(zip(*arr)) #faz a transposta da matriz. Linha passa a ser coluna e vice versa

for i in range(len(arr)):
    print(*arr1[i])