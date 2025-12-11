def hash_quadratic(d):
    size=23
    htable=HashTable(size)

    for key in d:
        h=(5*key+7)%size
        
        j=0
        while True:
            pos=(h+j*j)%size
            if htable.lookup(pos)=="-":
                htable.add(pos,key)
                break
            j+=1
    return htable

   
def hash_double(d):
    size=23
    htable=HashTable(size)
    
    for key in d:
       h=(5*key+7)%size
       h2=11-(key%11)
       j=0
       while True:
           pos=(h+j*h2)%size
           if htable.lookup(pos)=="-":
               htable.add(pos,key)
               break
           j+=1
        
    return htable
 