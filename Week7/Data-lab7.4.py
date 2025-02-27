import json

def seat_insert_sort(data, last):
    count = 0

    for current in range(1, last + 1):
        item = data[current]
        walker = current - 1
        item_str = "".join(filter(str.isalpha, item))
        item_num = int("".join(filter(str.isdigit, item)) or 0)

        while walker >= 0:
            count += 1
            w_str = "".join(filter(str.isalpha, data[walker]))
            w_num = int("".join(filter(str.isdigit, data[walker])) or 0)
            if (w_str, w_num) > (item_str, item_num):
                data[walker + 1] = data[walker]
                walker -= 1
            else:
                break
        data[walker + 1] = item
        print(data)
    print(f"Comparison times: {count}")

if __name__ == "__main__":
    data = json.loads(input())
    last = int(input())
    seat_insert_sort(data,last)
