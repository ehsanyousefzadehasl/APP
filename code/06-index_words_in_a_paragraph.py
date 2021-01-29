def is_capitalized(in_string):
    part1, part2 = in_string[0], in_string[1:len(in_string)]
    # print(part1, part2)
    if part1.isupper() == True and part2.islower() == True:
        return 1
    else:
        return 0

index_words = []

_in = []
_in = input().split(".")

cursor = 0
for sentence in _in:

    word_list_of_sentence = sentence.split()

    for i in range(1, len(word_list_of_sentence)):
        word  = word_list_of_sentence[i]
        if(word[len(word) - 1] == ","):
            word = word[0:len(word) - 1]
        if is_capitalized(word):
            index_words.append((str(i + cursor + 1), word))

    cursor = cursor + len(word_list_of_sentence)

if len(index_words) == 0:
    print("None")
else:
    for element in index_words:
        print(element[0] + ":" + element[1])

# --------- input -----------
# The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. 
# This video was captured by one of our heroes who wishes peace.

# -------- output -----------
# 2:Persian
# 3:League
# 15:Iran
# 17:Persian
# 18:League