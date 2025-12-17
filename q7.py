def merge(A,B):
    """Return the sorted lists A and B merged into
    a single list L
    """
    L=[]
    while A and B:
        if A[0] <= B[0]:
            L.append(A.pop(0))
        else:
            L.append(B.pop(0))
    L.extend(A)
    L.extend(B)
    return L

def check_list(L):
    sorted_flag=True
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            sorted_flag=False
            break
    if sorted_flag:
        return (L,None)
    
    A=[]
    B=[]

    for x in L:
        if not A or x>=A[-1]:
            A.append(x)
        elif not B or x>=B[-1]:
            B.append(x)
        else:
            return (None,None)
        
    for i in range(len(B)-1):
        if B[i]>B[i+1]:
            return (None,None)
        
    return (A,B)

def best_pivot(L,p1,p2,p3):
    def balance(p):
        left=0
        right=0
        for x in L:
            if x<p:
                left+=1
            elif x>p:
                right+=1
        return abs(left-right)
    
    best=p1
    best_diff=balance(p1)

    for p in [p2,p3]:
        diff=balance(p)
        if diff<best_diff:
            best=p
            best_diff=diff
    return best
def extra_check_quicksort(L):
    if len(L)<=1:
           return L
    
    (A,B)=check_list(L)

    if A is not None and B is None:
        return A
    elif A is not None and B is not None:
        left=extra_check_quicksort(A)
        right=extra_check_quicksort(B)
        return merge(left,right)
    
    first=L[0]
    middle=L[len(L)//2]
    last=L[-1]

    pivot=best_pivot(L,first,middle,last)

    left=[]
    right=[]

    for x in L:
        if x<pivot:
            left.append(x)
        elif x>pivot:
            right.append(x)

    return extra_check_quicksort(left)+[pivot]+extra_check_quicksort(right)

    

