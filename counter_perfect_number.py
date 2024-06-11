

# MUKEMMEL SAYI BULMA

# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. 
# Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).


def perfect_number(value):
    value_lst=list()
    value=int(value)
    total=0
    for i in range(1,value):
        if(value%i==0):
            value_lst.append(i)
    for index in value_lst:
        total=total+index
    if (total==value):
        # print(value_lst)
        return value 
    # else:
    #     print(value_lst)
    #     print("{} mükemmel bir sayı değildir.".format(value))
        
while True:
    # number=input("Enter the number: ")
    # if (number=="q"):
    #     break
    # else:
        for i in range(1,1001):
            if(perfect_number(i)):
                print("Mükemmel sayı: ",i)
        break




















    
    
        
    






