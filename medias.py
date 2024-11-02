print("tiveste 3 minitestes 20% cada, 1 apresentação 10% e 1 exame final 30%")
notMinTest1 = int(input("mini-teste 1: "))
notMinTest2= int(input("mini-teste 2: "))
notMinTest3= int(input("mini-teste 3: "))
notApres = int(input("Apresentação: "))
notEx = int(input("Exame final: "))
#notMax = int(input("qual é o seu sistema de nota?: "))

x = notMinTest1 * 0.2 + notMinTest2 * 0.2+ notMinTest3 * 0.2
y = notApres * 0.1
z = notEx * 0.3
a = x + y + z
print(a)
if a >= 70:
    print("Parabens tiveste muito bem")
elif a >= 50:
    print("tiveste positiva")
else:
    print("conseguiras melhor da proxima vez")