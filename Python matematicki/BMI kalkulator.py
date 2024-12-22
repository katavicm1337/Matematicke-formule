# Indeks tjelesne mase(BMI) je okvirni pokazatelj debljine i pretilosti.
# Računa se tako da se tjelesna masa osobe u kilogramima podijeli s
# kvadratom visine u metrima.
# BMI = m/h^2

visina = float(input("Unesi visinu u metrima: "))
masa = float(input("Unesi tezinu  u kilogramima: "))

bmi = masa / visina**2
zaokruzenibmi = round(bmi, 1)

if bmi < 18.5:
    print(f'Mrsav: {zaokruzenibmi}')
elif 18.5<=bmi<25.0:
    print(f'Normalno: {zaokruzenibmi}')
elif 25.0<=bmi<30.0:
    print(f'Debel: {zaokruzenibmi}')
elif 30.0<=bmi:
    print(f'Pretilost: {zaokruzenibmi}')
