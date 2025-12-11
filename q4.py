def sar(k):
    def build(seq, prefix_sum):
        if len(seq)==k:
            if prefix_sum==0:
                return seq
            else:
                return None

        for x in [1, 0, -1]:                    
            new_sum=prefix_sum+x
            if new_sum >= 0:
                next_seq = build(seq+[x], new_sum)
                if next_seq is not None:
                    return next_seq

        return None

    return build([], 0)


def is_sar(s):
    total=0
    prefix=0
    for x in s:
        prefix+=x
        if prefix<0:
             return False
        total+=x
    
    if total==0:
        return True
    else:
        return False

    
def all_sars(k):
    results = []

    def backtrack(seq,prefix_sum):
        if len(seq)==k:
            if prefix_sum==0:
                results.append(seq.copy())
            return

        for x in [1, 0, -1]:
            new_sum=prefix_sum+x
            if new_sum>=0:
                seq.append(x)
                backtrack(seq, new_sum)
                seq.pop() 
    backtrack([], 0)
    return results 




