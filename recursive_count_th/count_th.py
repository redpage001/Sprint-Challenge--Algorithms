'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    key = 'th'
    key_length = len(key)
    word_length = len(word)

    if word_length < key_length:
        return 0
    elif word[0:key_length] == key:
        return count_th(word[key_length - 1:]) + 1
    else:
        return count_th((word[key_length - 1:]))