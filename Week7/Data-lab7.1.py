import json
def insertion_sort(data, last) :
    comT = 0
    for current in  range(1, last+1) :
        result = data[current]
        walker = current - 1

        while walker >= 0:
            comT += 1
            if data[walker] > result:
                data[walker + 1] = data[walker]
                walker -= 1
            else:
                break
        data[walker + 1] = result
        print(data)
    print(f"Comparison times: {comT}")

if __name__ == "__main__":
    data = json.loads(input())
    last = int(input())
    insertion_sort(data, last)
