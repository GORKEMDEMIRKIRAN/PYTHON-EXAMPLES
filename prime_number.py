
# ASAL SAYI BULMA

# 1 ve kendisinden başka sayıyı bölünemiyen sayılardır.



# 1.yöntem

prime_number=int(input("Please enter te number: "))

if (prime_number==1):
    print("{} asal sayı değildir.".format(prime_number))
else:
    total=2
    lst=[]
    while (total<prime_number):
        if (prime_number%total ==0):
            lst.append(total)
        total=total+1
    if len(lst)==0:
        print("{} asal sayıdır.".format(prime_number))
    else:
        print("{} asal sayı değildir.".format(prime_number))
    
   
   

# 2.yöntem

def prime_number(number):
    if(number==1):
        return False
    elif (number==2):
        return True
    else:
        for i in range(2,number):
            if(number%i==0):
                return False
        return True
    
while True:
    number=input("Sayı: ")
    
    if (number=="q"):
        break
    else:
        number=int(number)
        if (prime_number(number)):
           print(number," asal bir sayıdır.")
        else:
            print(number," asal bir sayı değildir.")
   