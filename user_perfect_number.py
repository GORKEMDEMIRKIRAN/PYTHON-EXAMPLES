


# Mükemmel sayıyı bulma
# (1+2+3 = 6) bölenlerinin toplamı yine aynı sayıyı veriyorsa mükemmel sayı

number=int(input("Enter the number: "))

total=0
liste=[]
i=0
while (i<number):
    i=i+1
    if (number % i)==0:
        liste.append(i)
liste.pop()
for ls in liste:
    total=total+ls
if (total==number):
    print("{} mükemmel sayıdır.".format(number))
else:
    print("{} mükemmel sayı değildir.".format(number))