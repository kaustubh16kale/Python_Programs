import random as rm
'''flip_numeber is the user input from the user'''
def Flip_Coin(flip_number):
    if flip_number<0:
        raise ValueError("Enter the number greater than 0 ")
    
    heads=0
    tail=0
    times_fliped=0

    while times_fliped!=flip_number:
        random_num=rm.randint(0,1)
        if random_num>0.5:
            heads+=1
        else:
            tail+=1
        times_fliped+=1
    print(f"Numbers of times coin flipped {flip_number}")
    print(f"The percentage of Head is {(heads/flip_number)*100} %")
    print(f"The percentage of Tails is {(tail/flip_number)*100} %")
        
def main():
    try:
        flip_number=int(input("Enter the number of times coin to be flipped : "))
        Flip_Coin(flip_number)
    except ValueError:
        print("Enter a valid Number should be positive")
        main()

if __name__=="__main__":
    main()

