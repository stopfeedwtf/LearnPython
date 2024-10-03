# Suite de fibonnaci (Done)
# def fibonnaci(n):
#     x,y=0,1
#     for i in range(n):
#         x,y=y,x+y
#     return x

# n=int(input("Entrez un nombre : "))
# print(fibonnaci(n), "est la", n, "ème valeur de la suite de Fibonacci.")

# Suite de Syracuse
# def syracuse(n,a):
#     for i in range(n):
#         if a%2 == 0:
#             a = a//2
#         else:
#             a = 3*a + 1
#         return a
# n=int(input("Entrez un nombre de recherche : "))
# a=int(input("Entrez la première valeur : "))
# print(syracuse(n,a), "est la", n, "ème valeur de la suite de Syracuse.")

# Nombres parfaits (Done)

# n=int(input("Entrez un nombre : "))
# def is_a_divisor(a,b):
#     if a%b == 0:
#         return True
#     else:
#         return False

# def sum_of_divisors(n):
#     sum = 0
#     for i in range (1, n):
#         if is_a_divisor(n, i):
#             sum = sum + i
#     return sum

# def is_perfect(n):
#     return sum_of_divisors(n) == n

# def display_perfect_numbers_until(n):
#     for i in range(1, n):
#         if is_perfect(i):
#             return i
    
# def add_superior_limit(n):
#     return display_perfect_numbers_until(n) + 1

# Jeu de nim













