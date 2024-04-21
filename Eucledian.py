import math

def eucledian(x,y):
    origin_x=0
    origin_y=0
    return math.sqrt(x**2 + y**2)

def main():
    try:
        x=int(input("Enter the x co-ordinate : "))
        y=int(input("Enter the y co-ordinate : "))
        distance=eucledian(x,y)
        print(distance)
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()


