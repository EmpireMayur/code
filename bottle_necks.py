T=int(input('no. of test cases'))
for i in range(T):

    n=int(input('no. of elements'))
    arr=list(map(int,input().split()))

    freqs={}
    max_freq=-1
    for num in arr:
        if num in freqs:
            freqs[num]=freqs[num]+1
        else:
            freqs[num]=1

        max_freq=max(max_freq,freqs[num])

    print(max_freq)
    
    print(arr)
