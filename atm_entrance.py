


# ATM ENTRANCE

        
# 1- BAKİYE SORGULAMA

# 1.1- Bakiye sorgulama
# 1.2- Nakit avans durumu sorgulama
# 1.3- Kredi durumu sorgulama


# 2- PARA ÇEKME

# 2.1- Bakiyeden çekme
# 2.2- Nakit avans hesabından çekme
# 2.3- Kredi hesabından çekme


# 3- PARA YATIRMA

# 3.1- Bakiyeye para yatırma
# 3.2- Nakit avans hesabına para yatırma
# 3.3- Kredi hesabına para yatırma

    


# Veri tabanı bağlanarak kullanıcı ismi ve şifresi döndürülür.
# Çalışma mantığı için isim ve parola oluşturulmuştur.
# Kullanıcının bakiyesine göre kredi limiti ve nakit avans limiti belirleniyor.
import time

atm_user_name="ELLIE"
atm_user_surname="CRUZ"
atm_user_password=9876
user_balance=10000
user_credit_state=user_balance/4
user_cash_advance=user_balance/2

print("ATM GİRİŞİ")
print("Kartımızı Takınız")
print("Giriş yapılıyor lütfen bekleyiniz.....")
time.sleep(1)

while True:

    print("Welcome {} {}".format(atm_user_name,atm_user_surname))

    print(""" Lütfen genel işlem numarasını seçiniz:
      1 - BAKİYE İŞLEMLERİ
      2 - PARA ÇEKME İŞLEMLERİ
      3 - PARA YATIRMA İŞLEMLERİ
      İŞLEMLERİ BİTİRMEK İÇİN  q BASINIZ
      """)
    process_number=input("Genel işlem numarası: ")



    if (process_number=="1"):
        print("BAKİYE İŞLEMLERİ")
        print("""Lütfen bakiye işlem numarasını giriniz: 
          1-NAKİT AVANS DURUMUNU SORGULAMA
          2-KREDİ DURUMUNU SORGULAMA
          """)
        balance_number=input("Bakiye işlemleri numarasını giriniz: ")
        if (balance_number=="1"):
            print("NAKİT AVANS LİMİTİNİZ {}".format(user_cash_advance))
            # print("NAKİT AVANS ÇEKME İSTİYORSANIZ A BASINIZ")
        elif (balance_number=="2"):
            print("KREDİ LİMİTİNİZ {}".format(user_credit_state))
            # print("KREDİ ÇEKMEK İSTİYORSANIZ B BASINIZ")
        else:
            print("Geçersiz bir işlem numarasını girdiniz.")
    
    
    elif (process_number=="2"):
        print("PARA ÇEKME İŞLEMLERİ")
        print("""Lütfen para çekme işlem numarasını giriniz: 
          1-BAKİYEDEN PARA ÇEKME
          2-NAKİT AVANS PARA ÇEKME
          3-KREDİDEN PARA ÇEKME
          """)
        pull_number=input("Para çekme işlem numarasını giriniz: ")
        if (pull_number == "1"):
            print("GÜNCEL BAKİYENİZ {}".format(user_balance))
            money=int(input("PARA ÇEKMEK İSTEDİĞİNİZ MİKTARI GİRİNİZ: "))
            if (user_balance>money) or (user_balance==money):
                user_balance=user_balance-money
                print("Para çekme işleminiz tamamlanmıştır.")
                print("Paranızı alınız..")
            
            else:
                print("Hesabınızda yeterli para yok.")
                print("Geçerli bir miktar giriniz.")
            
        elif (pull_number == "2"):
            print("GÜNCEL NAKİT AVANS LİMİTİNİZ {}".format(user_cash_advance))   
            money=int(input("PARA ÇEKMEK İSTEDİĞİNİZ NAKİT AVANS MİKTARI GİRİNİZ: "))
            if (user_cash_advance>money) or (user_cash_advance==money):
                user_cash_advance=user_cash_advance-money
                print("Nakit avans işleminiz tamamlanmıştır.")
               
            else:
                print("Nakit avans limitinden fazla çekemezsiniz.")
                print("Geçerli bir nakit avans limiti giriniz.")
             
        elif  (pull_number == "3"): 
            print("GÜNCEL KREDİ LİMİTİNİZ {}".format(user_credit_state))
            money=int(input("PARA ÇEKME İSTEDİĞİNİZ KREDİ LİMİTİNİ GİRİNİZ: "))
            if (user_credit_state>money) or (user_credit_state==money):
                user_credit_state=user_credit_state-money
                print("Kredi çekme işleminiz tamamlanmıştır.")
            
            else:
                print("Yetersiz kredi limiti girdiniz.")
                print("Geçerli bir kredi limiti giriniz.")
        else:
            print("Geçersiz bir bakiye işlemleri numarası girdiniz.")
      
                      
    
    elif (process_number=="3"):
        print("PARA YATIRMA İŞLEMLERİ")
        print("""Lütfen para yatırma işlem numarasını giriniz: 
          1-BAKİYEYE PARA YATIRMA
          2-NAKİT AVANS PARA YATIRMA
          3-KREDİYE PARA YATIRMA
          """)
        put_number=input("Para yatırma işlem numarasını giriniz: ")
        
        if (put_number == "1"):
            print("GÜNCEL BAKİYENİZ {}".format(user_balance))
            money=int(input("PARA YATIRMAK İSTEDİĞİNİZ MİKTARI GİRİNİZ: "))
            user_balance=user_balance+money
            print("Bakiyenize para yatırma işleminiz tamamlanmıştır.")
            print("Bakiyenize {} tl paranız yaırıldı.".format(money))
            print("Güncel hesap bakiyeniz {} tl ".format(user_balance))
          

        elif (put_number =="2"):
            print("GÜNCEL NAKİT AVANS LİMİTİNİZ {}".format(user_cash_advance))   
            money=int(input("PARA YATIRMAK İSTEDİĞİNİZ NAKİT AVANS MİKTARINI GİRİNİZ: "))
            user_cash_advance=user_cash_advance+money
            print("Nakit avans hesabınıza para yatırma işleminiz tamamlanmıştır.")
            print("Nakit avans hesabınıza {} tl paranız yaırıldı.".format(money))
            print("Güncel nakit avans hesap  bakiyeniz {} tl ".format(user_balance))
      
     

        elif (put_number =="3"): 
            print("GÜNCEL KREDİ LİMİTİNİZ {}".format(user_credit_state))
            money=int(input("PARA YATIRMAK İSTEDİĞİNİZ KREDİ MİKTARINI GİRİNİZ: "))
            user_credit_state=user_credit_state+money
            print("Kredi hesabınıza para yatırma işleminiz tamamlanmıştır.")
            print("Kredi bakiyenize {} tl paranız yatırıldı.".format(money))
            print("Güncel kredi hesap bakiyeniz {} tl".format(user_credit_state))


        else:
            print("Geçersiz bir bakiye işlemleri numarası girdiniz.")
 
        
    elif (process_number=="q"):
        print("KARTINIZI ALMAYI UNUTMAYINIZ...")
        break  
    else:
        print("Geçerli bir işlem numarası giriniz...")
