def isIntersect(a,b,c):
    for x in a:
        if x in b and x in c:
            return True
    return False

def main():
    a = input().strip("[]").split(", ")
    b = input().strip("[]").split(", ")
    c = input().strip("[]").split(", ")
    print(isIntersect(a,b,c))
main()
