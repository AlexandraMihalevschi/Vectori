x = input('Dati un vector separat prin virgule: ')
x = x.split(',')
x = list(map(int, x))

print("Media temperaturii:", sum(x)/len(x))
mx = max(x)
mn = min(x)
print("Maximul:", mx, "grade la ora", x.index(mx)+1)
print("Minimul:", mn, "grade la ora", x.index(mn)+1)