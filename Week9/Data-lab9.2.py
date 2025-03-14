import json

def knapsack(g, cap):
    dp = [0] * (cap + 1)
    track = [{} for _ in range(cap + 1)]

    for n, val, wei in g:
        for w in range(cap, wei - 1, -1):
            if dp[w] < dp[w - wei] + val:
                dp[w] = dp[w - wei] + val
                track[w] = track[w - wei].copy()
                track[w][n] = (wei, val)

    item = sorted(track[cap].items())
    return dp[cap], [(n, w, v) for n, (w, v) in item]

def main():
    i, w = json.loads(input()), int(input())
    nax, item = knapsack(i, w)
    print(f"Total: {nax}")
    for n, w, v in item:
        print(f"{n} -> {w} kg -> {v} THB")
main()
