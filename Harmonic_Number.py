def harmonic_number(number):
    output=0  
    if number<=0:
        raise ValueError("Enter the number greater than 0 ")
    for num in range(1,number+1):
        output+=1/num
    print(output)

def main():
    try:
        number=int(input("Enter the number : "))
        harmonic_number(number)
    except ValueError as e:
        print("The number should not be 0 or less than 0 ")

if __name__=="__main__":
    main()
