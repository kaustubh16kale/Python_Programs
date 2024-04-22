import numpy as np
import random as rm

def array(row,col,values):
    arr=np.array(values)
    return arr.reshape(row,col)

def main():
    values=[]
    try:
        row=int(input("Enter the value of rows : "))
        col=int(input("enter the values of columns : "))

    except Exception as e:
        print(e)
    
    for i in range(0,row*col):
        values.append(rm.randrange(1,100))
    
    print(array(row,col,values))

if __name__=="__main__":
    main()