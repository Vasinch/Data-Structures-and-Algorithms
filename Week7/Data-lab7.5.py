import json
def selection_sort(data, last):
    count = 0

    for i in range(last + 1):
        small = i
        for j in range(i + 1, last + 1):
            count += 1
            smallstr, smalln = "".join(filter(str.isalpha, data[small])), int("".join(filter(str.isdigit, data[small])) or 0)
            jstr, jnum = "".join(filter(str.isalpha, data[j])), int("".join(filter(str.isdigit, data[j])) or 0)
            if (jstr, jnum) < (smallstr, smalln):
                small = j
        print(data)
    print(f"Comparison times: {count}")

if __name__ == "__main__":
    data = json.loads(input())
    last = int(input())
    selection_sort(data,last)
