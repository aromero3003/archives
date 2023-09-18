D = float(input("Diámetro: "))
dD = float(input("Incerteza diámetro: "))
H = float(input("\nAltura: "))
dH = float(input("Incerteza altura: "))

# Calculo el máximo error relativo de pi
max_er_pi = 0.2 * dD / D + 0.1 * dH / H
print("El máximo error de pi es", max_er_pi)
tabla_pi = {
        0.1 : 3.1,
        0.01:3.14,
        0.001:3.141,
        0.0001:3.1415,
        0.00001:3.14159
}
"""
print("Tabla de i Er de pi")
print(f"{0.1/3.1:06f} = 0.1 / 3.1")
print(f"{0.01/3.14:06f} = 0.01 / 3.14")
print(f"{0.001/3.141:06f} = 0.001 / 3.141")
print(f"{0.0001/3.1415:08f} = 0.0001 / 3.1415")
print(f"{0.00001/3.14159:08f} = 0.00001 / 3.14159")
"""
dpi = 0
pi = 0
for d in tabla_pi:
    if d/tabla_pi[d] <= max_er_pi and d > dpi:
        dpi = d
        pi = tabla_pi[d]
    print(f"{d / tabla_pi[d]:06f} = {d} / {tabla_pi[d]}")

print(f"\nPI vale {pi} y su incerteza apropiada es {dpi}")
dV = D*D*H/4 * dpi + pi*D*H/2 * dD + pi*D*D/4 * dH
print(f"Volumen: {pi*D*D*H/4:07f}(cm3)")
print(f"La incerteza de volumen es: {dV:07f}")

