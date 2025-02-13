def summation(n):
    a = 0
    if n > 1:
        a += (n+1)*(n/2)
        print(int(a))
    else:
        print(0)

def main():
    n = int(input())
    summation(n)
main()