

# PİSAGOR BULMA

def find_pythagorean():
    
    pisagor_lst=list()
    
    for i in range(1,101):
        for j in range(1,101):
            
            c=(i**2 + j**2) ** 0.5
            
            if(c==int(c)):
                pisagor_lst.append((i,j,int(c)))
    return pisagor_lst

for i in find_pythagorean():
    print(i)
    
    
    
    
    