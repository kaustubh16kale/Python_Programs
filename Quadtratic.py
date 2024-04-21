import math
def quadratic(a,b,c):
    delta= b * b - 4 * a * c
    if delta==0:
        root = -b / (2 * a)
        print("The root of the equation is:", root)
    elif delta < 0:
        print("No real roots exist.")
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Root 1 of x =", root1)
        print("Root 2 of x =", root2)

def main():
    try:
        a=int(input("Enter the value of a : "))
        b=int(input("Enter the value of b : "))
        c=int(input("Enter the value of c : "))
        quadratic(a,b,c)
    except Exception as e:
        print(e)
        print("Enter only numeric values ")
        main()
 

if __name__=="__main__":
    main()