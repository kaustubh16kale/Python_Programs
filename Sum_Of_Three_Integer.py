def triplets(numbers):
    if len(numbers)<3:
        raise Exception("Enter more than 6 numbers ")
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            for k in range(j+1,len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    print(numbers[i],numbers[j],numbers[k])
def main():
    numbers=[]
    try :
        num=None
        while num!=" ":
            num=(input("Enter the number : "))
            if num!=" ":
                numbers.append(int(num))
            print("space : " " to exit")
        triplets(numbers)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()