import json

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def knapsack(il, max):
    il.sort(key=lambda x: x.price / x.weight, reverse=True)

    print(f"Knapsack Size: {max} kg")
    print("===============================")

    ww = pp = 0
    for item in il:
        if ww + item.weight > max:
            break
        ww += item.weight
        pp += item.price
        print(f"{item.name} -> {item.weight} kg -> {item.price} THB")

    print(f"Total: {pp} THB")

def main():
    allitem = int(input())
    item = [Item(**json.loads(input())) for _ in range(allitem)]
    weight = float(input())
    knapsack(item, weight)
main()