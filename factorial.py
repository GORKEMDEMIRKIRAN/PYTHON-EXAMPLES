


# FAKTÖRİYEL BULMA PROGRAMI

factorial_number=int(input("Enter the number: "))
total=1
i=0
liste=[]
if (factorial_number=="1"):
    print("{} faktöriyeli {}".format(factorial_number,1))
else:
    while (i<factorial_number):
        i=i+1
        liste.append(i)
    for i in liste:
        total=total*i
    print("{} faktöriyeli {}".format(factorial_number,total))
    