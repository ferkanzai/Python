t = int(input())
for i in range(0, t):
    string = input()
    even = ""
    odd = ""
    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
    print(even + " " + odd)
