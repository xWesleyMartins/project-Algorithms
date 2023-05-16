def find_duplicate(nums):
    num_set = set()

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False

        if num in num_set:
            return num

        num_set.add(num)

    return False
