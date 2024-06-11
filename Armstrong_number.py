



# Bir sayının "Armstrong" sayısı olduğunu bulan bir algoritma
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
# sadece 4 basamaklı sayılar için geçerlidir.


armstrong_number=input("Enter the number (example number:4545): ")

length=[]
total=0
for i in str(armstrong_number):
   i=int(i)
   length.append(i)
   
   

vr = str(armstrong_number)[i] * str(armstrong_number)[length-1]
total=total+vr

if (armstrong_number==total):
    print("{} bir armstrong sayısıdır.",armstrong_number)
else:
    print("{} bir armstrong sayısı değildir.",armstrong_number)













