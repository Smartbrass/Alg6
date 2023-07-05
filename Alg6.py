# Interpolation search

import random

n = 200
arr = []

for i in range(n):
    #num = random.randint(1, 100)
    num = i
    arr.append(num)

tos = random.randint(1, 100)
#ans = -1


##################################################################
#arr.sort()
#lef = 0
#rt = len(arr) - 1

#while (lef <= rt and 
#       tos >= arr[lef] and 
#       tos <= arr[rt]):

#    part_1 = (rt - lef) / (arr[rt] - arr[lef])
#    part_2 = tos - arr[lef]

## Поскольку инекс должен быть целым числом, преобразуем в инт

#    index = lef + int(part_1 * part_2)

#    if arr[index] == tos:
#        ans = index
#        break
#    if arr[index] < tos:
#        lef = index + 1
#    else:
#        rt = index - 1


#print(arr)
#print(tos)
#print('___')

#if ans != 1:
#    print(ans)
#else:
#    print(ans)





# Решето Эратосфена

#arr[1] = 0

#for i in range(n):
#    if arr[i] != 0:
#        j = i * 2
#        while j < n:
#            arr[j] = 0
#            j += i

#for i in arr:
#    if arr[i] != 0:
#        print(arr[i], end = " ")





# Решето Эратосфена попроще

#n = 1000
#sieve = set(range(2, n+1))

#while sieve:
#    prime = min(sieve)
#    print(prime, end = " ")
#    sieve -= set(range(prime, n+1, prime))




# Поиск подстроки в строке

str_where = "Hello World!"
str_find = "Wo"

index_w = 0
index_f = 0
len_w = len(str_where)
len_f = len(str_find)

while (index_w <= len_w - len_f and
    index_f < len_f):

    if str_where[index_w + index_f] == str_find[index_f]:
        index_f += 1

    else:
        index_w += 1
        index_f = 0

if index_f == len_f:
     print(f"Индекс начала искомой подстроки '{index_w}'")
else:
    print(f"No")
