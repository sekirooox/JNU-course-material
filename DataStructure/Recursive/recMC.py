coin_list=[1,5,10,25]
coin_list=sorted(coin_list,reverse=True)
def recMC(memo,remain_value):
    if remain_value in coin_list :
        return 1
    if memo[remain_value]!=0:
        return memo[remain_value]

    res=10e+6
    for i in [c for c in coin_list if c<=remain_value]:
        num_coins=recMC(memo,remain_value-i)+1
        memo[remain_value-i]=num_coins
        res=min(res,num_coins)
    return res

if __name__=='__main__':
    coin_value=63
    memo=[0]*(coin_value+1)

    print(recMC(memo,63))
    print(memo)
