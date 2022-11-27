def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if len(word) <= 2 and word[low_index] == word[high_index]:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word[1:-1], 0, -1)
