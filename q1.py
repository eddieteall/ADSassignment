# (a)
def compute_winner(moves_A, moves_B):
    a_score=0
    b_score=0

    for i in range(len(moves_A)):
        a=moves_A[i]
        b=moves_B[i]

        if a == b:
            continue
        elif (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
            a_score+=1
        else:
            b_score+=1

    if a_score > b_score:
        return 'A'
    elif b_score > a_score:
        return 'B'
    else:
        return 'D'


#(b)
def encode(moves):
    compressed=""
    i=0

    while i < len(moves):
        repeat=True
        temp=i
        tempM=moves[temp]
        repeatNum=1

        while repeat==True and temp+1<len(moves):
            if moves[temp+1]==tempM:
                repeatNum+=1
                temp+=1
            else:
                repeat=False

        compressed+=tempM+str(repeatNum)
        i=temp+1

    return compressed

#(c)
def decode(compressed_moves):
   if compressed_moves == "":
       return ""
   
   char=compressed_moves[0]
   numRepeats=int(compressed_moves[1])

   decompressed = ""
   
   for _ in range(numRepeats):
       decompressed+=char

   return decompressed+decode(compressed_moves[2:])

#(d)
def compute_winner_compressed(compressed_moves_A, compressed_moves_B):
    a_score=0
    b_score=0

    i=0
    j=0

    countA=0
    countB=0

    while i<len(compressed_moves_A) and j<len(compressed_moves_B):

        if countA==0:
            moveA=compressed_moves_A[i]
            countA=int(compressed_moves_A[i+1])
            i+=2

        if countB==0:
            moveB=compressed_moves_B[j]
            countB=int(compressed_moves_B[j+1])
            j+=2

        if moveA!=moveB:
            if (moveA=='R' and moveB=='S') or (moveA=='S' and moveB=='P') or (moveA=='P' and moveB=='R'):
                a_score+=1
            else:
                b_score+=1

        countA-=1
        countB-=1

    if a_score>b_score:
        return 'A'
    elif b_score>a_score:
        return 'B'
    else:
        return 'D'
moves_a = "RRSPPS"
moves_b = "RSPRSP"


print(compute_winner(moves_a,moves_b)=="A")
print(encode(moves_a)=="R2S1P2S1")
print(encode(moves_b)=="R1S1P1R1S1P1")
print(decode("R2S3P1")=="RRSSSP")
print(compute_winner_compressed(encode(moves_a),encode(moves_b))=="A")
