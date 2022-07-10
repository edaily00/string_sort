#Author: Eric Daily
#Github username: edaily00
#Date: 7/9/2022
#This program takes a list of words and sorts them alphabetically
def string_sort(word_list):
    for i in range(1, len(word_list)):
        j = i
        while word_list[j - 1].lower() > word_list[j].lower() and j > 0:
            temp = word_list[j - 1]
            word_list[j - 1] = word_list[j]
            word_list[j] = temp
            j -= 1

