



# KUMANDA SINIFI

# Kumanda özellikleri
# kanallar

# tv ses arttırma azaltma
# tv açma ve kapama
# kanal ekleme
# rastgele kanal çevirme
# kanal sayısı
# tv genel durumu


import random

class command():
    def __init__(self,tv_case="close",tv_sound=0,canal_lst=["trt","star","fox"],canal="trt"):
        self.tv_case=tv_case
        self.tv_sound=tv_sound
        self.canal_lst=canal_lst
        self.canal=canal
    def __str__(self):
        return "TV DURUMU: {} \nTV SES: {} \nMEVCUT KANAL: {} \nKANALLAR: {}".format(self.tv_case,self.tv_sound,self.canal,self.canal_lst)
    
    def __len__(self):
        return len(self.canal_lst)
    
    def tv_open(self):
        if (self.tv_case == "open"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor.....")
            self.tv_case="Open"
            
    def tv_close(self):
        if (self.tv_case == "close"):
            print("Televizyon zaten kapalı....")
        else:
            print("Televizyon kapanıyor...")
            self.tv_case="close"
    
    def add_canal(self,new_canal):
        self.canal_lst.append(new_canal)
        print("Kanal eklendi.")
        
    def random_canal(self):
        randoms=random.randint(0,len(self.canal_lst)+1)
        self.canal=self.canal_lst[randoms]
        print("Şu anki kanal: ",self.canal)
            
    def sound_plus_minus(self):
        
        while True:
            character=input("Arttırmak için '>' Azaltmak için '<' Tamam ise 'q' basınız")
            if (character=="<"):
                if(self.tv_sound != 0):
                    self.tv_sound=self.tv_sound-1
                    print("ses: ",self.tv_sound)
            elif (character==">"):
                if(self.tv_sound !=32):
                    self.tv_sound=self.tv_sound+1
                    print("ses: ",self.tv_sound)
            else:
                print("Ses güncellendi: ",self.tv_sound)
                break
            

tv_command=command()
print("""**********************
      Televizyon Uygulaması
      
      İşlemler;
      
      1. Televizyonu Aç
      2.Televizyonu Kapat
      3.Televizyon Bilgileri
      4.Kanal Sayısını Öğrenme
      5.Kanal Ekle
      6.Rastgele Kanal'a Geç
      7.Sesi Azalt Ya da Artır
      
      Çıkmak için "q" basın.
      
      """)   

while True:
    process=input("İşlemi seçiniz: ")
    
    if(process=="q"):
        print("Programdan çıkılıyor......")
        break
    elif (process == "1"):
        tv_command.tv_open()
    elif (process == "2"):
        tv_command.tv_close()
    elif (process == "3"):
        print(tv_command)
    elif (process=="4"):
        print("Kanal sayısı: ",len(tv_command))
    elif(process=="5"):
        new_canal=input("Eklemek istediğiniz kanalları ',' ile ayırarak girin:  ")
        append_canal=new_canal.split(",")
        for cnl in append_canal:
            tv_command.add_canal(cnl)
        print("Kanallar listeye başarıyla eklendi.")
    elif (process=="6"):
        tv_command.random_canal()
    elif (process=="7"):
        print(tv_command.sound_plus_minus())
    else:
        print("Geçersiz işlem....")
        
