"""
Conversor de temperatura. convertir de grados centigrado a farenheit y vicesersa
"""
temp_c = float(input("Ingresa la temp en grados °C:"))
temp_f = float(input("Ingresa la temp en grados F:"))

action = input("Quieres pasar de grados °C a F?")
if action == "si":
    c_to_f = (temp_c * 9 / 5) + 32
    print(f"{temp_c} °C son {c_to_f} F")
else:
    f_to_c = (temp_f - 32 ) * 5/9
    print(f"{temp_f} F son {f_to_c} °C")