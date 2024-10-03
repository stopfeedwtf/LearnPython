# Exercice 1 (Done)
# a = eval(input("Saisissez votre prix unitaire HT"))
# b = eval(input("Saisissez votre taux de TVA"))
# c = eval(input("Saisissez le nombre d'articles"))

# prix_total_ht = a * c
# taux_tva = b / 100
# total=prix_total_ht + (prix_total_ht * taux_tva)
# print("Prix total TTC :", total, "$")

# Exercice 2-1 (Done)
# a = input("Saisissez la valeur que doit prendre la première variable")
# b = input("Saisissez la valeur que doit prendre la seconde variable")
# a, b = b, a
# print("A=", a, "B=", b)

# Exercice 2-2 (Done)
# a = input("Saisissez la valeur que doit prendre la première variable")
# b = input("Saisissez la valeur que doit prendre la seconde variable")
# c = a
# a = b
# b = c
# print("A=", a, "B=", b)

# Exercice 2-3 (Done)
# a = eval(input("Saisissez la valeur numéraire que doit prendre la première variable"))
# b = eval(input("Saisissez la valeur numéraire que doit prendre la seconde variable"))
# c = (a + b)-a
# d = (a + b)-b
# a = c
# b = d
# print("A=", a, "B=", b)

# Exercice 3 (Done)
# a = input("Saisissez la valeur que doit prendre la première variable")
# b = input("Saisissez la valeur que doit prendre la seconde variable")
# c = input("Saisissez la valeur que doit prendre la troisième variable")

# a, b, c = b, c, a
# print("A=", a, "B=", b, "C=", c)

# Date de pâques (Done)
# m = eval(input("Choisissez l'année dont vous souhaitez connaître la dâte de Pâques"))
# n = m - 1900
# a = n%19
# b = (7*a+1)//19
# c = (11*a-b+4)%29
# d = n//4
# e = (n-c+d+31)%7
# print("Date de Pâques :", "31 Mars", "+", (25-c-e), "jours")