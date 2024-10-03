# TP1
# Exercice 1 (Done)
# a = eval(input("Saisissez votre premier nombre"))
# b = eval(input("Saisissez votre second nombre"))

# if a > b:
#     print(a, "est plus grand que", b)
# else:
#     print(b, "est plus grand que", a)


# Exercice 2 (Done)
# a = eval(input("Saisissez votre montant"))

# if a > 500:
#     b = a * 0.08
#     print("Le montant de la remise pour un bien supérieur à 500 $ est de", b)
# elif a > 100:
#     c = a * 0.05
#     print("Le montant de la remise pour un bien entre 100 et 500 $ est de", c)
# else:
#     print("Votre montant n'est pas éligible à une remise")


# Exercice 3 (Done)
# a = eval(input("Saisissez votre premier nombre"))
# b = eval(input("Saisissez votre second nombre"))
# c = eval(input("Saisissez votre troisième nombre"))

# if a > b and b > c:
#     print(a, b, "et", c, "sont classés dans l'ordre croissant")
# else:
#     print(a, b, "et", c, " ne sont pas classés dans l'ordre croissant")

# Exercice 4 (Done)
# a = eval(input("Saisissez votre premier nombre"))
# b = eval(input("Saisissez votre second nombre"))
# c = eval(input("Saisissez votre troisième nombre"))

# d = a, b, c
# e= sorted(d)
# print(e)

# Exercice 5 (Done)
# a = eval(input("Saisissez votre premier nombre"))
# b = eval(input("Saisissez votre second nombre"))

# if a*b > 0:
#     print("Le produit des deux nombres est positif ou nul")
# else:
#     print("Le produit des deux nombres est négatif")


# Exercice 6 (Done)
# a = eval(input("Saisissez votre premier nombre"))

# for i in range(a+1):
#     print(i)

# Exercice 7 (Done)
# a = int(input("Saisissez un réel"))
# somme = 0

# while a!= 0:
#     somme = somme + a
#     a = int(input("Saisissez un réel (0 pour terminer)"))
# print (somme)

# Exercice 8 (Done)
# a = eval(input("Saisissez votre premier nombre"))
# b = eval(input("Saisissez votre second nombre"))
# somme = 0

# for i in range(a+2, b, 2):
#     somme = somme + i
# print(somme)

# TP2
# Exercice 1 (Done)
# a = int(input("Saisissez un entier"))
# b = int(input("Saisissez un autre entier"))
# somme = 0

# for i in range(b):
#     somme = somme + a
# print(somme)

# Old Ex1
# for i in range(a, b+1, 1):
#     somme = (a+i+b)-a
# print(somme)

# Exercice 2 (Done)
# a = int(input("Saisissez un entier"))

# for i in range(a):
#     print("*" * (a-i))

# Exercice 3 (Done)
# a = int(input("Saisissez un entier \n"))

# for i in range(0,a):
#     print(" " * (a-i-1), "*" * (2*i+1))
# Exercice 4 (Done)
# a = int(input("Saisissez un entier \n"))
# x = 1
# for i in range(0,a):
#     print(x, "*", x, "=", x*x)
#     x = 10*x + 1

# Exercice 5 (Done)
# a = int(input("Saisissez un entier \n"))
# x = 1
# y = x+1
# z = 1
# for i in range(0,a):
#     print(a, "*", x, "+", y, "=", z)
#     x = 10*x + y
#     y = y + 1
#     z = 10*z + 1

# Exercice 6 (Done)
# a = int(input("Saisissez un entier \n"))
# x = 1
# for i in range(2,a+2):
#     print(8, "*", x, "+", i-1, "=", 8*x+i-1)
#     x = 10*x + i

# Exercice 7 

