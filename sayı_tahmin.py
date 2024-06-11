

# SAYI TAHMİN OYUNU


import random

import time

print("""
      
      Sayı Tahmin Oyunu
      
      1 ile 40 arasında sayıyı tahmin edin.
      
      """)


random_number=random.randint(1,40)

estimate_rights=7
while True:
    
    rnd=int(input("Tahmininiz: "))
    if (rnd < random_number):
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin...") 
        estimate_rights=estimate_rights-1
        
    elif (rnd > random_number):
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin....")  
        estimate_rights=estimate_rights-1
    else:
        print("Bilgiler sorgulanyor....")
        time.sleep(1)
        print("Tebrikler sayımız",random_number)
        break
    if (estimate_rights==0):
        print("Tahmin hakkı bitti....")
        print("Sayımız: ",random_number)
        break
    
    
    
        
        
