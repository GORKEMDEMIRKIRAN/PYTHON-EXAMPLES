

fibonnacci_number=int(input("Enter the number: "))

if (fibonnacci_number==1):
    fb_list=[1]
    print("fibbonacci list: ",fb_list)
elif (fibonnacci_number==2):
    new_list=[1,1]
    print("fibbonacci list: ",new_list)
else:
    new_list=[1,1]
    while (i<fibonnacci_number):
        a = i+(i+1)
        new_list.append(a)
    print(new_list)
