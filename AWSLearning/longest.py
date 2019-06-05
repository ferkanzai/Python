def get_longest(string):

    words = string.split()

    longest = ''

    for word in words:
        if len(word) % 2 == 0 and len(word) >= len(longest):
            if len(word) == len(longest):
                continue
            else:
                longest = word

#    print(longest)
    print("The word \"{w}\" is the longest and has {n} characters".format(w=longest, n=len(longest)))


get_longest(input("Type a phrase and I'll let you know the longest word on it with an even number of letters: "))
