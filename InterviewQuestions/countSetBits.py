def countSetbits(n):
    count=0
    while(n):
        count+= n & 1
        print(n)
        print("count: ",count)
        n>>=1
        print(n)
    return count
print(countSetbits(9))
