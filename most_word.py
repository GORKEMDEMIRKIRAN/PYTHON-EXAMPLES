
# Python dilindi en çok geçen 5 kelimeyi veren fonksiyon   

#  Örnek bir veri vererek çalışması gösterilmiştir.

vari="EN Çok kullanılan çok sayıda bulunan metin sayıda EN Çok kullanılan çok sayıda bulunan metin sayıda bulunan metin sayıda bulma sonucu"

def most_word(variable):  
    word_list=list()  
    # değişkenin içindeki değerlerin hepsini küçük yaptık.
    variable=variable.lower()
    # Boşluk noktalarını seçerek kelimeleri ayırdık.         
    value=variable.split(' ')
    # kelimelerin sayısını hesaplamak için bir sözlük kurduk.
    word_count={}
    for word in value:
        if word in word_count:
            word_count[word]=word_count[word] + 1
        else:
            word_count[word]= 1
    words=sorted(word_count.items())
    reverse_words=words[::-1]   
    select_words=reverse_words[:5]
    print(select_words)   
    
         
most_word(vari)