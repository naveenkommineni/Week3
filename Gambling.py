def Gambling():
    import random
    stack=int(input('Enter the value:'))
    goal=int(input('Enter the goals'))
    trails=int(input('enter trails to perform'))
    bet=0
    wins=0
    for i in range(trails):
        cash=stack
        while cash>0 and cash<goal:
            bet+=1
            if random.randint(0,1)==0:
                cash+=1
            else:
                cash-=1
        if cash==goal:
            wins+=1
            wins_p=(wins/trails)*100
            avg_bets=bet//trails
    print(wins)
    print(wins_p)
    print(avg_bets)
Gambling()
