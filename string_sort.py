
def string_sort(word_list):
    for i in range(1, len(word_list)):
        j = i
        while word_list[j - 1].lower() > word_list[j].lower() and j > 0:
            temp = word_list[j - 1]
            word_list[j - 1] = word_list[j]
            word_list[j] = temp
            j -= 1

