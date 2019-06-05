string = 'ACCGGGTTTTAAAA'
reversed = string[::-1]
swapped = ''
for i in range(len(reversed)):
    if reversed[i] == 'A':
        swapped = swapped + 'T'
    elif reversed[i] == 'T':
        swapped = swapped + 'A'
    elif reversed[i] == 'C':
        swapped = swapped + 'G'
    elif reversed[i] == 'G':
        swapped = swapped + 'C'
print(swapped)
