def power(N):
    if 0<=N<31:
        raise ValueError("Enter the value of N less than 31")
    else:
        for power in range(N):
            print(f"2 ^ {power} is {2**power}")

def main():
    try:
        N=int(input("Enter the power "))
        power(N)
    except ValueError as e:
        print(e)


if __name__=="__main__":
    main()