def match_words(words):
    ctr = 0
    Lst = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            lst.append(i)
        print("list of words with the first and last charecter same\n", lst)
        return ctr
    count = match_words(['abc', 'cfc', 'xyz', aba, '1221'])
    print("number of words having first and last charecter same:", count)