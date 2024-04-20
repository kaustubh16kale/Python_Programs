def User_Input():
    name=input("enter your name ")
    if len(name)<3:
        print(" Enter a valid user name containing more than 3 letters ")
        User_Input()
    else:
        print(f" Hello {name} , How are you ?")

if __name__=="__main__":
    User_Input()
            
