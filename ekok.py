



# EKOK BULMA (EN KÜÇÜK ORTAK BÖLEN)
def ekok(number1,number2):
    i=2
    ekok=1
    while True:
        if (number1%i==0 and number2%i==0):
            ekok=ekok * i 
            
            # Burada number1 değişkeninin i'yi kaç kere böldüğü
            # 5/4 dersek 5'te 4 değeri 1 tane var.
            number1=number1//i  
            number2=number2//i 
        elif (number1%i==0 and number2%i!=0):
            ekok=ekok * i
            
            number1=number1//i
        elif (number1%i != 0 and number2%i == 0):
            ekok=ekok * i
            
            number2=number2//i
            
        else:
            i=i+1
        
        if (number1==1 and number2==1):
            break
    return ekok


while True:
    new1=int(input("Enter the first number: "))
    new2=int(input("Enter the second number: "))
    if (new1=="q" or new2=="q"):
        break
    else:
        print(ekok(new1,new2))