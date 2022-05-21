from itertools import product
import string
from collections import OrderedDict

#use crane
#use slipt
import enchant
G = ["NA","NA","NA","NA","NA"]
unknown = 5
O = [[],[],[],[],[]]
H = []
B = []
used_words = []

for p in range(6):
    U = []
    list_of_lists = []
    letters = input("Input letters as string: ")
    colors = input("Input colors as string Orange Black Green (eg. OOBGB): ")
    if(colors == "GGGGG"):
        print("Congrats!")
        exit()
    used_words.append(letters)
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
    letterlist = Convert(letters)
    colorlist = Convert(colors)
    for i in range(len(letterlist)):
        if(colorlist[i] == "G"):
            if G[i] != letterlist[i]:
                G[i] = letterlist[i]
                unknown -= 1
        if(colorlist[i] == "O"):
            O[i].append(letterlist[i])
            H.append(letterlist[i])
        if(colorlist[i] == "B"):
            if(letterlist[i] not in H):
                B.append(letterlist[i])

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    for i in range(len(alphabet_list)):
        if alphabet_list[i] not in B:
            U.append(alphabet_list[i])

    d = enchant.Dict("en_US")

    combos = product(U, repeat=unknown)

    def newthing(list):
        new_list = G.copy()
        k = 0
        for i in range(len(new_list)):
            if(new_list[i] == "NA"):
                new_list[i] = list[k]
                k += 1
        flag = 0
        if d.check(''.join(new_list)) == True and new_list[0] not in O[0] and new_list[1] not in O[1] and new_list[2] not in O[2] and new_list[3] not in O[3] and new_list[4] not in O[4]:
            for j in range(len(H)):
                if H[j] not in new_list:
                    flag = 1
            if flag == 0:
                list_of_lists.append(''.join(new_list))

    hello = list(combos)
    for i in range(len(hello)):
        newthing(list(hello[i]))

    semi_final_list = list(OrderedDict.fromkeys(list_of_lists))
    final_list = []
    for i in range(len(semi_final_list)):
        if(semi_final_list[i] not in used_words):
            final_list.append(semi_final_list[i])
    print(final_list)