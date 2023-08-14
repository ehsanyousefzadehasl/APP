num = int(input())

english_dic = dict()
french_dic = dict()
german_dic = dict()

for i in range(num):
    fa, en, fr, gr = input().split()
    english_dic[en] = fa
    french_dic[fr] = fa
    german_dic[gr] = fa

sentence_to_translate = input().split()

translated_sentence = []

for element in sentence_to_translate:
    if element in english_dic:
        translated_sentence.append(english_dic[element])
    elif element in french_dic:
        translated_sentence.append(french_dic[element])
    elif element in german_dic:
        translated_sentence.append(german_dic[element])
    else:
        translated_sentence.append(element)

# print(translated_sentence)

for word in translated_sentence:
    print(word, end=" ")

# -------- input ----------
# 4
# man I je ich
# kheili very très sehr
# alaghemand interested intéressé interessiert 
# barnamenevisi programming laprogrammation Programmierung
# I am very interested in programming

# -------- output ----------
# man am kheili alaghemand in barnamenevisi