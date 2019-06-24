fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tmp = line.split()
    #tmp2 = tmp.split()
    #tmp.append(line.strip())
    #print(tmp)
    for word in tmp:
        if word not in lst:
            lst.append(word)
print(sorted(lst))