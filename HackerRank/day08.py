n = int(input())
lst = [input().split() for i in range(n)]
dict = {k: v for k, v in lst}

while True:
    try:
        name = input()
        if name not in dict:
            print("Not found")
        elif name in dict:
            print(name + "=" + dict.get(name))
        else:
            break
    except EOFError:
        break
