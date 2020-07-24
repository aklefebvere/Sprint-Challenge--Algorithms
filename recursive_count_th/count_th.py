'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # If the passed in word has less than two characters
    if len(word) < 2:
        # return 0
        return 0
    # if the word is greater than 2 characters
    else:
        # if the first two characters are "th"
        if word[0:2] == "th":
            # return 1 + the return of the function count_th
            return 1 + count_th(word[2:])
        # if the firs two characters are not "th"
        else:
            # call the count_th function using the word incremented by 1
            return count_th(word[1:])
