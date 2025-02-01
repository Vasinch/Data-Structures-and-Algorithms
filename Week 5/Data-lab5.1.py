def summation(n):
    a = 0
    if n > 1:
        a += (n+1)*(n/2)
        print(int(a))
    else:
        print(0)

def summation1(n):
    a = 0
    for i in range(1,n+1):
        a += i
    print(a)

def main():
    n = int(input())
    summation(n)
    summation1(n)
main()
