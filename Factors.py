def prime_factors(N):
    if  N<=0:
        raise Exception("Enter a positive value to find factorization ")
    num=2
    while (num*num<=N):
        while(N>1):
            while N%num==0:
                print(num)
                N=N/num
            num+=1

def main():
    try:
        N=int(input("Enter a number to find factorization"))
        prime_factors(N)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()