names = ("Aman","Jain")
comps = ("Dell", "HP")

zipped = list(zip(names, comps))
zipped1 = set(zip(names, comps))
print(zipped1)

for (a,b) in zipped:
    print(a,b)