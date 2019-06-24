fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
dic = {}
mails = []
for line in fh:
    count = 0
    if line.startswith('From '):
        mail = line.split()[1]
        if dic.get(mail):
            dic[mail] += 1
        else:
            dic[mail] = 1
#As per the web the following throws a ValueError: Keyword arguments are not supported by this function on line 16
#maximum = max(dic, key=dic.get)
#print(maximum, dic[maximum])

max_key = None
max_value = None

for key, val in dic.items():

    if max_value is None or val > max_value:
        max_value = val
        max_key = key

print(max_key, max_value)
