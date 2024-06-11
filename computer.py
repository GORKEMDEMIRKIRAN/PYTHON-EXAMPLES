


# BİLGİSAYAR SINIFI


class computer():
    def __init__(self,computer_type=["Dell","Lenovo",
                                     "Monster","Hp",
                                     "Acer", "Apple",
                                     "Asus", "Casper",
                                     "MSI","Huawei"],
                 panel_shape=[12,13,14,15.6,17,17.3],
                 ram=0,ssd=0,harddisk=0,
                 ekran_kartı=["GTX3050","GTX3060","GRX3070"],
                 işlemci=["ryzen3","ryzen5","ryzen7","ryzen9","i3","i5","i7","i9"],
                 
                 select_computer_type="Dell",
                 select_panel=15.6,
                 select_ram=8,
                 select_ssd=256,
                 select_harddisk=1000,
                 select_ekran_kartı="GTX3050",
                 select_işlemci="i3"):
                 
        self.computer_type=computer_type
        self.panel_shape=panel_shape
        self.ram=ram
        self.ssd=ssd
        self.harddisk=harddisk
        self.ekran_kartı=ekran_kartı
        self.işlemci=işlemci
        self.select_copmputer_type=select_computer_type
        self.select_panel=select_panel
        self.select_ram=select_ram
        self.select_ssd=select_ssd
        self.select_harddisk=select_harddisk
        self.select_ekran_kartı=select_ekran_kartı
        self.select_işlemci=select_işlemci
        
    def __str__(self):
        print("BİLGİSAYAR BİLGİLERİ") 
        return "BİLGİSAYAR MARKASI : {} \nPANEL BOYUTU: {} inç \nRAM KAPASİTESİ: {} gb\nSSD KAPASİTESİ: {} gb\nHARDDISK KAPASİTESİ: gb{} \nEKRAN KARTI MODELİ: {} \nİŞLEMCİ MODELİ: {}".format(self.computer_type,self.panel_shape,self.ram,self.ssd,self.harddisk,self.ekran_kartı,self.işlemci)
    
    
    
    def select_computer_types(self,computer_information):
        self.select_computer_type=computer_information
        return self.select_computer_type
    def select_panel_shapes(self,panel_information):
        self.select_panel=panel_information
        return self.select_panel
    def select_ekran_kartı(self,ekran_kartı_information):
        
        
        
        
        
    def add_ram(self,n_ram):
        print("Mevcut slot sayısı 2 tanedir.")
        slot_number=int(input(""))
    
    
    # RAM,SSD,HARDDISK markalara göre maksimum kapasiteleri belli
    # eklenen yeni ram,ssd ,harddisk boyutu kapasiteyi aşmıyorsa eklenir.
    def change_ram(self,new_ram):
        for model in self.computer_type:
            if model =="Dell":
                if (self.ram+new_ram <= 32):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."                
            elif model =="MSI":
                if (self.ram+new_ram <= 64):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."     
            elif model =="Lenovo":
                if (self.ram+new_ram <= 128):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Monster":
                if (self.ram+new_ram <= 64):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Hp":
                if (self.ram+new_ram <= 32):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Acer":
                if (self.ram+new_ram <= 128):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Apple":
                if (self.ram+new_ram <= 64):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Casper":
                if (self.ram+new_ram <= 64):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Asus":
                if (self.ram+new_ram <= 128):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            elif model =="Huawei":
                if (self.ram+new_ram <= 32):
                    self.ram=new_ram
                else:
                    return "Kapasite aşıldı."
            else:
                break
  
    def change_ssd(self,new_ssd):
        for model in self.computer_type:
            if model =="Dell":
                if self.ssd <= 512:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Asus":
                if self.ssd <= 1000:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Lenovo":
                if self.ssd <= 1500:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Monster":
                if self.ssd <= 2000:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Hp":
                if self.ssd <= 2000:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Acer":
                if self.ssd <= 1500:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Apple":
                if self.ssd <= 1500:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Casper":
                if self.ssd <= 2000:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="MSI":
                if self.ssd <= 512:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            elif model =="Huawei":
                if self.ssd <= 512:
                    self.ssd=self.ssd+new_ssd
                else:
                    return "Kapasite aşıldı."
            else:
                break
        
    def change_harddisk(self,new_harddisk):
        for model in self.computer_type:
            if model =="Dell":
                if self.harddisk <= 512:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Asus":
                if self.harddisk <= 1000:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Lenovo":
                if self.harddisk <= 1500:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Monster":
                if self.harddisk <= 2000:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Hp":
                if self.harddisk <= 2000:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Acer":
                if self.harddisk <= 1500:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Apple":
                if self.harddisk<= 1500:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Casper":
                if self.harddisk<= 2000:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="MSI":
                if self.harddisk <= 512:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            elif model =="Huawei":
                if self.harddisk <= 512:
                    self.harddisk=self.harddisk+new_harddisk
                else:
                    return "Kapasite aşıldı."
            else:
                break   

computers=computer()
print(computers)
print(computers.change_harddisk(600))
print(computers)


# while True:
#     print("""
#           BİLGİSAYAR TOPLAMA
          
#           İşlemler
          
#           1-Bilgisayar markası
#           2-Panel boyutu
#           3-Ram kapasitesi
#           4-Ssd kapasitesi
#           5-Harddisk kapasitesi
#           6-Ekran kartı
#           7-İşlemci
#           """)
    # print(computers)
    # process_number=int(input("İşlem numarasını seçiniz: "))
    # if (process_number=="1"):
        
    # elif (process_number=="2"):
    # elif (process_number=="3"):
    # elif (process_number=="4"):
    # elif (process_number=="5"):
    # elif (process_number=="6"):
    # elif (process_number=="7"):
    # else:
    #     print("Geçersiz işlem girdiniz....")
    