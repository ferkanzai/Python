import re

sum_file = input('Enter the name of the file: ')
total = 0
with open(sum_file, 'r') as sum_file:
    for line in sum_file:
        nums = re.findall('[0-9]+', line)
        for num in nums:
            total += int(num)
print(total)