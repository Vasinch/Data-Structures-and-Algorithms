import json

def main(city, station):
    st = [json.loads(input()) for _ in range(station)]
    uc = set(city)
    select = []

    while uc:
        best = None
        bc = set()
        for station in st:
            c = set(station["Cities"]) & uc
            if len(c) > len(bc):
                best = station
                bc = c

        if not best:
            break

        select.append(best["Name"])
        uc -= bc
    select.sort()
    print(select)
main(json.loads(input()), int(input()))