t = int(input())

for i in range(0, t):
    lst = []
    string = input()
    even = ""
    odd = ""
    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
    lst.append(even)
    lst.append(odd)
    print(even + " " + odd)
    print(lst[0] + " " + lst[1])
