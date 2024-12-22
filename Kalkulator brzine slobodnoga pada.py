# U slobodnom padu tijelo se kreće samo pod utjecajem sile teže.
# Za izračun vremena slobodnog pada treba pomnožiti vrijeme pada
# s ubrzanjem sile teže.
# v = gt

t = float(input("Unesi trajanje slobodnog pada u sekundama: "))
g = 9.81 # Konstanta ubrzanja sile teže

brzina_metri = round(g*t, 1)
brzina_kilometri = round(g*t*3.6, 1)

print(f'Brzina postignuta je {brzina_metri}m/s ili {brzina_kilometri}km/h')
