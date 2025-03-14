import json

def convert_key(data):
    return {int(k): v for k, v in sorted(data.items(), key=lambda x: -int(x[0]))}

def coinExchange(total, denominations):
    dp = [{denom: 0 for denom in denominations}] + [{} for _ in range(total)]
    min_coins = [0] + [float('inf')] * total

    for amt in range(1, total + 1):
        for value, limit in denominations.items():
            if value <= amt and min_coins[amt - value] < float('inf') and dp[amt - value].get(value, 0) < limit:
                if min_coins[amt] > min_coins[amt - value] + 1:
                    min_coins[amt] = min_coins[amt - value] + 1
                    dp[amt] = dp[amt - value].copy()
                    dp[amt][value] = dp[amt].get(value, 0) + 1
    
    if min_coins[total] == float('inf'):
        print(f"Amount: {total}\nCan not exchange.")
    else:
        print(f"Amount: {total}\nCoin exchange result:")
        print("\n".join(f"  {k} baht = {v} coins" for k, v in dp[total].items()))
        print(f"Number of coins: {sum(dp[total].values())}")

def main():
    amount = int(input())
    coinList = convert_key(json.loads(input()))
    coinExchange(amount, coinList)

main()