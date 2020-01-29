'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    print(word)
    amt_th = 0
    # print(f"count before: {amt_th}")
    # base case: if the length of string word is equal to 1
    if len(word) <= 1:
        return 0
    # converge on base case: 
    # if the first two letters are th
    if word[0] + word[1] == 'th':
        # then return 1 + send the word from index 1 to last index back into count_th
        amt_th = 1 + count_th(word[1:]) 
        # print(f"found 'th' - count after: {amt_th}")  
    # if the first two letters are not th
    else:
        # then send the word from index 1 to last index back into count_th
        # print(f"did not find 'th'- count after: {amt_th}")
        return count_th(word[1:])
    return amt_th

# count_th("abcthefthghith")