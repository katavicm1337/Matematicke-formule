# Pitagorina trojka je naziv za uređenu trojku prirodnih brojeva gdje su
# duljine a i b katete, a c hipotenuza pravokutnog trokuta.
# a^2+b^2=c^2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Provjera je li tvrdnja(pitagorina trojka) istinita
if (a**2+b**2==c**2):
    print(f'{a,b,c} JE pitagorina trojka')
else:
    print(f'{a,b,c} NIJE pitagorina trojka')
