def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        orig_high_other = i
        i = i.lower()
        if root_word in i:
            same_words.append(orig_high_other)
        elif i in root_word:
            same_words.append(orig_high_other)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)