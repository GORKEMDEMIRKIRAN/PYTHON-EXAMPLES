



# SAYININ OKUNUŞUNU ÇIKARTMA


# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi


# 1.YÖNTEM


def reading_number(blue):
    
    read=0
    first_lst=[[1,"on"],
                [2,"yirmi"],
                [3,"otuz"],
                [4,"kırk"],
                [5,"elli"],
                [6,"atmış"],
                [7,"yetmiş"],
                [8,"seksen"],
                [9,"doksan"]]
    second_lst=[[1,"bir"],
                [2,"iki"],
                [3,"üç"],
                [4,"dört"],
                [5,"beş"],
                [6,"Altı"],
                [7,"yedi"],
                [8,"sekiz"],
                [9,"dokuz"]]
    blue=int(blue)
    ones_step=str(blue)[0]
    those_step=str(blue)[1]
    ones=int(ones_step)
    those=int(those_step)
    for i in first_lst:
        if (ones==i[0]):
            read=i[1]
    for j in second_lst:
        if(those==j[0]):
            read=read+" "+j[1]
    return read    
    
while True:
    value=input("Enter the number: ")
    if (value=="q"):
        break
    else:
        print(reading_number(value))
        
        
    
    
    
    
        
# 2.YÖNTEM       



def read(value):
    
    birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    
    birinci = value % 10
    ikinci = value // 10
    
    return onlar[ikinci] + " " + birler[birinci]

    
while True:
    
    number=  int(input("Number: "))
    if (number=="q"):
        break
    else:
        print(read(number))