x = input('Dati un vector separat prin virgule: ')
x = x.split(',')
x = list(map(int, x))
y = x

print("Suma primelor trei componente: ", x[0]+x[1]+x[2])
print('Suma tuturor componentelor: ', sum(y))

p = 1
for i in range(len(x)):
	p = p * x[i]
 
print('Produsul: ', p)
print('Valoarea absoluta: ', abs(y[2]))
print('Suma primelor componente: ', x[0]+y[0])