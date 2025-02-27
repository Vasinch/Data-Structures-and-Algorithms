import json
def bubble_sort(data, last):
    count = 0

    for i in range(last):
        sw = False
        for j in range(last, i, -1):
            count += 1
            a, b = data[j], data[j - 1]
            ass, an = "".join(filter(str.isalpha, a)), int("".join(filter(str.isdigit, a)) or 0)
            bs, bn = "".join(filter(str.isalpha, b)), int("".join(filter(str.isdigit, b)) or 0)
            if (ass, an) < (bs, bn):
                data[j], data[j - 1] = b, a
                sw = True
        print(data)
        if not sw:
            break
    print(f"Comparison times: {count}")

if __name__ == "__main__":
    data = json.loads(input())
    last = int(input())
    bubble_sort(data,last)
