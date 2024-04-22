import math

def windchill(t,v):
    if t>50:
        raise ValueError("invalid value of t ,should be below 50 : ")
    if 3>v>120:
        raise ValueError("Enter the valid value of v in range 3-120 : ")
    else:
        return 35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v,0.16)

def main():
    try:
        t=int(input("Enter the value of t : "))
        v=int(input("Enter the value of v : "))
        w=windchill(t,v)
        print(w)
    except ValueError as e:
        print(e)


if __name__=="__main__":
    main()
