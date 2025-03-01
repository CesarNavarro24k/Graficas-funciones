import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña = int(input("Introduce la longitud de la contraseña:"))

contraseña_c = " "

for i in range(contraseña):
    contraseña_c += random.choice(caracteres)
print(contraseña_c)
