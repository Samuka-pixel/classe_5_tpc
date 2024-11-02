Eur = float(input("quanto é que ganhas por mês?: "))
Pres = float(input("quanto é o valor da prestação da sua casa?: "))
Pres_Eur = (Pres / Eur) * 100
if Pres_Eur <= 30:
    print("Podes conceder esta casa!!")
else:
    print("Infelizmente não ganhas o suficiente para esta casa :(")