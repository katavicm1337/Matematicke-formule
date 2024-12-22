fahrenheit = float(input("Unesi temperaturu u fahrenheitu: "))

celzij = (fahrenheit - 32) * 5/9
celzij = round(celzij, 1)

print(f'{celzij}C')
