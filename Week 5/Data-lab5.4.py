def calculator(n):
    if n == 1:
        print("1")
    else:
        a = sum(len(str(i)) for i in range(1,n+1))
        print(a+n)

def main():
    n = int(input())
    calculator(n)
main()