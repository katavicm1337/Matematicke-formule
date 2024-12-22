# Nejednakost trokuta je svojstvo trokuta da mu je zbroj duljina
# dviju stranica veći od duljine treće stranice
# Formule: a+b>c, a+c>b, b+c>a

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Provjera nejednakosti s formulom
if(a+b>c and a+c>b and b+c>a):
    print("To JE trokut")
else:
    print("To NIJE trokut")
