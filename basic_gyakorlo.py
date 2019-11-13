print("Hello Python")

#String muveletek
print('Ábrahámhegy'[3])
print('Ábrahámhegy'[3::2])
print('Ábrahámhegy'[::-1])

print("Agyagosszergény".replace("A","E"))
print("Agyagosszergény".upper())
print("agy" in "Agyagosszergény".lower())
name = "Komlódtótfalu"
print(name.lower())
print(name)
line = "Windows 2000;Windows Server 2000;Harmadik érték"
parts = line.split(";")
print(parts[0])
print(parts[1])
print(parts[2])