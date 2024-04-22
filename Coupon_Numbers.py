import random
def coupon_number(numbers_coupons,num_digits):
    coupon_genreated=0
    coupons=[]
    while coupon_genreated!=numbers_coupons:
        digit=""
        for i in range(num_digits):
            digit+=str(random.randint(0,9))
        coupons.append(int(digit))
        coupon_genreated+=1
    for i in coupons:
        print(i)


def main():
    try:
        number_coupons=int(input("Enter the numbers of coupons to be generated : "))
        num_digits=int(input("Enter the number of digits in one coupons : "))
        coupon_number(number_coupons,num_digits)
    except Exception as e:
        print(e)
    

if __name__=="__main__":
    main()