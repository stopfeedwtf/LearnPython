# Occurences(Done)
# list = [1,2,3,8,52,2,2]

# def occurences(list,element):
#     count=0
#     for i in range(len(list)):
#         if list[i] == element:
#             count += 1
#     return count

# print(occurences(list, 2))

# Recherche (Done)
# list = [1,2,3,8,52,2,2]

# def search(list,element):
#     count=0
#     for i in range (len(list)):
#         if list[i] == element:
#             count += 1
#     return True if count > 0 else False

# print(search(list,2))

# Minimum (Done)
# list = [10,23,31,8,52,27,29]

# def minimum(list):
#     min_value = list[0]
#     for i in range(1, len(list)):
#         if list[i] < min_value:
#             min_value = list[i]
#     return min_value

# print(minimum(list))

# Minimum-index (Done)
# list = [10,23,31,8,52,27,29]

# def min_index(list):
#     min_value = list[0]
#     min_index = 0
#     for i in range(1, len(list)):
#         if list[i] < min_value:
#             min_value = list[i]
#             min_index = i
#     return min_index
    
# print(min_index(list))

# Inversion (Done)
# list = [1,2,3,4,5,6,7]

# def reverse(list):
#     start = 0
#     end = len(list) - 1
#     while start < end:
#         list[start], list[end] = list [end], list [start]
#         start += 1
#         end -= 1
#     return list

# print(reverse(list))

# Carré magiques

square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

# Ok
def sum_total(square,n):
    total = 0
    for i in range (n):
        for j in range(n):
            total += square[i][j]
    return total

def check_row(square,n,i,x):
    somme = 0
    for j in range (n):
        somme += square [i][j]
    return somme == x
    
def check_col(square,n,j,x):
    somme = 0
    for i in range (n):
        somme += square [i][j]
    return somme == x

def check_diag(square,n,d,x):
    if d == 1:
        s = 0
        for i in range(n):
            s+= square [i][i]
        return s == x
    elif d == 2:
        s = 0
        for i in range(n):
            s+= square [i][n-i-1]
        return s == x
    
def magic(square):
    n = len(square)
    square = n ** 2
    for i in range(1,square):
        if i not in square:
            return False
    return True

def magic_normal(square):
    n = len(square)
    total = sum_total(square,n)
    print(f'La somme total est de {total}')
    somme= total/n 
    print(f'La somme doit être de {somme}')
    for i in range(n):
        if not check_row(square, n, i, somme):
            return False
        if not check_col(square, n, i, somme):
            return False
    if not check_diag(square, n, 1, somme):
        return False
    if not check_diag(square, n, 2, somme):
        return False
    if not magic(square):
        return False
    return True
    
print(f'La réponse est {magic_normal(square)}')