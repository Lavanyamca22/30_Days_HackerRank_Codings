# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(0,T):
    S = input()
    ES = ""
    OS = ""
    for i in range(0,len(S)):
        if(i%2==0):
            ES += S[i]
        else:
            OS += S[i]
    print(ES,OS)

