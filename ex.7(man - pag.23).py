x = input('Dati un vector separat prin virgule: ')
x = x.split(',')
x = list(map(int, x))

print(x)
print("Venit saptamanal:", sum(x))
print("Media venitului:", sum(x)/len(x))
print("Maximul:", max(x))
print("Minimul:", min(x))