import string


def dicts_1(dictionary, string):
    ans = [dictionary.get(char) if dictionary.get(char) != None else char for char in string]
    return ('').join(ans)

def dicts_2(string):
    ans = {}
    for char in string:
        if char in ans:
            ans[char] += 1
        else:
            ans[char] = 1
    return ans

#print (dicts_2('banana'))

import string
def dicts_3(text):
    words = text.split()
    removed_punct = [i.strip(string.punctuation) for i in words]
    ans = {}
    for word in removed_punct:
        if word in ans:
            ans[word]+=1
        else:
            ans[word]=1
    return ans

def dicts_4(name, name2):
    with open(name, mode="r", encoding="cp1251") as f, open(name2, mode="w", encoding="cp1251") as g:
        all_lines = f.read().lower()
        dictionary = dicts_3(all_lines)
        for word, counter in dictionary.items():
            strin = f'{word};{counter}'
            g.write(strin + '\n')

#print(dicts_4('text1.txt', 'text2.txt'))
