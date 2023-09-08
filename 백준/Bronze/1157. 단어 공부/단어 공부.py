s = input()
s = s.upper()
word = dict()

for i in s:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

sorted_word = dict(sorted(word.items(), key=lambda x:x[1], reverse=True))

if len(word) == 1:
    print(next(iter(sorted_word)))

else:
    first_key = list(sorted_word.keys())[0]
    second_key = list(sorted_word.keys())[1]

    if sorted_word[first_key] == sorted_word[second_key]:
        print("?")
    else: print(first_key)
