def is_palindrome_iterative(word):
    if word:
        return word.lower() == word[::-1].lower()
    else:
        return False
