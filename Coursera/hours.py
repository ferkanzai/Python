name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = {}

for line in handle:
    if line.startswith('From '):    
        time = line.split()[5].split(':')[0]
        #print(time)
        dic[time] = dic.get(time, 0) + 1

sort_dic = sorted(dic)
tmp = sorted([(k, v) for (k, v) in dic.items()])

for time in tmp:
    print(time[0], time[1])
