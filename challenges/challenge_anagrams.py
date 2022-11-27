def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]
    return array


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    first_string_lowercase = first_string.lower()
    second_string_lowercase = second_string.lower()

    first_list_sorted = selection_sort(list(first_string_lowercase))
    second_list_sorted = selection_sort(list(second_string_lowercase))
    first_string_sorted = "".join(first_list_sorted)
    second_string_sorted = "".join(second_list_sorted)
    anagram = first_string_sorted == second_string_sorted

    return (first_string_sorted, second_string_sorted, anagram)
