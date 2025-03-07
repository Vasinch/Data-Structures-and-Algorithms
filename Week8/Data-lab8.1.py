import json

def coinExchange(amount, coins):
    print("Amount: " + str(amount))
    c = [10, 5, 2, 1]
    cc = {coin: 0 for coin in c}

    for coin in c:
        if amount <= 0:
            break
        nc = min(amount // coin, coins.get(coin, 0))
        cc[coin] = nc
        amount -= nc * coin

    if amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin, count in cc.items():
            print(f"  {coin} baht = {count} coins")
        print("Total number of coins: " + str(sum(cc.values())))

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    amount = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(amount, data)
main()