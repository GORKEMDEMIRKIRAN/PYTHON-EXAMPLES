

# TAM BÖLENİNİ BULMA

# Girdiğizi sayının bölenlerini liste içerisinde size çevirir.

def tam_bolen_bulma(number):
    lst=[]
    for i in range(1,number+1):
        if (number%i == 0):
            lst.append(i)
    return lst

while True:
    value=input("TAM BÖLENLERİNİ BULMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ: ")
    if (value=="q"):
        break
    else:
        value=int(value)
        print(tam_bolen_bulma(value))
        


