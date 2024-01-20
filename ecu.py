lista = []

for x in range (2, 20):
    xl = round(x*0.1, 2)
    r = round(3*xl**2, 2)
    lista.append(r)

for t in lista:
    res = sum(lista)

res = res * 0.1
print (round(res, 4))

print(lista)
