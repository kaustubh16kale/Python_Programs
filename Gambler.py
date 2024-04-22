import random as rm
def gambling(goal,stake,bet):
    if stake<bet:
        raise ValueError("invalid stake amount : bet amount is greater than stake amount")
    if goal<stake:
        raise ValueError("Invalid goal entered : goal should be greater than stake")
    money=stake
    count=0
    bet_won=0
    bet_loss=0
    while money!=0 and money!=goal:
        play=rm.randint(0,1)
        if play==0:
            print(f"bet loss : current bet {count}  : current money : {money} ")
            money-=bet
            bet_loss+=1
        else:
            print(f"bet won : current bet {count} : current money : {money}")
            money+=bet
            bet_won+=1
        count+=1
    if money==goal:
        print(f"Goal reached and you won : {money-stake}")
    else:
        print(f"You loss all your money : {stake-money}")
    print(f"total numbers of bets placed is {count}")
    print(f"Total win % is {(bet_won/count)*100}")
    print(f"Total loss % is {(bet_loss/count)*100}")
    
def main():
    try:
        goal=int(input("enter the goal amount : "))
        stake=int(input("Enter initial money (stake_amount) : "))
        bet=int(input("Enter the amount for single bet : "))
        gambling(goal,stake,bet)
    except ValueError as e:
        print(e)


if __name__=="__main__":
    main()

