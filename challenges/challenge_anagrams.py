def merge(character_list, left, right):
    i_left = i_right = i_total = 0
    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            character_list[i_total], i_left = left[i_left], i_left + 1
        else:
            character_list[i_total], i_right = right[i_right], i_right + 1
        i_total += 1
    for i in range(i_left, len(left)):
        character_list[i_total], i_total = left[i], i_total + 1
    for i in range(i_right, len(right)):
        character_list[i_total], i_total = right[i], i_total + 1


def sort(character):
    if len(character) <= 1:
        return character
    mid = len(character) // 2
    left = sort(character[:mid])
    right = sort(character[mid:])
    merge(character, left, right)
    return character


def is_anagram(first_string, second_string):
    first_list = sort(list(first_string.lower()))
    second_list = sort(list(second_string.lower()))
    first_sorted = "".join(first_list)
    second_sorted = "".join(second_list)
    if not first_sorted or not second_sorted:
        return (first_sorted, second_sorted, False)
    return (first_sorted, second_sorted, first_sorted == second_sorted)
